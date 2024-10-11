from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,String,Integer,DateTime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs,async_sessionmaker

from config import MYSQL_URL

engine = create_async_engine(MYSQL_URL, echo=True)
async_session = async_sessionmaker(engine)

class Base(DeclarativeBase,AsyncAttrs):
    pass

class Categoryfoods(Base):
    __tablename__ = 'category_foods'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    foods= relationship('Foods',back_populates="category")

class Foods(Base):
    __tablename__ = 'foods'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    img: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    size: Mapped[int] = mapped_column(Integer,nullable=True) 
    price: Mapped[int] = mapped_column(Integer)
    gramm: Mapped[int] = mapped_column(Integer)
    component: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[int] = mapped_column(ForeignKey('category_foods.id'))
    category= relationship('Categoryfoods',back_populates="foods")

async def crate_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def add_category():
    async with async_session() as session:
        category = Categoryfoods(name =  "Салаты")

        session.add(category)
        await session.commit()
        await session.refresh(category)
        return category
    
async def add_foods():
    async with async_session() as session:
        foods = Foods(name = 'Цезарь',img = 'imgae/zesar.jpeg',description = 'Цезарь(не Гай Юлий)',price = 300,gramm = 50,component = 'салат, курица, помидоры черри,соус цезарь, пармезан, сухарики',category_id = 4)

        session.add(foods)
        await session.commit()
        await session.refresh(foods)
        return foods
    