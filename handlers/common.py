from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram_dialog import DialogManager, StartMode

from states.states import MainSG
from database.database import Database

router = Router()


@router.message(Command("start"))
async def start_cmd(message: Message, dialog_manager: DialogManager, db: Database):
    is_created = await db.get_user(message.from_user.id)
    if (is_created):
        await dialog_manager.start(MainSG.main, mode=StartMode.RESET_STACK)
    else:
        await db.create_user(message.from_user.id)
        await dialog_manager.start(MainSG.first_time, mode=StartMode.RESET_STACK)

@router.message(Command("menu"))
async def menu_cmd(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.main, mode=StartMode.RESET_STACK)

