import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from pyrogram import filters
from pyrogram import Client  as Mai_bOTs
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message

@Mai_bOTs.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        parse_mode="html", disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS,
        reply_to_message_id=update.message_id
    )


@Mai_bOTs.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT.format(update.from_user.mention),
        parse_mode="html", disable_web_page_preview=True,
        reply_markup=Translation.HELP_BUTTONS,
        reply_to_message_id=update.message_id
    )


@Mai_bOTs.on_message(filters.command(["about"]) & filters.private)
async def about(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT.format(update.from_user.mention),
        parse_mode="html", disable_web_page_preview=True,
        reply_markup=Translation.ABOUT_BUTTONS,
        reply_to_message_id=update.message_id
    )


@Mai_bOTs.on_message(filters.command(["plan"]) & filters.private)
async def plan(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.PLAN_TEXT.format(update.from_user.mention),
        parse_mode="html", disable_web_page_preview=True,
        reply_markup=Translation.PLAN_BUTTONS,
        reply_to_message_id=update.message_id
    )
@Mai_bOTs.on_callback_query()
async def cb_handler(client: Mai_bOTs , query: CallbackQuery):
    data = query.data
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
