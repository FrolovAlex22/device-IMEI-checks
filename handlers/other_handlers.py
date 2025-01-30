import logging

from aiogram import F, Router
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove, Contact

from lexicon.lexicon import LEXICON_OTHER


other_router = Router()

logger = logging.getLogger(__name__)




@other_router.message(CommandStart())
async def start_cmd_other(message: Message):
    """Сообщение в случае команды /start"""
    logger.info(
        f"неавторризованный пользователь {message.from_user.id} запустил бота"
    )

    await message.answer(
        f"{message.from_user.first_name} {LEXICON_OTHER["not_authorized"]}",
        reply_markup=None
    )