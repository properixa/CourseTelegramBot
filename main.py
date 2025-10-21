import asyncio
from services.config_reader import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from dialogs import start_dialog, settings_dialog
from handlers.common import router as common_router


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    dp.include_router(common_router)

    dp.include_router(start_dialog)
    dp.include_router(settings_dialog)
    
    setup_dialogs(dp)
    
    await dp.start_polling(bot)

asyncio.run(main())