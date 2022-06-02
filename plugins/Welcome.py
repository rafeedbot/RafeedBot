from pyrogram import filters, Client as Rocky
from pyrogram.types import Message

@Rocky.on_message(filters.new_chat_members & filters.group)
async def welcome_msg(bot, message):
    await msg.reply_text(
        text=f"{WELCOME_MSG}"
    )

@Rocky.on_message(filters.command("setwelcome"))
async def welcome_txt(bot, message):
    WELCOME_MSG = message.reply_to_message.text
    mention = message.from_user.mention
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    title = message.chat.title
    await message.reply_text(
        text=f"YOURE WELCOME MESSAGE IS : {WELCOME_MSG}"
    )
