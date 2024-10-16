from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.querysets import *

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Menu')],
    [KeyboardButton(text='Category')],
    ],resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Выберите пункт")


async def get_categorys_kb():
    categorys = await get_categorys()
    builder = InlineKeyboardBuilder()
    for category in categorys:
        builder.add(InlineKeyboardButton(text=category.name,callback_data=f'category_{category.id}'))
    return builder.adjust(2).as_markup()


async def get_foods_kb():
    foods = await get_foods_by_category()
    builder = InlineKeyboardBuilder()
    for food in foods:
        builder.add(InlineKeyboardButton(text=food.name,callback_data=f'food_{food.id}'))
    return builder.adjust(2).as_markup()



# Category_kb = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='супы')],
#     [KeyboardButton(text='салаты')],
#     [KeyboardButton(text='десерты')],
#     [KeyboardButton(text='закуски')],
#     [KeyboardButton(text='напитки')]
#     ],resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Выберите пункт в категории")

# menu_lnline = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Add',callback_data='add'),
#     InlineKeyboardButton(text='Delete',callback_data='delete')],
# ])


# menu_kb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Чечевица',callback_data='чечевица')],
#     [InlineKeyboardButton(text='Цезарь',callback_data='цезарь')],
#     [InlineKeyboardButton(text='Дубайский шокалад',callback_data='дубайский шокалад')],
#     [InlineKeyboardButton(text='Хамон',callback_data='хамон')],
#     [InlineKeyboardButton(text='Кроснадарский напиток',callback_data='кроснадарский напиток')],
# ])

# async def get_inline_keyboard():
#     builder = InlineKeyboardBuilder()
#     list1 =['hello','key','jhn','vi', 'world','msi','bot','top','jungle','item']
#     for n in range(0,len(list1)):
#         builder.add(InlineKeyboardButton(text=list1[n], callback_data=f'{list1[n]}'))
#     return builder.adjust(3).as_markup()

                    
