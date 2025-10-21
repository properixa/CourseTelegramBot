from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Column
from states.states import MainSG, GameSG, SettingsSG, InvoiceSG, ProfileSG

async def get_start_data(dialog_manager: DialogManager, **kwargs):
    user_id = dialog_manager.event.from_user.id
    return {
        'username': dialog_manager.event.from_user.first_name
    }

async def start_game(callback, button, manager: DialogManager):
    await manager.start(GameSG.question)

async def open_settings(callback, button, manager: DialogManager):
    await manager.start(SettingsSG.main)

async def open_profile(callback, button, manager: DialogManager):
    await manager.start(ProfileSG.main)

async def open_invoice(callback, button, manager: DialogManager):
    await manager.start(InvoiceSG.main)

start_window = Window(
    Const("🎮 Добро пожаловать в Викторину!"),
    Format(
        "Привет {username}!\n"
        "кол-во игр и всякая шелуха\n"
        "процент правильных ответов\n\n"
        "Выбери действие:"
    ),
    Column(
        Button(Const("🎯 Начать игру"), id='start_game', on_click=start_game),
        Button(Const("⚙️ Настройки"), id='settings', on_click=open_settings),
        Button(Const("👤 Профиль"), id="profile", on_click=open_profile),
        Button(Const("Поддержка разработчика"), id="invoice", on_click=open_invoice)
    ),
    state=MainSG.main,
    getter=get_start_data
)
