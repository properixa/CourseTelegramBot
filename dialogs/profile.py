from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Cancel, Button, Column

from database.database import Database
from states.states import ProfileSG
#todo: Доделать профиль
async def get_profile_data(dialog_manager: DialogManager, **kwargs):
    user_id = dialog_manager.event.from_user.id
    db : Database = dialog_manager.middleware_data.get('db')
    stats = await db.get_stats(user_id)
    wins = stats['wins']
    games = stats['games']
    return {
        'wins': wins,
        'games': games
    }

async def reset_user_stats(callback, button, manager: DialogManager):
    user_id = manager.event.from_user.id
    db : Database = manager.middleware_data.get("db")
    await db.reset_stats(user_id)
    await manager.show()

profile_window = Window(
    Const("Ваш профиль"),
    Format("Процент правильных ответов: {wins}\nКоличество игр: {games}"),    
    Column(
        Button(Const("Сбросить статистику"), id='reset_stats', on_click=reset_user_stats),
        Cancel(Const("⬅️ Назад"))
    ),
    
    state=ProfileSG.main,
    getter=get_profile_data
)
