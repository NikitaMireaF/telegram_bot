import asyncio
import aiogram
import logging
from aiogram import Bot
from config import TOKEN
import handlers
from aiogram.types import BotCommand, BotCommandScopeDefault

bot = aiogram.Bot(token=TOKEN)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start', description='Начало работы'
        ),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    logging.basicConfig(level=logging.INFO)
    dp = aiogram.Dispatcher()
    dp.include_routers(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())