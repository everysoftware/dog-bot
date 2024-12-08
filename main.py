import asyncio

import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from config import config

# test comment...
bot = Bot(config.bot_token)
dp = Dispatcher()

async def get_dog() -> dict[str, str]:
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dog.ceo/api/breeds/image/random') as response:
            return await response.json()

@dp.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer("Привет! Я бот, который умеет отправлять фото собачек. Напиши /dog и получи фото! 🐶")

@dp.message(Command("dog"))
async def dog(message: types.Message) -> None:
    data = await get_dog()
    await message.answer_photo(data['message'])

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())