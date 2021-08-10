from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} ,<b>𝙸'𝚖 𝙰 𝙿𝙾𝚆𝙴𝚁𝙵𝚄𝙻𝙻 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚛 𝙱𝚘𝚝 𝙵𝚛𝚘𝚖 𝙹𝙽𝚂 𝙱𝙾𝚃𝚂 𝚆𝚒𝚝𝚑 𝚊𝚍𝚍𝚎𝚍 𝚙𝚕𝚊𝚢𝚕𝚒𝚜𝚝 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚂𝚞𝚙𝚙𝚘𝚛𝚝💯.\n

𝙿𝚕𝚎𝚊𝚜𝚎 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚊𝚗𝚢 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚕𝚒𝚗𝚔, 𝙸 𝚌𝚊𝚗 𝚞𝚙𝚕𝚘𝚊𝚍 𝚒𝚝 𝚝𝚘 𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚊𝚜 𝙵𝚒𝚕𝚎/𝚅𝚒𝚍𝚎𝚘</b>

𝙲𝚕𝚒𝚌𝚔 /help 𝚏𝚘𝚛 𝚖𝚘𝚛𝚎 𝚍𝚎𝚝𝚊𝚒𝚕𝚜......
\n\n
 <b>♕ 𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 ♛</b> <a href="https://t.me/jns_bots">ＪƝ⟆ ᗷ〇Ƭ⟆</a>🎊
"""


    HELP_TEXT = """
𝙷𝚎𝚕𝚕𝚘 {}  🙋🏻‍♀️ , <b> 𝙸'𝚊𝚖 𝚊 𝚜𝚒𝚖𝚙𝚕𝚎 𝚢𝚘𝚞𝚝𝚞𝚋𝚎 𝚟𝚒𝚍𝚎𝚘 𝚕𝚒𝚗𝚔 𝚝𝚘 𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚏𝚒𝚕𝚎 𝚘𝚛 𝚖𝚎𝚍𝚒𝚊 𝚞𝚙𝚕𝚘𝚊𝚍𝚎𝚛 𝚋𝚘𝚝 𝚠𝚒𝚝𝚑 𝚙𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚜𝚞𝚙𝚙𝚘𝚛𝚝.</b> \n
<b><u>𝙻𝚒𝚗𝚔 𝚝𝚘 𝙼𝚎𝚍𝚒𝚊 𝚘𝚛 𝙵𝚒𝚕𝚎</u></b>💾
➠ 𝚂𝚎𝚗𝚍 𝚊 𝚢𝚘𝚞𝚝𝚞𝚋𝚎 𝚟𝚒𝚍𝚎𝚘 𝚕𝚒𝚗𝚔 𝚏𝚘𝚛 𝚞𝚙𝚕𝚘𝚊𝚍 𝚝𝚘 𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚏𝚒𝚕𝚎 𝚘𝚛 𝚖𝚎𝚍𝚒𝚊.

<b><u>𝚂𝚎𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕</u></b>⛓️
➠ 𝚂𝚎𝚗𝚍 𝚊 𝚙𝚑𝚘𝚝𝚘 𝚝𝚘 𝚖𝚊𝚔𝚎 𝚒𝚝 𝚊𝚜 𝚙𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕.

<b><u>𝙳𝚎𝚕𝚎𝚝𝚒𝚗𝚐 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕</u></b>🗑️
➠ 𝚂𝚎𝚗𝚍 /delthumb 𝚝𝚘 𝚍𝚎𝚕𝚎𝚝𝚒𝚗𝚐 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕.

<b><u>𝚂𝚑𝚘𝚠 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕</u></b>🖥️
➠ 𝚂𝚎𝚗𝚍 /showthumb 𝚝𝚘 𝚟𝚒𝚎𝚠 𝚌𝚞𝚜𝚝𝚘𝚖 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕.

 <b>♕ 𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 ♛</b> <a href="https://t.me/jns_bots">ＪƝ⟆ ᗷ〇Ƭ⟆</a>🎊
"""
    ABOUT_TEXT = """
🤖 𝗠𝗬 𝗡𝗔𝗠𝗘 : <a href="https://t.me/JNS_YOYTUBE_BOT">JNS YT DOWNLOADER</a>
    
📣𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : <a href="https://t.me/jns_bots">ＪƝ⟆ ᗷ〇Ƭ⟆</a>

👲 𝗗𝗘𝗩𝗟𝗢𝗣𝗘𝗥 : <a href="https://t.me/jintons">JINTO NS</a>❤

📜𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘 : <a href="https://www.python.org/">Python3</a>

✨𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href="https://t.me/githubsoursecode">CLICK</a>

📮 𝗙𝗥𝗔𝗠𝗘𝗪𝗢𝗥𝗞 : <a href="https://github.com/pyrogram/pyrogram">PYROGRAM</a>
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Developer🧑‍💻', url='https://t.me/naviya2'),
        InlineKeyboardButton('Rate us ★', url='https://t.me/tlgrmcbot?start=leoyoutubedownloaderbot-review')
        ],[
        InlineKeyboardButton('Updates Channel 🗣', url='https://telegram.me/new_ehi'),
        InlineKeyboardButton('Support Group 👥', url='https://telegram.me/leosupportx')
        ],[
        InlineKeyboardButton('Help🆘', callback_data='help'),
        InlineKeyboardButton('About❗', callback_data='about'),
        InlineKeyboardButton('Plan💸', callback_data='plan')
        ],[
        InlineKeyboardButton('Close❎', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home🏠', callback_data='home'),
        InlineKeyboardButton('About❗', callback_data='about'),
        InlineKeyboardButton('Plan💸', callback_data='plan')
        ],[
        InlineKeyboardButton('Close❎', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home🏠', callback_data='home'),
        InlineKeyboardButton('Help🆘', callback_data='help'),
        InlineKeyboardButton('Plan💸', callback_data='plan')
        ],[
        InlineKeyboardButton('Close❎', callback_data='close')
        ]]
    )
    PLAN_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home🏠', callback_data='home'),
        InlineKeyboardButton('About❗', callback_data='about'),
        InlineKeyboardButton('Help🆘', callback_data='Help')
        ],[
        InlineKeyboardButton('Close❎', callback_data='close')
        ]]
    )
@Client.on_callback_query()
async def cb_data(bot, update):
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
    else:
        await update.message.delete()

    PLAN_TEXT = """
<b>Hai {} Your Plan Details</b>
<code>Plan name: Free User
Expires on: Until my Death 😍</code>
"""
    BLOCK_LIST_TEXT = "This url is blocked so I can not upload this 🙅 URL.\n\nUse @JNS_URLUPLOADERbot"
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>🙅"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>📥Downloading To My server Please Wait patiently...</code> 😉 "    
    UPLOAD_START = "<code>📤Uploading into Telegram...😉</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, 😔 I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @JNS_BOTS"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
