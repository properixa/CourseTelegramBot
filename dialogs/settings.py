from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Row, Cancel
from states.states import SettingsSG

async def difficulty_menu(callback, button, manager: DialogManager):
    await manager.switch_to(SettingsSG.difficulty)

async def theme_menu(callback, button, manager: DialogManager):
    await manager.switch_to(SettingsSG.category)

async def change_difficulty(callback, button, manager: DialogManager):
    print(button)

async def to_settings(callback, button, manager: DialogManager):
    await manager.switch_to(SettingsSG.main)


settings_window = Window(
    Const("Тут планируются настройки...."),
    Row(
        Button(Const("Сложность"), id='menu', on_click=difficulty_menu),
        Button(Const("Тема"), id="theme", on_click=theme_menu)
    ),
    Cancel(Const("⬅️ Назад")),
    state=SettingsSG.main
)

difficulty_choice = Window(
    Const("сложность пупупу"),
    Row(
        Button(Const("Легкая"), id='easy', on_click=change_difficulty),
        Button(Const("Средняя"), id='medium', on_click=change_difficulty),
        Button(Const("Тяжелая"), id='hard', on_click=change_difficulty)
    ),
    Button(Const("Назад к настройкам!"), id='back_to_settings', on_click=to_settings),
    state=SettingsSG.difficulty
)

theme_choice = Window(
    Const("Выбор темы"),
    Row(
        Button(Const("Тут кароче многа кнопок будет но пока нету"), id='mnoga_knopok')
    ),
    Button(Const("Назад к настройкам!"), id='back_to_settings', on_click=to_settings),
    state=SettingsSG.category
)