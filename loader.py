import logging

from pyrogram import Client

import config

bot = Client('sessions/1', config.Api.ID, config.Api.HASH)

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.addHandler(logging.FileHandler('.log', 'w'))
