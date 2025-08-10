import random
import re
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import *
import asyncio
from Script import text
from .db import tb
from .fsub import get_fsub

def parse_button_markup(text: str):
    lines = text.split("\n")
    buttons = []
    final_text_lines = []
    for line in lines:
        row = []
        parts = line.split("||")
        is_button_line = True
        for part in parts:
            match = re.fullmatch(r"\[(.+?)\]\((https?://[^\s]+)\)", part.strip())
            if match:
                row.append(InlineKeyboardButton(match[1], url=match[2]))
            else:
                is_button_line = False
                break
        if is_button_line and row:
            buttons.append(row)
        else:
            final_text_lines.append(line)
    return InlineKeyboardMarkup(buttons) if buttons else None, "\n".join(final_text_lines).strip()

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    if await tb.get_user(message.from_user.id) is None:
        await tb.add_user(message.from_user.id, message.from_user.first_name)
        bot = await client.get_me()
        await client.send_message(
            LOG_CHANNEL,
            text.LOG.format(
                message.from_user.id,
                getattr(message.from_user, "dc_id", "N/A"),
                message.from_user.first_name or "N/A",
                f"@{message.from_user.username}" if message.from_user.username else "N/A",
                bot.username
            )
        )
    if IS_FSUB and not await get_fsub(client, message):return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=text.START.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ⇆', url='https://telegram.me/QuickReactRobot?startgroup=botstart')],
            [InlineKeyboardButton('ℹ️ 𝖠𝖻𝗈𝗎𝗍', callback_data='about'),
             InlineKeyboardButton('📚 𝖧𝖾𝗅𝗉', callback_data='help')],
            [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ⇆', url='https://telegram.me/QuickReactRobot?startchannel=botstart')]
        ])
    )

@Client.on_message(filters.command("help") & filters.private)
async def help_cmd(client, message):
    reply = await message.reply(
        text=("❓ <b>𝘏𝘢𝘷𝘪𝘯𝘨 𝘛𝘳𝘰𝘶𝘣𝘭𝘦?</b>\n\n𝘐𝘧 𝘺𝘰𝘶'𝘳𝘦 𝘧𝘢𝘤𝘪𝘯𝘨 𝘢𝘯𝘺 𝘱𝘳𝘰𝘣𝘭𝘦𝘮 𝘸𝘩𝘪𝘭𝘦 𝘶𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘣𝘰𝘵 𝘰𝘳 𝘪𝘵𝘴 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴, 𝘱𝘭𝘦𝘢𝘴𝘦 𝘸𝘢𝘵𝘤𝘩 𝘵𝘩𝘦 𝘵𝘶𝘵𝘰𝘳𝘪𝘢𝘭 𝘷𝘪𝘥𝘦𝘰 𝘣𝘦𝘭𝘰𝘸.\n\n🎥 𝘛𝘩𝘦 𝘷𝘪𝘥𝘦𝘰 𝘸𝘪𝘭𝘭 𝘤𝘭𝘦𝘢𝘳𝘭𝘺 𝘦𝘹𝘱𝘭𝘢𝘪𝘯 𝘩𝘰𝘸 𝘵𝘰 𝘶𝘴𝘦 𝘦𝘢𝘤𝘩 𝘧𝘦𝘢𝘵𝘶𝘳𝘦 𝘸𝘪𝘵𝘩 𝘦𝘢𝘴𝘦.\n\n💖 𝘍𝘰𝘳 𝘮𝘰𝘳𝘦 𝘶𝘱𝘥𝘢𝘵𝘦𝘴 — <b><a href='https://techifybots.github.io/PayWeb/'>𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘜𝘴.</a></b>"
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🎬 𝘞𝘢𝘵𝘤𝘩 𝘛𝘶𝘵𝘰𝘳𝘪𝘢𝘭", url="https://youtu.be/rOnzfDdYqnc")]
        ])
    )
    await asyncio.sleep(300)
    await reply.delete()
    try:
        await message.delete()
    except:
        pass

@Client.on_message(filters.command("stats") & filters.private & filters.user(ADMIN))
async def total_users(client, message):
    try:
        users = await tb.get_all_users()
        await message.reply(f"👥 **Total Users:** {len(users)}",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🎭 𝖢𝗅𝗈𝗌𝖾', callback_data='close')]]))
    except Exception as e:
        r=await message.reply(f"❌ *Error:* `{str(e)}`")
        await asyncio.sleep(30)
        await r.delete()

@Client.on_message(filters.group | filters.channel)
async def send_reaction(client: Client, msg: Message):
    try:
        await msg.react(random.choice(EMOJIS))
    except FloodWait as e:
        print(f"FloodWait: Sleeping for {e.value} seconds")
        await asyncio.sleep(e.value)
        await msg.react(random.choice(EMOJIS))
    except Exception as e:
        print(f"Error: {e}")

@Client.on_message(filters.command("broadcast") & filters.private & filters.user(ADMIN))
async def broadcasting_func(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("<b>Reply to a message to broadcast.</b>")
    msg = await message.reply_text("Processing broadcast...")
    to_copy_msg = message.reply_to_message
    users_list = await tb.get_all_users()
    completed = 0
    failed = 0
    raw_text = to_copy_msg.caption or to_copy_msg.text or ""
    reply_markup, cleaned_text = parse_button_markup(raw_text)
    for i, user in enumerate(users_list):
        user_id = user.get("user_id")
        if not user_id:
            continue
        try:
            if to_copy_msg.text:
                await client.send_message(user_id, cleaned_text, reply_markup=reply_markup)
            elif to_copy_msg.photo:
                await client.send_photo(user_id, to_copy_msg.photo.file_id, caption=cleaned_text, reply_markup=reply_markup)
            elif to_copy_msg.video:
                await client.send_video(user_id, to_copy_msg.video.file_id, caption=cleaned_text, reply_markup=reply_markup)
            elif to_copy_msg.document:
                await client.send_document(user_id, to_copy_msg.document.file_id, caption=cleaned_text, reply_markup=reply_markup)
            else:
                await to_copy_msg.copy(user_id)
            completed += 1
        except (UserIsBlocked, PeerIdInvalid, InputUserDeactivated):
            await tb.delete_user(user_id)
            failed += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                await to_copy_msg.copy(user_id)
                completed += 1
            except:
                failed += 1
        except Exception as e:
            print(f"Broadcast to {user_id} failed: {e}")
            failed += 1
        await msg.edit(f"Total: {i + 1}\nCompleted: {completed}\nFailed: {failed}")
        await asyncio.sleep(0.1)
    await msg.edit(
        f"😶‍🌫 <b>Broadcast Completed</b>\n\n👥 Total Users: <code>{len(users_list)}</code>\n✅ Successful: <code>{completed}</code>\n🤯 Failed: <code>{failed}</code>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎭 𝖢𝗅𝗈𝗌𝖾", callback_data="close")]])
    )
