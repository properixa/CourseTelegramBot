from config_reader import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(Command("start"))
async def start_message(message: types.Message):
    await message.answer("Дашка куда подсматриваем")


async def main():
    print("Bot started!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
