from pyrogram import filters, Client as Rocky
from pyrogram.types import Message

@Rocky.on_message(filters.new_chat_members & filters.group)
async def welcome_msg(bot, msg):
    await msg.reply_text(
        text=f"{WELCOME_MSG}"
    )

@Rocky.on_message(filters.command("setwelcome"))
async def welcome_txt(bot, msg):
    WELCOME_MSG = await msg.reply_to_Message.text
    mention = msg.from_user.mention
    id = msg.from_user.id
    name = msg.from_user.first_name
    username = msg.from_user.username
    title = msg.from_chat.title
    await msg.reply_text(
        text=f"YOURE WELCOME MESSAGE IS : {WELCOME_MSG}"
    )
