import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", ))

    API_HASH = str(os.environ.get("API_HASH", ""))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", ""))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1940030638))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    START = str(os.environ.get("START_TEXT", "hi"))

    HELP = str(os.environ.get("HELP_TEXT", "try @groupdc"))

    DONATE = str(os.environ.get("DONATE_TEXT", """Paytm : 9677804820
UPI : 9677804820@paytm
         9677804820@ybl
         9677804820@ibl
         9677804828@postbank

If payment not support try UPI to pay.

After payment send screenshot"""))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", ""))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://t.me/GroupDcBots"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://t.me/groupdc"))

    DB_URL = str(os.environ.get("DB_URL", ""))
    
    DB_NAME = str(os.environ.get("DB_NAME", "dcbotsoff"))
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))

