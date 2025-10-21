import asyncio
from services.config_reader import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from dialogs import game_dialog, invoice_dialog, profile_dialog, settings_dialog, start_dialog
from handlers.common import router as common_router
from handlers.error import router as error_router


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    dp.include_router(error_router)
    dp.include_router(common_router)

    dp.include_router(start_dialog)
    dp.include_router(settings_dialog)
    dp.include_router(game_dialog)
    dp.include_router(invoice_dialog)
    dp.include_router(profile_dialog)
    
    setup_dialogs(dp)
    print("Роутеры подключены!")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
