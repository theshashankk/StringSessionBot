from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

k_but = InlineKeyboardMarkup([[InlineKeyboardButton('Generate string', callback_data='generate')]])
	
	

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.reply_text(f'Hey {msg.from_user.mention}\n\n__Click on Below Button to use me__', reply_markup=k_but)
