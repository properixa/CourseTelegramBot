from aiogram import Router
from aiogram.types import ErrorEvent
from aiogram_dialog.api.exceptions import UnknownIntent
from aiogram_dialog import DialogManager

router = Router()

@router.errors()
async def handle_unknown_intent(error: ErrorEvent, dialog_manager: DialogManager):
    if not isinstance(error.exception, UnknownIntent):
        return False
        
    callback = getattr(error.update, 'callback_query', None)
    if not callback:
        return True
        
    try:
        await callback.answer("Сессия устарела!! Пропишите /start", show_alert=True)
        
        
        
    except Exception as e:
        print(f"Ошибка в обработчике UnknownIntent: {e}")
        
    return True 