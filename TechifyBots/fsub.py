from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import AUTH_CHANNELS
from pyrogram import Client
from pyrogram.types import Message
from typing import List
from pyrogram.errors import UserNotParticipant

async def get_fsub(bot: Client, message: Message) -> bool:
    tb = await bot.get_me()
    user_id = message.from_user.id
    not_joined_channels = []
    for channel_id in AUTH_CHANNELS:
        try:
            await bot.get_chat_member(channel_id, user_id)
        except UserNotParticipant:
            chat = await bot.get_chat(channel_id)
            invite_link = chat.invite_link or await bot.export_chat_invite_link(channel_id)
            not_joined_channels.append((chat.title, invite_link))
    if not_joined_channels:
        join_buttons = []
        for i in range(0, len(not_joined_channels), 2):
            row = []
            for j in range(2):
                if i + j < len(not_joined_channels):
                    title, link = not_joined_channels[i + j]
                    button_text = f"{i + j + 1}. {title}"
                    row.append(InlineKeyboardButton(button_text, url=link))
            join_buttons.append(row)
        join_buttons.append([InlineKeyboardButton("🔄 Try Again", url=f"https://telegram.me/{tb.username}?start=start")])
        await message.reply(f"**🎭 {message.from_user.mention}, As I see, you haven’t joined my channel yet.\nPlease join by clicking the button below.**", reply_markup=InlineKeyboardMarkup(join_buttons))
        return False
    return True
