import os
from typing import List

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "1255023013"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/7NX2TY1N/photo-2025-07-13-12-32-15-7531449578462117904.jpg https://i.ibb.co/3mSrtgDw/photo-2025-07-14-08-03-12-7526845489484922908.jpg https://i.ibb.co/8nNgvwyn/photo-2025-07-14-08-02-56-7526846752205307932.jpg https://i.ibb.co/bgH9CXnx/photo-2024-11-07-03-36-42-7531449810390351892.jpg https://i.ibb.co/s9gt09Vq/photo-2025-07-14-08-00-51-7531450025138716692.jpg https://i.ibb.co/8g1fH31T/cutie.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002686843200"))

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "store")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-100******** -100*********").split())) # Add Multiple channel ids

EMOJIS = [
    "👍", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "😢",
    "🎉", "🤩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🤷‍♂️",
    "❤️‍🔥", "🌚", "💯", "🤣", "⚡", "🏆", "🗿", "😐", "🤨", "🍾",
    "💋", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🙈", "🤷‍♀️",
    "😇", "🤝", "✍️", "🤗", "🫡", "😨", "🧑‍🎄", "🎄", "⛄", "🤪",
    "🆒", "💘", "🙊", "🦄", "😘", "🙉", "💊", "😎", "👾", "🤷"
]