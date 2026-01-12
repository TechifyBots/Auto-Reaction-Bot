import logging
import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client, filters, StopPropagation, enums
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ChatJoinRequest, ChatMemberUpdated
from pyrogram.errors import UserNotParticipant, ChatAdminRequired
from config import AUTH_CHANNELS, AUTH_REQ_CHANNELS, ADMIN, DB_URI, DB_NAME, IS_FSUB, FSUB_EXPIRE

class TechifyBots:
    def __init__(self):
        client = AsyncIOMotorClient(DB_URI)
        db = client[DB_NAME]
        self.join_requests = db["join_requests"]
        self.fsub_cache = db["fsub_cache"]

    async def add_join_req(self, user_id: int, channel_id: int):
        await self.join_requests.update_one({"user_id": user_id}, {"$addToSet": {"channels": channel_id}, "$set": {"created_at": datetime.datetime.utcnow()}}, upsert=True)

    async def has_joined_channel(self, user_id: int, channel_id: int) -> bool:
        doc = await self.join_requests.find_one({"user_id": user_id})
        return bool(doc and channel_id in doc.get("channels", []))

    async def del_join_req(self):
        await self.join_requests.drop()
        await self.fsub_cache.drop()

    async def save_fsub_msg(self, user_id: int, message_id: int):
        await self.fsub_cache.update_one({"user_id": user_id}, {"$set": {"message_id": message_id, "created_at": datetime.datetime.utcnow()}}, upsert=True)

    async def get_fsub_msg(self, user_id: int):
        doc = await self.fsub_cache.find_one({"user_id": user_id})
        return doc.get("message_id") if doc else None

    async def delete_fsub_msg_db(self, user_id: int):
        await self.fsub_cache.delete_one({"user_id": user_id})

tb = TechifyBots()

async def check_all_channels_joined(bot: Client, user_id: int):
    for channel_id in AUTH_CHANNELS:
        try:
            await bot.get_chat_member(channel_id, user_id)
        except UserNotParticipant:
            return False
        except Exception:
            pass
    for channel_id in AUTH_REQ_CHANNELS:
        if not await tb.has_joined_channel(user_id, channel_id):
            return False
    return True

async def auto_delete_fsub_and_start(client: Client, user_id: int):
    if not await check_all_channels_joined(client, user_id):
        return
    msg_id = await tb.get_fsub_msg(user_id)
    if msg_id:
        try:
            await client.delete_messages(user_id, msg_id)
        except Exception:
            pass
        await tb.delete_fsub_msg_db(user_id)
    user = await client.get_users(user_id)
    bot_user = await client.get_me()
    try:
        await client.send_message(user_id, f"**{user.mention},\n\nʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ ᴀʟʟ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs.\n\nᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("▶️ 𝖲𝗍𝖺𝗋𝗍", url=f"https://telegram.me/{bot_user.username}?start=start")]]))
    except Exception as e:
        logging.error(f"Failed to send start link to {user_id}: {e}")

def is_auth_req_channel(_, __, update):
    return update.chat.id in AUTH_REQ_CHANNELS

@Client.on_chat_join_request(filters.create(is_auth_req_channel))
async def join_reqs(client: Client, message: ChatJoinRequest):
    await tb.add_join_req(message.from_user.id, message.chat.id)
    await auto_delete_fsub_and_start(client, message.from_user.id)

@Client.on_chat_member_updated(filters.chat(AUTH_CHANNELS))
async def check_normal_join(client: Client, message: ChatMemberUpdated):
    if message.from_user and message.new_chat_member and message.new_chat_member.status in [enums.ChatMemberStatus.MEMBER, enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
        await auto_delete_fsub_and_start(client, message.from_user.id)

@Client.on_message(filters.command("delreq") & filters.private & filters.user(ADMIN))
async def del_requests(client: Client, message: Message):
    await tb.del_join_req()
    await message.reply("**⚙ Successfully join request cache deleted.**")

async def is_subscribed(bot: Client, user_id: int):
    missing = []
    expire_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=FSUB_EXPIRE) if FSUB_EXPIRE > 0 else None
    for channel_id in AUTH_CHANNELS:
        try:
            await bot.get_chat_member(channel_id, user_id)
        except UserNotParticipant:
            try:
                chat = await bot.get_chat(channel_id)
                invite = await bot.create_chat_invite_link(channel_id, expire_date=expire_at)
                missing.append((chat.title, invite.invite_link))
            except ChatAdminRequired:
                logging.error(f"Bot not admin in auth channel {channel_id}")
            except Exception:
                pass
        except Exception:
            pass
    return missing

async def is_req_subscribed(bot: Client, user_id: int):
    missing = []
    for channel_id in AUTH_REQ_CHANNELS:
        if await tb.has_joined_channel(user_id, channel_id):
            continue
        try:
            chat = await bot.get_chat(channel_id)
            invite = await bot.create_chat_invite_link(channel_id, creates_join_request=True)
            missing.append((chat.title, invite.invite_link))
        except ChatAdminRequired:
            logging.error(f"Bot not admin in request channel {channel_id}")
        except Exception:
            pass
    return missing

async def get_fsub(bot: Client, message: Message) -> bool:
    user_id = message.from_user.id
    if user_id == ADMIN:
        return True
    old_msg_id = await tb.get_fsub_msg(user_id)
    if old_msg_id:
        try:
            await bot.delete_messages(user_id, old_msg_id)
        except Exception:
            pass
        await tb.delete_fsub_msg_db(user_id)
    missing = []
    if AUTH_CHANNELS:
        missing.extend(await is_subscribed(bot, user_id))
    if AUTH_REQ_CHANNELS:
        missing.extend(await is_req_subscribed(bot, user_id))
    if not missing:
        return True
    bot_user = await bot.get_me()
    buttons = []
    for i in range(0, len(missing), 2):
        row = []
        for j in range(2):
            if i + j < len(missing):
                title, link = missing[i + j]
                row.append(InlineKeyboardButton(f"{i + j + 1}. {title}", url=link))
        buttons.append(row)
    buttons.append([InlineKeyboardButton("🔄 𝖳𝗋𝗒 𝖠𝗀𝖺𝗂𝗇", url=f"https://telegram.me/{bot_user.username}?start=start")])
    msg = await message.reply(f"**{message.from_user.mention},\n\n𝖸𝗈𝗎 𝗆𝗎𝗌𝗍 𝗃𝗈𝗂𝗇 𝖠𝖫𝖫 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌 𝖻𝖾𝗅𝗈𝗐 𝗍𝗈 𝗎𝗌𝖾 𝗍𝗁𝖾 𝖻𝗈𝗍!\n\n𝖱𝖾𝗊𝗎𝗂𝗋𝖾𝖽 𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌 ({len(missing)}):**", reply_markup=InlineKeyboardMarkup(buttons))
    await tb.save_fsub_msg(user_id, msg.id)
    return False

@Client.on_message(filters.private & ~filters.user(ADMIN) & ~filters.bot & ~filters.service & ~filters.me, group=-10)
async def global_fsub_checker(client: Client, message: Message):
    if not IS_FSUB:
        return
    if not await get_fsub(client, message):
        raise StopPropagation
