from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} ,<b>πΈ'π π° πΏπΎππ΄ππ΅ππ»π» ππΎππππ±π΄ π³ππ πππππππ π±ππ π΅πππ πΉπ½π π±πΎππ ππππ πππππ ππππ’ππππ πππππππππ ππππππππ―.\n

πΏπππππ ππππ ππ πππ’ ππΎππππ±π΄ ππππ, πΈ πππ ππππππ ππ ππ ππππππππ ππ π΅πππ/πππππ</b>

π²ππππ /help πππ ππππ πππππππ......
\n\n
 <b>β πΏπΎππ΄ππ΄π³ π±π β</b> <a href="https://t.me/jns_bots">οΌͺΖβ α·γΖ¬β</a>π
"""


    HELP_TEXT = """
π·ππππ {}  ππ»ββοΈ , <b> πΈ'ππ π ππππππ π’ππππππ πππππ ππππ ππ ππππππππ ππππ ππ πππππ ππππππππ πππ π πππ πππππππππ πππππππππ πππππππ.</b> \n
<b><u>π»πππ ππ πΌππππ ππ π΅πππ</u></b>πΎ
β  ππππ π π’ππππππ πππππ ππππ πππ ππππππ ππ ππππππππ ππππ ππ πππππ.

<b><u>πππ πππππππππ</u></b>βοΈ
β  ππππ π πππππ ππ ππππ ππ ππ πππππππππ πππππππππ.

<b><u>π³πππππππ πππππππππ</u></b>ποΈ
β  ππππ /delthumb ππ ππππππππ πππππππππ.

<b><u>ππππ  πππππππππ</u></b>π₯οΈ
β  ππππ /showthumb ππ ππππ  ππππππ πππππππππ.

 <b>β πΏπΎππ΄ππ΄π³ π±π β</b> <a href="https://t.me/jns_bots">οΌͺΖβ α·γΖ¬β</a>π
"""
    ABOUT_TEXT = """
π€ π π¬ π‘ππ π : <a href="https://t.me/JNS_YOYTUBE_BOT">JNS YT DOWNLOADER</a>
    
π£ππππ‘π‘ππ : <a href="https://t.me/jns_bots">οΌͺΖβ α·γΖ¬β</a>

π² πππ©ππ’π£ππ₯ : <a href="https://t.me/jintons">JINTO NS</a>β€

ππππ‘ππ¨πππ : <a href="https://www.python.org/">Python3</a>

β¨π¦π’π¨π₯ππ ππ’ππ : <a href="https://t.me/githubsoursecode">CLICK</a>

π? ππ₯ππ ππͺπ’π₯π : <a href="https://github.com/pyrogram/pyrogram">PYROGRAM</a>
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Developerπ§βπ»', url='https://t.me/naviya2'),
        InlineKeyboardButton('Rate us β', url='https://t.me/tlgrmcbot?start=leoyoutubedownloaderbot-review')
        ],[
        InlineKeyboardButton('Updates Channel π£', url='https://telegram.me/new_ehi'),
        InlineKeyboardButton('Support Group π₯', url='https://telegram.me/leosupportx')
        ],[
        InlineKeyboardButton('Helpπ', callback_data='help'),
        InlineKeyboardButton('Aboutβ', callback_data='about'),
        InlineKeyboardButton('PlanπΈ', callback_data='plan')
        ],[
        InlineKeyboardButton('Closeβ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Homeπ ', callback_data='home'),
        InlineKeyboardButton('Aboutβ', callback_data='about'),
        InlineKeyboardButton('PlanπΈ', callback_data='plan')
        ],[
        InlineKeyboardButton('Closeβ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Homeπ ', callback_data='home'),
        InlineKeyboardButton('Helpπ', callback_data='help'),
        InlineKeyboardButton('PlanπΈ', callback_data='plan')
        ],[
        InlineKeyboardButton('Closeβ', callback_data='close')
        ]]
    )
    PLAN_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Homeπ ', callback_data='home'),
        InlineKeyboardButton('Aboutβ', callback_data='about'),
        InlineKeyboardButton('Helpπ', callback_data='Help')
        ],[
        InlineKeyboardButton('Closeβ', callback_data='close')
        ]]
    )

    PLAN_TEXT = """
<b>Hai {} Your Plan Details</b>
<code>Plan name: Free User
Expires on: Until my Death π</code>
"""
    BLOCK_LIST_TEXT = "This url is blocked so I can not upload this π URL.\n\nUse @JNS_URLUPLOADERbot"
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "<code>Analysing Your Link</code>β³"
    BANNED_USER_TEXT = "<code>You are Banned!</code>π"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>π₯Downloading To My server Please Wait patiently...</code> π "    
    UPLOAD_START = "<code>π€Uploading into Telegram...π</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, π I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @JNS_BOTS"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me ππ....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
