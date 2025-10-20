import asyncio
from config_reader import config
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import Dialog, Window, DialogManager, setup_dialogs
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram.fsm.state import State, StatesGroup

class MainSG(StatesGroup):
    main = State()
    settings = State()

async def start_cmd(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.main)

async def on_click_menu(callback, button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(MainSG.main)

async def on_click_settings(callback, button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(MainSG.settings)

main_dialog = Dialog(
    Window(
        Const("ебучие попытки"),
        Button(Const("А вот куку туту пупу"), id="settings", on_click=on_click_settings),
        state=MainSG.main
    ),
    Window(
        Const("Куку туту пупу"),
        Button(Const("в пизду я дальше пытатся"),  id="menu", on_click=on_click_menu),
        state=MainSG.settings
    )
)

async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    dp.message.register(start_cmd, Command("start"))
    dp.include_router(main_dialog)
    setup_dialogs(dp)
    
    await dp.start_polling(bot)

asyncio.run(main())