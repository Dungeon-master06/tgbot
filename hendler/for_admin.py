from aiogram import Router,F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from database.querysets import *
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from hendler.keyboards import *


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
    size = State()
    component = State()
    category = State()



@admin_router.message(Command('add_food'))
async def add_food_admin(message: Message, state: FSMContext):
    await message.answer('Введите название еды')
    await state.set_state(AddFood.name)

@admin_router.message(AddFood.name)
async def add_food_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer('Введите описание')
    await state.set_state(AddFood.description)

@admin_router.message(AddFood.description)
async def add_food_description(message: Message, state: FSMContext):
    await state.update_data(description = message.text)
    await message.answer('Введите цену')
    await state.set_state(AddFood.price)

@admin_router.message(AddFood.price)
async def add_food_price(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Цена должна быть цифрой')
        return add_food_price
    await state.update_data(price = int(message.text))
    await message.answer('Введите граммы')
    await state.set_state(AddFood.gramm)

@admin_router.message(AddFood.gramm)
async def add_food_gramm(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Граммы должны быть цифрой')
        return add_food_gramm
    await state.update_data(gramm = message.text)
    await message.answer('Введите размер')
    await state.set_state(AddFood.size)

@admin_router.message(AddFood.size)
async def add_food_size(message: Message, state: FSMContext):
    await state.update_data(size = message.text)
    await message.answer('Введите состав')
    await state.set_state(AddFood.component)

@admin_router.message(AddFood.component)
async def add_food_component(message: Message, state: FSMContext):
    await state.update_data(component = message.text)
    await message.answer('Выберите фотографию')
    await state.set_state(AddFood.img)

@admin_router.message(AddFood.img)
async def add_food_img(message: Message, state: FSMContext):
    await state.update_data(img = message.photo[0].file_id)
    await message.answer('Выберите категорию', reply_markup= await get_categories_kb2())
    await state.set_state(AddFood.category)

@admin_router.callback_query(AddFood.category)
async def add_food_category(callback: CallbackQuery, state: FSMContext):
    await state.update_data(category = callback.data.split('_')[1])
    data =await state.get_data()
    food = Foods(
        name = data['name'],
        img = data['img'],
        description = data['description'],
        price = data['price'],
        gramm = data['gramm'],
        size = data['size'],
        component = data['component'],
        category_id = data['category']
    )
    await add_food_db(food)
    await callback.answer('Еда добавлена')
    await state.clear()
    
@admin_router.message(Command('delete_food'))
async def delete_food(message: Message):
    await message.answer('Выберите блюдо для удаления:', reply_markup= await get_foods_kb2())

@admin_router.callback_query(F.data.startswith('food2_'))
async def delete_food_callback(callback: CallbackQuery):
    food_id = callback.data.split('_')[1]
    await callback.message.answer(f"Вы действительно хотите удалить это блюдо?", reply_markup= await yes_no_kb(food_id))

@admin_router.callback_query(F.data.startswith('yes_'))
async def delete_food_callback(callback: CallbackQuery):
    food_id = callback.data.split('_')[1]
    await delete_food_db(food_id)
    await callback.message.answer('Блюдо удалено')

@admin_router.callback_query(F.data.startswith('no'))
async def delete_food_callback(callback: CallbackQuery):
    await callback.message.delete()

@admin_router.message(Command('delete_category'))
async def delete_category(message: Message):
    await message.answer('Выберите категорию для удаления:', reply_markup= await get_categories_kb2())

@admin_router.callback_query(F.data.startswith('category2_'))
async def delete_category_callback(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'Вы действительно хотите удалить эту категорию?', reply_markup= await yes_no_kb2(category_id))

@admin_router.callback_query(F.data.startswith('yes2_'))
async def delete_category_callback(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await delete_category_db(category_id)
    await callback.message.answer('Категория удалена')

@admin_router.callback_query(F.data.startswith('no2'))
async def delete_food_callback(callback: CallbackQuery):
    await callback.message.delete()

