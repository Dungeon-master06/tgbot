import asyncio
from database.models import *
import sys , logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from hendler.commands import router

async def main():
    # await crate_tables()
    # await add_category()
    # await add_foods()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())    