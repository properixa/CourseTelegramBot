from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Row, Cancel, Group, ScrollingGroup
from states.states import SettingsSG

from asyncio import sleep

from database.database import Database

CATEGORIES = [
    'All', 'Linux', 'DevOps', 'Networking', 'Programming', 'Cloud', 'Docker', 'Kubernetes'
]

async def get_output_data(dialog_manager: DialogManager, **kwargs):
    difficulties = {
        'easy': "Легкая",
        'medium': 'Средняя',
        'hard': 'Тяжелая'
    }

    user_id = dialog_manager.event.from_user.id
    db = dialog_manager.middleware_data.get("db")
    difficulty = await db.get_difficulty(user_id)
    category = await db.get_category(user_id)

    return {
        'category': "Все" if category['theme'] == "all" else category['theme'],
        'difficulty': difficulties.get(difficulty['difficulty'])
    }

async def get_categories_data(dialog_manager: DialogManager, **kwargs):
    return {
        "categories": CATEGORIES,
    }

async def difficulty_menu(callback, button, manager: DialogManager):
    await manager.switch_to(SettingsSG.difficulty)

async def theme_menu(callback, button, manager: DialogManager):
    await manager.switch_to(SettingsSG.category)

async def change_difficulty(callback, button, manager: DialogManager):
    button_id = button.widget_id
    user_id = manager.event.from_user.id
    db : Database = manager.middleware_data.get("db")
    await db.change_difficulty(user_id, button_id)

    await manager.switch_to(SettingsSG.main)

async def change_category(callback, button: Button, manager: DialogManager):
    user_id = manager.event.from_user.id
    db : Database = manager.middleware_data.get("db")
    category = int(button.widget_id.split('_')[1])
    await db.change_category(user_id, CATEGORIES[category])

    await manager.switch_to(SettingsSG.main)

async def to_settings(callback, button, manager: DialogManager):
    await manager.switch_to(SettingsSG.main)

settings_window = Window(
    Const("Ваши настройки:\n"),
    Format("Выбранная категория:\n{category}\n\nВыбранная сложность:\n{difficulty}\n\n"),
    Const("Что вы хотите изменить?"),
    Row(
        Button(Const("Сложность"), id='menu', on_click=difficulty_menu),
        Button(Const("Тема"), id="theme", on_click=theme_menu)
    ),
    Cancel(Const("⬅️ Назад")),
    state=SettingsSG.main,
    getter=get_output_data
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
    Const("Выберите категорию:"),
    Group(
    ScrollingGroup(
        *[Button(Const(item), id=f"cat_{i}", on_click=change_category) 
          for i, item in enumerate(CATEGORIES)],
        id="categories_scroll",
        width=2,
        height=4,
        hide_pager=True,
    ),
    Group(
        Row(
            Button(Const("⬅️"), id="prev_page"),
            Button(Const("➡️"), id="next_page"),
        ),
        id="nav_buttons",
    ),
    id="main_group"),
    Button(Const("Назад к настройкам!"), id='back_to_settings', on_click=to_settings),
    state=SettingsSG.category,
    getter=get_categories_data
)