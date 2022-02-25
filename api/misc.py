import asyncio

from loader import bot


def after_connection(func):
    async def wrapper(*args, **kwargs):
        while not bot.is_connected:
            await asyncio.sleep(1)

        await func(*args, **kwargs)

    return wrapper
