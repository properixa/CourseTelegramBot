from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Cancel

from states.states import ProfileSG
#todo: Доделать профиль
async def get_profile_data(**kwargs):
    return {
        'winrate': 50,
        'games': 100
    }

profile_window = Window(
    Const("Ваш профиль"),
    Format("Процент правильных ответов: {winrate}\nКоличество игр: {games}"),    
    Cancel(Const("⬅️ Назад")),
    state=ProfileSG.main,
    getter=get_profile_data
)
