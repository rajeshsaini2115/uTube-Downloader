import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        parse_mode="html", disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT.format(update.from_user.mention),
        parse_mode="html", disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ JOIN UPDATES CHANNEL ⚙', url='https://telegram.me/jns_bots')]]),
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT.format(update.from_user.mention),
        parse_mode="html", disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ JOIN UPDATES CHANNEL ⚙', url='https://telegram.me/jns_bots')]]),
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["plan"]) & filters.private)
async def plan(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.PLAN_TEXT.format(update.from_user.mention),
        parse_mode="html", disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ JOIN UPDATES CHANNEL ⚙', url='https://telegram.me/jns_bots')]]),
        reply_to_message_id=update.message_id
    )
