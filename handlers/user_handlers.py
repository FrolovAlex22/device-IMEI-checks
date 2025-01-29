import logging

from aiogram import F, Router
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove, Contact

from lexicon.lexicon import LEXICON_USER


user_router = Router()

logger = logging.getLogger(__name__)


@user_router.message(CommandStart(), StateFilter("*"))
async def start_cmd(message: Message):
    """Сообщение в случае команды /start"""
    logger.info(f"Пользователь {message.from_user.id} запустил бота")

    await message.answer(
        f"{message.from_user.first_name} {LEXICON_USER["start_button"]}",
        reply_markup=None
    )
