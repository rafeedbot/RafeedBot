from pyrogram import Client as Mr_bots, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Mr_bots.on_message(filters.command('setwelcome'))
async def welcome(bot: Messages, id: chat_id):
    welcome = message.reply_to_message.text
    await id.save(welcome)
    await bot.reply_text(
        text=f"youre welcome message saved {title} is {welcome}"
    )
      except: 
        await bot reply_text(
            text="nothing provided for welcome"
        )
        
            
