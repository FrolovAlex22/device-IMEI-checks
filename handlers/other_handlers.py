import logging

from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_OTHER


other_router = Router()

logger = logging.getLogger(__name__)


@other_router.message()
async def start_cmd_other(message: Message):
    """Сообщение в случае команды /start"""
    logger.info(
        f"неавторризованный пользователь {message.from_user.id} запустил бота"
    )

    await message.answer(
        f"{message.from_user.first_name} {LEXICON_OTHER["not_authorized"]}",
        reply_markup=None
    )
