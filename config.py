import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
OWNER_ID = int(os.environ.get("OWNER_ID", "6497757690"))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluser0")
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1001473043276"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1001495022147"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1001572271892"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1001723817903"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n ɪ ᴀᴍ ᴍᴜʟᴛɪ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ , ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ » @team_netflix</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5115691197 6273945163 6103092779 2005714953 5231212075 6497757690").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} 𝐁𝐫𝐨/𝐒𝐢𝐬 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬..\n\n 𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐚𝐧𝐝 𝐜𝐥𝐢𝐜𝐤 𝐨𝐧 “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @team_netflix</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @sewxiy"
ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
