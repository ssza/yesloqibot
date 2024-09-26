import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from config import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message()
async def cmd_start(message: types.Message):
    if message.text.lower() == "да" or message.text.lower() == "lf" or message.text.lower() == "da":
        await message.reply_video(video="https://aa60668e-c7f5-41af-bfc3-ac01d5c9a76f.selstorage.ru/yesloqibot.mp4")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
