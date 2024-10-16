from unicodedata import category
from .models import *

from sqlalchemy import select,delete,update

async def get_categorys():
    async with async_session() as session:
        result =await session.scalars(select(Categoryfoods))
        return result
    

async def get_foods_by_category():                    
    async with async_session() as session:
        result =await session.scalars(select(Foods).where(Foods.category_id == 1))
        return result.all()
    
