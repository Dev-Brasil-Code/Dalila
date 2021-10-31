import re
from os import environ
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/79a0f0fb6854119f587af.jpg https://telegra.ph/file/bbb66ddf51e86efd86516.jpg https://telegra.ph/file/c553385cdb905f16c344e.jpg https://telegra.ph/file/1c8442c7ee7231f871115.jpg https://telegra.ph/file/ab02104cc6450e488dba5.jpg https://telegra.ph/file/221ad5cbd1d92a3f4e058.jpg https://telegra.ph/file/5cf4769133a612fdca945.jpg https://telegra.ph/file/baca2d73704f3bea50508.jpg https://telegra.ph/file/823b482494e49f2e0ae79.jpg https://telegra.ph/file/cbf4559f7912f739fbeca.jpg https://telegra.ph/file/54268cbe52e82e7c1ca7e.jpg https://telegra.ph/file/ede9213ac4f11937cf395.jpg https://telegra.ph/file/274b267196edb4db909bf.jpg https://telegra.ph/file/b47dbd5b90e32236c6cee.jpg https://telegra.ph/file/0cc1f7f74ea6145e28281.jpg https://telegra.ph/file/bdd4b089eea3e581fc5d2.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "JPRoseBot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'mizotelegram')

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>File Name:</b> <code>{file_name}</code>\n\n<b>Join [ZoSeries Studio](https://t.me/joinchat/prE6ALN6x2hkY2E1) for more useful bots</b>\n\n<b>Size:</b> {file_size}\n{file_caption}.")
