import asyncio
import logging

from pyrogram import types

import api
from config import SEND_AS_CHAT_ID
from loader import bot, log

TARGET_CHAT_IDS = set()


@api.after_connection
async def on_startup():
    async for dialog in bot.iter_dialogs():
        chat = dialog.chat

        if chat.type in ["group", "supergroup"]:
            try:
                res = await bot.set_send_as_chat(chat.id, SEND_AS_CHAT_ID)
            except Exception as e:
                log.exception(e)
            else:
                if res:
                    TARGET_CHAT_IDS.add(chat.id)

    log.warning(f'{TARGET_CHAT_IDS=}')


@bot.on_message()
async def send_comment(_, msg: types.Message):
    if msg.forward_from_chat:
        if msg.chat.id in TARGET_CHAT_IDS:
            log.warning(f'send message to Chat(id={msg.chat.id}, title="{msg.chat.title}")')

            try:
                await msg.reply('ХУЙ ВОЙНЕ')
            except Exception as e:
                log.exception(e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING, filename='.log')

    loop = asyncio.get_event_loop()
    loop.create_task(on_startup())
    bot.run()
