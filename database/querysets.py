from .models import *

from sqlalchemy import select,delete,update

async def get_categories():
    async with async_session() as session:
        result = await session.scalars(select(Categoryfoods))
        return result
    
async def get_foods():
    async with async_session() as session:
        result = await session.scalars(select(Foods))
        return result


async def get_foods_by_category(category_id):
    async with async_session() as session:
        result = await session.scalars(select(Foods).where(
            Foods.category_id == category_id))
        return result


async def get_food_by_id(food_id):
    async with async_session() as session:
        result = await session.scalar(select(Foods).where(
            Foods.id == food_id))
        return result

async def add_category(text):
    async with async_session() as session:
        category = Categoryfoods(name = text)
        session.add(category)
        await session.commit()
        await session.refresh(category)
        return category
    
async def add_food_db(data):
    async with async_session() as session:
        session.add(data)
        await session.commit()
        await session.refresh(data)
        return data

async def delete_food_db(data):
    async with async_session() as session:
        await session.execute(delete(Foods).where(Foods.id == data.id))
        await session.commit()
        return data