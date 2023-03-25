## 𝐁𝐢𝐤𝐚𝐬𝐡𝐡𝐚𝐥𝐝𝐞𝐫 & 𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫

import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import *

from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli


API_ID = int(os.environ.get("API_ID", None))
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL")
OWNER_ID = int(os.environ.get("OWNER_ID"))
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
BOT_NAME = os.environ.get("BOT_NAME")
START_IMG1 = os.environ.get("START_IMG1")
START_IMG2 = os.environ.get("START_IMG2")
START_IMG3 = os.environ.get("START_IMG3")
START_IMG4 = os.environ.get("START_IMG4")
START_IMG5 = os.environ.get("START_IMG5")
START_IMG6 = os.environ.get("START_IMG6")
START_IMG7 = os.environ.get("START_IMG7")
START_IMG8 = os.environ.get("START_IMG8")
START_IMG9 = os.environ.get("START_IMG9")
START_IMG10 = os.environ.get("START_IMG10")

bot = Client(
    "v_chat_bot" ,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

mongo = MongoCli(MONGO_URL)
db = mongo.bikash
chatsdb = db.chatsdb
usersdb = db.users

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


PHOTO = [
    START_IMG1,
    START_IMG2,
    START_IMG3,
    START_IMG4,
    START_IMG5,
    START_IMG6,
    START_IMG7,
    START_IMG8,
    START_IMG9,
    START_IMG10,
]

EMOJIOS = [ 
      "🇮🇳",
      "🌷",
      "🌹",
      "💐",
      "🌺",
      "🦁",
      "🐯",
      "🐶",
      "🐰",
      "🐢",
      "🪔",
      "📱",
      "❤️",
      "💧",
      "👻",
      "🔥",
      "🌻",
      "🕊",
      "🥀",
      "🇮🇳",
      "❣️",
      "🤫",
      "🙏",
      "☀️",
      "☁️",
      "🌤️",
      "🌨️",
      "🌤️",
      "🌛",
      "⭐",
      "🌌",
      "🌍",
]
      
START = f"""
━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐢  𝐈'𝐦 𝐀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🌷.\n\n📌 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 [{BOT_NAME}]({START_IMG1}) 🌷 𝐅𝐨𝐫𝐦 𝐈𝐧𝐝𝐢𝐚 🇮🇳 \n\n🌷 𝐈'𝐦 𝐀 𝐀𝐫𝐭𝐢𝐟𝐢𝐜𝐢𝐚𝐥 𝐈𝐧𝐭𝐞𝐥𝐥𝐢𝐠𝐞𝐧𝐜𝐞 🌷\n\n /chatbot - [on|off] 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐔𝐬𝐞 𝐎𝐧𝐥𝐲 𝐀𝐧𝐲 𝐆𝐫𝐨𝐮𝐩

┏━━━━━━━━━━━━━━━━━┓
┣❥︎ ♕︎ 𝐎𝐰𝐧𝐞𝐫 ♕︎ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{OWNER_USERNAME})
┣❥︎ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{UPDATE_CHNL})
┣❥︎ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{SUPPORT_GRP})
┣❥︎ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 ➪ » [𝐁𝐢𝐤𝐚𝐬𝐡](https://t.me/BikashHalder)
┗━━━━━━━━━━━━━━━━━┛

💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐂𝐡𝐚𝐭.
━━━━━━━━━━━━━━━━━━━━━━━━
"""
DEV_OP = [
    [
        InlineKeyboardButton(text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 🖥️︎", url=f"https://youtube.com/@BikashGadgetsTech"),
        InlineKeyboardButton(text="🇮🇳 𝐃𝐩𝐳 📱", url=f"https://t.me/BikashDp"),
    ],
    [
        InlineKeyboardButton(
            text="➕ ❰ 𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="⚙️ 𝐂𝐦𝐝 ⚙️", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="💠 𝐀𝐛𝐨𝐮𝐭 💠️", callback_data="ABOUT"),
    ],
]
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="➕ ❰ 𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(
             text="🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", 
             url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
HELP_READ = f"""
<u>**{BOT_NAME} 𝐀𝐥𝐥 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐂𝐦𝐝𝐬 🥀**</u>

<u>**🥀 𝐔𝐬𝐞 𝐁𝐞𝐥𝐨𝐰 𝐂𝐦𝐝❗**</u>

🥀 [𝐂𝐡𝐚𝐧𝐧𝐞𝐥](https://t.me/{UPDATE_CHNL}) & [𝐆𝐫𝐨𝐮𝐩](https://t.me/{SUPPORT_GRP}) 🥀
**──────────────**
<b>|| [𝐎𝐰𝐧𝐞𝐫](https://t.me/{OWNER_USERNAME})||</b>
"""
BACK = [
     [
           InlineKeyboardButton(text="↖⬅️ 𝐁𝐚𝐜𝐤 ⬅️", callback_data="BACK"),
     ],
]
HELP_BTN = [
     [
          InlineKeyboardButton(text="🤖 𝐁𝐨𝐭 🤖", callback_data="CHATBOT_CMD"),
          InlineKeyboardButton(text="🌻 𝐄𝐱𝐭𝐫𝐚 🌻", callback_data="TOOLS_DATA"),
     ],
     [
          InlineKeyboardButton(text="↖⬅️ 𝐁𝐚𝐜𝐤 ⬅️", callback_data="BACK"),
          InlineKeyboardButton(text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="CLOSE"),
     ],
]

CLOSE_BTN = [
      [
           InlineKeyboardButton(text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌️", callback_data="CLOSE"),
      ],
]

CHATBOT_ON = [
        [
            InlineKeyboardButton(text="✔️ 𝐄𝐧𝐚𝐛𝐥𝐞 ✔️", callback_data=f"addchat"),
            InlineKeyboardButton(text="❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞 ❌", callback_data=f"rmchat"),
        ],
]

PNG_BTN = [
    [
         InlineKeyboardButton(
             text="➕ ❰ 𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", 
                              callback_data="CLOSE",
         ),
     ],
]

TOOLS_DATA_READ = f"""
<u>** {BOT_NAME} 𝐀𝐥𝐥 𝐓𝐨𝐨𝐥𝐬 𝐇𝐞𝐫𝐞 ∇:**</u>
** 𝐔𝐬𝐞 : `/donate` 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 𝐎𝐰𝐧𝐞𝐑 𝐇𝐚𝐫𝐝 𝐖𝐨𝐫𝐤 🥀**
**──────────────**
** 𝐔𝐬𝐞 `/ping` 𝐅𝐨𝐫 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐏𝐢𝐧𝐠 𝐎𝐟 {BOT_NAME}**
**──────────────**
<b>||[𝐎𝐰𝐧𝐞𝐫](https://t.me/{OWNER_USERNAME})||</b>
"""

async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True

async def get_served_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list

async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})

async def get_served_chats() -> list:
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list

async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})

