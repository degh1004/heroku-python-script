import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
CHAT_ID_BETS_CHANNEL = os.getenv('CHAT_ID_BETS_CHANNEL')
CHAT_ID_BOT_CHANNEL = os.getenv('CHAT_ID_BOT_CHANNEL')
CHAT_ID_POPORO_CHANNEL = os.getenv('CHAT_ID_POPORO_CHANNEL')

