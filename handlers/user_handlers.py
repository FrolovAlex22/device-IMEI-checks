import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from filters.users_whitelist import IsWhitelist
from lexicon.lexicon import LEXICON_USER
from utils.request_api import check_imei_and_return_info


user_router = Router()
user_router.message.filter(IsWhitelist())

logger = logging.getLogger(__name__)


@user_router.message(CommandStart())
async def start_cmd(message: Message):
    """Сообщение в случае команды /start"""
    logger.info(f"Пользователь {message.from_user.id} запустил бота")

    await message.answer(
        LEXICON_USER["start_button"],
        reply_markup=None
    )


@user_router.message(F.text)
async def processing_imei(message: Message):
    """Обработка IMEI, возвращение информации о нем"""
    logger.info(f"Пользователь {message.from_user.id} написал {message.text}")
    if not message.text.isdigit() or not len(message.text) == 15:
        await message.answer(LEXICON_USER["wrong_imei"], reply_markup=None)
        return
    imei = int(message.text)
    try:
        imei_text = await check_imei_and_return_info(imei)
        text = f"{LEXICON_USER["imei_info"]}{imei_text}"
        await message.answer(text, reply_markup=None)
        await message.answer(LEXICON_USER["second_imei"], reply_markup=None)
        logger.info(f"Пользователь проверил IMEI: {imei}")
    except Exception as e:
        logger.error(e)


@user_router.message(~F.text)
async def wrong_message(message: Message):
    """Ответ на неправильное сообщение"""
    logger.info("Пользователь прислал не текст")
    await message.answer(
        LEXICON_USER["wrong_message"],
        reply_markup=None
    )
