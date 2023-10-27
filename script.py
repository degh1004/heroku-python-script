import os

from telegram.client import Telegram
import settings

tg = Telegram(
    api_id=settings.API_ID,
    api_hash=settings.API_HASH,
    phone=settings.PHONE_NUMBER,
    database_encryption_key='changeme1234',
    # library_path='./libfile/libtdjson.dylib'
)

tg.login()


def new_message_handler(update):
    message_content = update['message']['content'].get('text', {})
    message_text = message_content.get('text', '').lower()
    is_outgoing = update['message']['is_outgoing']
    chat_id = update['message']['chat_id']
    li = message_text.lower().split(' ')
    contains_stake = any("stake" in string for string in li)
    print(update)
    print(chat_id)
    print(message_text)

    if not is_outgoing and chat_id == int(settings.CHAT_ID_BETS_CHANNEL) and contains_stake:
        tg.send_message(
            chat_id=int(settings.CHAT_ID_POPORO_CHANNEL),
            text=message_text,
        )

    if not is_outgoing and chat_id == int(settings.CHAT_ID_BOT_CHANNEL):
        tg.send_message(
            chat_id=int(settings.CHAT_ID_POPORO_CHANNEL),
            text=message_text,
        )


tg.add_message_handler(new_message_handler)
tg.idle()

