from aiogram import Router,F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from database.querysets import *
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State


admin_router = Router()

class AddCategory(StatesGroup):
    name = State()

@admin_router.message(Command('add_category'))
async def add_category_admin(message: Message, state: FSMContext):
    await message.answer('Введите название категории')
    await state.set_state(AddCategory.name)

@admin_router.message(AddCategory.name)
async def add_category_name(message: Message, state: FSMContext):
    await add_category(message.text)
    await message.answer('Категория добавлена')
    await state.clear()
class AddFood(StatesGroup):
    name = State()
    img = State()
    description = State()
    price = State()
    gramm = State()
    component = State()
    category = State()