CHATBOT_READ = f"""
<u>**{BOT_NAME} 𝐂𝐦𝐝𝐬**</u>
** 𝐔𝐬𝐞 `/chatbot` 𝐓𝐨 enable/disable ❗ 𝐓𝐡𝐢𝐬 𝐂𝐦𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩 𝐒𝐨 𝐃𝐨𝐧'𝐭 𝐔𝐬𝐞 𝐎𝐧 𝐏𝐦 ❌.**
**───────────────**
[𝐎𝐰𝐧𝐞𝐫](https://t.me/{OWNER_USERNAME})
"""
CHATBOT_BACK = [
        [     
              InlineKeyboardButton(text="⬅️ 𝐁𝐚𝐜𝐤 ⬅️", callback_data="CHATBOT_BACK"),
              InlineKeyboardButton(text="❌️ 𝐂𝐥𝐨𝐬𝐞 ❌️", callback_data="CLOSE"),
        ],
]
HELP_START = [
     [
            InlineKeyboardButton(text="💖 𝐇𝐞𝐥𝐩 💖", callback_data="HELP"),
            InlineKeyboardButton(text="❌️ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="CLOSE"),
     ],
]

HELP_BUTN = [
     [
           InlineKeyboardButton(text="💥 𝐇𝐞𝐥𝐩 💥", url=f"https://t.me/{BOT_USERNAME}?start=help"),
           InlineKeyboardButton(text="❌️ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="CLOSE"),
     ],
]

ABOUT_BTN = [
      [
           InlineKeyboardButton(text="🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/{SUPPORT_GRP}"),  
           InlineKeyboardButton(text="🥀 𝐇𝐞𝐥𝐩 🥀", callback_data="HELP"),
      ],
      [    
           InlineKeyboardButton(text="🥀 𝐂𝐫𝐞𝐚𝐭𝐨𝐫💖", url=f"https://t.me/{OWNER_USERNAME}"), 
           InlineKeyboardButton(text="💥 𝐑𝐞𝐩𝐨 💥️", callback_data="SOURCE"),
      ],
      [ 
           InlineKeyboardButton(text="🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/{UPDATE_CHNL}"),  
           InlineKeyboardButton(text="⬅️ 𝐁𝐚𝐜𝐤 ⬅️", callback_data="BACK"),
      ],
]
SOURCE_READ = f"**🥀 𝐇𝐞𝐲, [{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝐑𝐞𝐩𝐨 𝐈𝐬 𝐇𝐞𝐫𝐞 💖.**\n**𝐆𝐢𝐯𝐞𝐧 𝐒𝐭𝐚𝐫 & 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐑𝐞𝐩𝐨**\n**──────────────────**\n**[𝐑𝐞𝐩𝐨](https://github.com/BikashHalderNew/BikashChAtBot)**\n**──────────────────**\n𝐒𝐞𝐞 𝐎𝐮𝐫 𝐕𝐢𝐝𝐞𝐨 𝐓𝐮𝐭𝐨𝐫𝐢𝐚𝐥 𝐇𝐨𝐰 𝐓𝐨 𝐌𝐚𝐤𝐞 𝐎𝐰𝐧 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐒𝐞𝐞 𝐕𝐢𝐝𝐞𝐨](https://youtu.be/GwkCcRXM4d8) \n**──────────────────**\n**𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧 & 𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐡𝐞𝐧 𝐉𝐨𝐢𝐧 [𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐏](https://t.me/{SUPPORT_GRP}).\n🥀 [𝐎𝐰𝐧𝐞𝐫](https://t.me/{OWNER_USERNAME})"

ABOUT_READ = f"""
** [{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝐈𝐬 𝐀𝐧 𝐀𝐢 𝐁𝐚𝐬𝐞𝐝 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 𝐅𝐫𝐨𝐦 𝐈𝐧𝐝𝐢𝐚 𝐒𝐭𝐚𝐭𝐞 𝐖𝐞𝐬𝐭 𝐁𝐞𝐧𝐠𝐚𝐥**
**──────────────**
𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 ❗

[𝐒𝐞𝐞 𝐇𝐨𝐰 𝐓𝐨 𝐌𝐚𝐤𝐞 𝐀 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 𝐋𝐢𝐤𝐞 𝐌𝐞](https://youtu.be/GwkCcRXM4d8)

[𝐉𝐨𝐢𝐧 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥](https://t.me/{UPDATE_CHNL})
[𝐉𝐨𝐢𝐧 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩](https://t.me/{SUPPORT_GRP})
"""
@bot.on_message(filters.command(["start", "bgtai", "aistart", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        accha = await m.reply_text(
            text = random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("🇮🇳 𝐕 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🥀🥀 𝐈𝐬 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠...💖")
        await asyncio.sleep(0.2)
        await accha.edit(" 𝐕 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 𝐈𝐬 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠...")
        await asyncio.sleep(0.2)
        await accha.edit("𝐕 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 𝐈𝐬 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠...")
        await asyncio.sleep(0.2)
        await accha.delete()
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo = random.choice(PHOTO),
            caption=f"""🥀 𝐇𝐞𝐲,  𝐈'𝐦 𝐀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🌷.\n\n📌 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 [{BOT_NAME}](t.me/{BOT_USERNAME}) 🌷 𝐅𝐨𝐫𝐦 𝐈𝐧𝐝𝐢𝐚 🇮🇳 \n\n🌷 𝐈'𝐦 𝐀 𝐀𝐫𝐭𝐢𝐟𝐢𝐜𝐢𝐚𝐥 𝐈𝐧𝐭𝐞𝐥𝐥𝐢𝐠𝐞𝐧𝐜𝐞 🌷\n\n➡️ 𝐔𝐬𝐚𝐠𝐞 : /chatbot - [on|off] 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐔𝐬𝐞 𝐎𝐧𝐥𝐲 𝐀𝐧𝐲 𝐆𝐫𝐨𝐮𝐩\n**──────────────**\n🥀 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐇𝐞𝐥𝐩 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩 💖!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GRP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHNL}) 🌷""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(PHOTO),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)

@bot.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    bikashdb = MongoClient(MONGO_URL)
    bikash = bikashdb["BikashDb"]["Bikash"]
    if query.data == "HELP":
        await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup=InlineKeyboardMarkup(HELP_BTN),
                      disable_web_page_preview=True,
     )
    elif query.data == "CLOSE":
            await query.message.delete()
    elif query.data == "BACK":
            await query.message.edit(
                  text = START,
                  reply_markup=InlineKeyboardMarkup(DEV_OP),
     )
    elif query.data == "SOURCE":
            await query.message.edit(
                   text = SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,

     )
    elif query.data == "ABOUT":
            await query.message.edit(
                    text = ABOUT_READ,
                    reply_markup = InlineKeyboardMarkup(ABOUT_BTN),
                    disable_web_page_preview=True,
     )
    elif query.data == "ADMINS":
            await query.message.edit(
                    text = ADMIN_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data== "TOOLS_DATA":
            await query.message.edit(
                    text= TOOLS_DATA_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK),
     )
    elif query.data == "BACK_HELP":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN),
     )
    elif query.data == "CHATBOT_CMD":
            await query.message.edit(
                    text = CHATBOT_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK), 
     )
    elif query.data == "CHATBOT_BACK":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN), 
     )
    elif query.data == "addchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "You don't have permissions to do this .",
                show_alert=True,
            )
        else:
            is_bikash = bikash.find_one({"chat_id": query.message.chat.id})
            if not is_bikash:           
                await query.edit_message_text(f"**💥 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐄𝐧𝐚𝐛𝐥𝐞𝐝🌷!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GRP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATE_CHNL}) 🌷**")
            if is_bikash:
                bikash.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**💥 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 𝐁𝐲 :** {query.from_user.mention}!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GRP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATE_CHNL}) 🌷**")
    elif query.data == "rmchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "**You don't have permissions to do this!**",
                show_alert=True,
            )
        else:
            is_bikash = bikash.find_one({"chat_id": query.message.chat.id})
            if not is_bikash:
                bikash.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**💥 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐃𝐢𝐬𝐚𝐛𝐥𝐞 𝐁𝐲 :** {query.from_user.mention}!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GRP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATE_CHNL}) 🌷.")
            if is_bikash:
                await query.edit_message_text("**💥 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝**\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GRP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATE_CHNL}) 🌷")
                            
@bot.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(
       text=SOURCE_READ,
       reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
       disable_web_page_preview=True,
    )

@bot.on_message(filters.command("donate") & filters.private & ~filters.edited)
async def donate_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 & 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐢𝐤𝐚𝐬𝐡 𝐨𝐫 𝐀𝐝𝐢𝐭𝐲𝐚 𝐅𝐨𝐫 𝐐𝐫 𝐂𝐨𝐝𝐞, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤 𝐓𝐡𝐞𝐧 [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/BgtPromote) & 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 [𝐘𝐨𝐮𝐭𝐮𝐛𝐞](https://youtube.com/@bikashgadgetstech)..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐁𝐢𝐤𝐚𝐬𝐡 🥀", url=f"https://t.me/BikashHalder")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝐀𝐝𝐢𝐭𝐲𝐚 🥀", url=f"https://t.me/AdityaHalder")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/Bgt_Chat"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/BikashGadgetsTech")
                ]
            ]
        ),
    )
       

@bot.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        hmm = await m.reply_photo(
            photo=random.choice(PHOTO),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(PHOTO),
            caption="**🥀 𝐇𝐞𝐲 , 𝐏𝐦 𝐌𝐞 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐇𝐞𝐥𝐩 𝐨𝐫 𝐂𝐦𝐝𝐬 ❗**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@bot.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def get_st(_, msg: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await msg.reply_photo(
        photo="https://graph.org/file/5ad0b22a90b34a94256a7.png",
        caption=f"📊 𝐒𝐭𝐚𝐭𝐬 𝐎𝐟 {BOT_NAME}\n\n➻ **🥀 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐚𝐭𝐬 :** {chats}\n🥀 **𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬 :** {users}",
    )

@bot.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(client, message: Message):
    if message.chat.type == "private":
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
    await message.delete()
    start = datetime.now()
    wtfbhemchomd = await message.reply_sticker(sticker= random.choice(STICKER))
    ms = (datetime.now()-start).microseconds / 1000
    await message.reply_photo(
        photo=random.choice(PHOTO),
        caption=f"🥀 𝐇𝐞𝐲, 𝐔𝐬𝐞𝐫\n**[{BOT_NAME}](t.me/{BOT_USERNAME})** 𝐈𝐬 𝐀𝐥𝐢𝐯𝐞 🥀 𝐌𝐲 𝐏𝐢𝐧𝐠\n➥ `{ms}` ms\n\n<b>|| 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 [𝐁𝐢𝐤𝐚𝐬𝐡](https://t.me/{OWNER_USERNAME})||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )

                  
@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"])
    & ~filters.private)
async def chatonoff(client: Client, message: Message):
    if not message.from_user:
        return
    else:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (await is_admins(chat_id)):
            return await message.reply_text(
                "**YOU ARE'NT AN ADMIN.**"
            )
        else:
            await message.reply_text(
            text="» <u>**🥀 𝐂𝐡𝐨𝐨𝐬𝐞 𝐀𝐧 𝐎𝐩𝐭𝐢𝐨𝐧 𝐓𝐨 enable/disable 𝐀𝐢 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭.**</u>",
            reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
        )


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def bikashai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       bikashdb = MongoClient(MONGO_URL)
       bikash = bikashdb["BikashDb"]["Bikash"] 
       is_bikash = bikash.find_one({"chat_id": message.chat.id})
       if not is_bikash:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       bikashdb = MongoClient(MONGO_URL)
       bikash = bikashdb["BikashDb"]["Bikash"] 
       is_bikash = bikash.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_bikash:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def bikashstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       bikashdb = MongoClient(MONGO_URL)
       bikash = bikashdb["BikashDb"]["Bikash"] 
       is_bikash = bikash.find_one({"chat_id": message.chat.id})
       if not is_bikash:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       bikashdb = MongoClient(MONGO_URL)
       bikash = bikashdb["BikashDb"]["Bikash"] 
       is_bikash = bikash.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_bikash:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def bikashprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def bikashprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")

print(f"{BOT_NAME} 𝐈𝐬 𝐀𝐥𝐢𝐯𝐞 ! 𝐍𝐨𝐰 𝐉𝐨𝐢𝐧 @BikashGadgetsTech & @Bgt_Chat !!")      
bot.run()
