import logging

from pyrogram import types

from config import SEND_AS_CHAT_ID, MSG_TEXT
from loader import bot, log


# TARGET_CHAT_IDS = set()


# @api.after_connection
# async def on_startup():
#     async for dialog in bot.iter_dialogs():
#         chat = dialog.chat
#
#             try:
#                 res = await bot.set_send_as_chat(chat.id, SEND_AS_CHAT_ID)
#             except Exception as e:
#                 log.exception(e)
#             else:
#                 if res:
#                     TARGET_CHAT_IDS.add(chat.id)
#
#     log.warning(f'{TARGET_CHAT_IDS=}')


@bot.on_message()
async def send_comment(_, msg: types.Message):
    if msg.chat.type not in ["group", "supergroup"]:
        return

    if not msg.sender_chat:
        return

    log.warning(f'Send message to Chat(id={msg.chat.id}, title="{msg.chat.title}")')

    try:
        await bot.set_send_as_chat(msg.chat.id, SEND_AS_CHAT_ID)
        await msg.reply(MSG_TEXT)
    except Exception as e:
        log.exception(e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)

    bot.run()
