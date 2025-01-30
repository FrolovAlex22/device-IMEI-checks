import logging.config

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import Config, load_config
from config.logging_settings import logging_config
from handlers import (
    other_handlers,
    user_handlers,
)


config: Config = load_config()

logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

bot = Bot(
    token=config.tg_bot.token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

bot.white_list = config.tg_bot.admin_ids


async def on_startup(bot):
    logger.info("Начало работы бота")


async def main():
    dp.startup.register(on_startup)
    dp.include_router(user_handlers.user_router)
    dp.include_router(other_handlers.other_router)
    await dp.start_polling(bot)

asyncio.run(main())
