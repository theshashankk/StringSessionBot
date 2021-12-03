from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

k_but = InlineKeyboardMarkup([[InlineKeyboardButton('Generate string', callback_data='generate')]])
	
	

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	await bot.send_message(f'**Hey**\n\n__Click on Below Button to use me__', reply_markup=k_but)
