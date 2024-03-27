class script(object):
    START_TXT = """<b>سلام {}, <i>{}</i>
    
🎬 <a href=https://t.me/filmgirgp>جهت جستجو و دریافت فیلم و سریال اینجا کلیک کنید</a>

✅ کانال رسمی ما در تلگرام 
@MyFilmia</b>"""

    MY_ABOUT_TXT = """★ Server: <a href=https://www.heroku.com>Heroku</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>
★ Language: <a href=https://www.python.org>Python</a>
★ Library: <a href=https://pyrogram.org>Pyrogram</a>"""

    MY_OWNER_TXT = """★ Name: HA Bots
★ Username: @HA_Bots
★ Country: Sri Lanka 🇱🇰"""

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
🤑 Premium Users: <code>{}</code>
✨ Used Storage: <code>{}</code>
🗳 Free Storage: <code>{}</code>
🚀 Bot Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NO_RESULT_TXT = """#NoResult
★ Group Name: {}
★ Group ID: <code>{}</code>
★ Name: {}

★ Message: {}"""

    REQUEST_TXT = """★ Name: {}
★ ID: <code>{}</code>

★ Message: {}"""

    NOT_FILE_TXT = """👋 سلام {},

فیلم،سریال،انیمه <b>{}</b> در ربات یافت نشد! 🥲

👉 آیا نام سریال/فیلم را به درستی وارد کرده اید؟"""
    
    EARN_TXT = """<b>🍿 آموزش استفاده از ربات فیلم و سریال فیلمیا\n\n1- جهت جست و جوی فیلم در گروه نام فیلم را به صورت انگلیسی ارسال کنید\nبرای مثال :\nThe Nun\nجهت جست و جوی سریال/انیمه در گروه نام سریال را به صورت انگلیسی ارسال کنید\nبرای مثال :\nShogun S01E01\n(S01 به معنی فصل اول)\n(E01 به معنی قسمت اول اول)\</b>"""

    HOW_TXT = """<b>✅ مجوز نصب برنامه های ناشناخته در اندروید 13

1️⃣در اولین قدم به "Setting" مراجعه کنید.
2️⃣وارد بخش "برنامه ها" یا "Apps" شوید.
3️⃣روی "Special app access" ضربه بزنید.
4️⃣برای یافتن "نصب برنامه‌های ناشناخته" یا "Install unknown apps" به پایین بروید.
5️⃣در این بخش می‌توانید فهرست برنامه‌هایی را ببینید که می‌توانید به آنها اجازه دهید روی دستگاه اندروید نصب شوند.
6️⃣برنامه مورد نظر را انتخاب کنید و گزینه "Allow from this source" را تغییر دهید.

✅ فعالسازی Unknown sources در اندروید 10، 11 و 12
	
1	وارد بخش تنظیمات دستگاه اندروید خود شوید.
	2	به قسمت "Apps" مراجعه کنید. 
	3	روی "Special app access" ضربه بزنید. اگر نتوانستید آن را پیدا کنید، ابتدا به بخش "Advanced" بروید و سپس "Special app access" را انتخاب کنید.
	4	روی "نصب برنامه های ناشناخته" یا "Install unknown apps" ضربه بزنید.
	5	برنامه ناشناسی که قصد دارید روی دستگاه اندروید نصب کنید(معمولاً یک مرورگر یا برنامه Files) را انتخاب نمایید.
	6	گزینه "Allow from this source" را تغییر دهید تا مشکل دسترسی برنامه ها در اندروید حل شود. 

✅ اجازه نصب برنامه ها از منابع ناشناس در اندروید 8 و 9
	
1	به "Setting" بروید.
	2	به بخش "برنامه‌ها و اعلان‌ها" یا "Apps & notifications" مراجعه کنید.
	3	روی "Advanced" کلیک کنید. 
	4	گزینه "Special app access" را انتخاب کنید.
	5	روی "Install unknown apps" ضربه بزنید.
	6	برنامه ای را که می خواهید از منابع ناشناس نصب کنید انتخاب کنید.
	7	سوئیچ "Allow from this source" را تغییر دهید.

✅ چگونه مجوز نصب برنامه ها را در اندروید 7 یا پایین تر فعال کنیم؟
	
1	منوی برنامه را در دستگاه خود باز کنید و روی "Setting" ضربه بزنید تا وارد بخش تنظیمات شوید.
	2	دنبال گزینه "Security & fingerprint" یا "Security" بگردید.
	3	به پایین بروید و روی گزینه "Unknown sources" ضربه بزنید.
	4	یک پیام هشدار پاپ آپ ظاهر می شود. روی "OK" کلیک کنید.
	5	از منوی تنظیمات خارج شده و فایل APK را نصب کنید.

✅ اجازه نصب برنامه از منابع ناشناس در سامسونگ
	
1	به تنظیمات بروید.
	2	به بخش "Apps" مراجعه کنید. 
	3	روی نماد سه نقطه در گوشه سمت راست بالا ضربه بزنید.
	4	گزینه "Special access" را از منو انتخاب کنید.
	5	روی "Install unknown apps" ضربه بزنید.
	6	برای اجازه نصب برنامه از منابع ناشناس در سامسونگ، سوئیچ کنار برنامه‌ مورد نظر را فعال کنید. 

🔺اگر این مورد روی دستگاه سامسونگ شما کار نمی کند مراحل زیر را دنبال کنید:
	
1	به بخش "Setting" مراجعه کنید.
	2	روی "Biometrics and security" یا "Privacy" ضربه بزنید.
	3	گزینه "Install unknown apps" را انتخاب کنید.
	4	گزینه مربوط به برنامه مورد نظر را فعال کنید. 
چگونه مجوز نصب برنامه در گوشی شیائومی را فعال کنیم؟
	1	به بخش تنظیمات دستگاه مراجعه کنید.
	2	به پایین بروید و روی "Additional settings" ضربه بزنید.
	3	سپس "Privacy" را انتخاب کنید. 
	4	گزینه "Unknown sources"را پیدا کنید و آن را فعال کنید.</b>"""

    IMDB_TEMPLATE = """🎥: <code>{query}</code>

🏷 عنوان : <a href={url}>{title}</a>
🎭 ژانر : {genres}
📆 سال انتشار : <a href={url}/releaseinfo>{year}</a>
🌟 امتیاز : <a href={url}/ratings>{rating} / 10</a>
☀️ زبان : {languages}
📀 مدت زمان : {runtime} Minutes

🗣 درخواست توسط: {message.from_user.mention}
©️ آدرس وبسایت فیلمیا: <b>Filmia.org</b>
©️ کانال دانلود فیلم و سریال: <b>@MyFilmia</b>"""

    FILE_CAPTION = """<i>{file_name}</i>

کانال ما در تلگرام
@MyFilmia"""

    WELCOME_TEXT = """👋 سلام {mention}, به گروه {title} خوش آمدید! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Try each command without any argument to see more details 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇
 
/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/index - to index bot accessible channels</b>"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id
/openai - Find solution to any question with ChatGPT</b>"""

    SOURCE_TXT = """<b>ʙᴏᴛ ɢɪᴛʜᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ -

- ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

- ꜱᴏᴜʀᴄᴇ - <a href=https://github.com/HA-Bots/Auto-Filter-Bot>ʜᴇʀᴇ</a>

- ᴅᴇᴠʟᴏᴘᴇʀ - @HA_Bots"""

    SPAM_TXT = """{} Don't Spam, Wait For {}

Else, You Can Buy Our Subscriptions.
<a href={}>Click Here</a> To Learn More"""
