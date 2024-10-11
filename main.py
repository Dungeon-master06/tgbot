import asyncio
from database.models import *
import sys , logging

async def main():
    # await crate_tables()
    await add_category()
    await add_foods()
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())    