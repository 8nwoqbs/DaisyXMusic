from os import getenv

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "p_k_musicbot_channel")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/49b6430a55d795796853c.jpg")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Pk_music_bot_assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "p_k_musicbot_support")
PROJECT_NAME = getenv("PROJECT_NAME", "𝙋𝙍𝙄𝙉𝘾𝙀 𝙈𝙐𝙎𝙄𝘾 𝘽𝙊𝙏")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/8nwoqbs/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
