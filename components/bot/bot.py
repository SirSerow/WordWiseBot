import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

logging.basicConfig(level=logging.INFO)

TOKEN_FILE = "/run/secrets/token.txt"
with open(TOKEN_FILE, "r") as file:
    token = file.read().strip()

bot = Bot(token)

dp = Dispatcher()


@dp.message()
async def start(message: types.Message):
    webAppInfo = types.WebAppInfo(
        url="https://translate.google.com/")
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(
        text='Launch app', web_app=webAppInfo))

    await message.answer(text='App launched', reply_markup=builder.as_markup())


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
