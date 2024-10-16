from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton


kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Menu')],
    [KeyboardButton(text='Category')],
    ],resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Выберите пункт")

Category_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='супы')],
    [KeyboardButton(text='салаты')],
    [KeyboardButton(text='десерты')],
    [KeyboardButton(text='закуски')],
    [KeyboardButton(text='напитки')]
    ],resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Выберите пункт в категории")

menu_lnline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Add',callback_data='add'),
    InlineKeyboardButton(text='Delete',callback_data='delete')],
])


menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Чечевица',callback_data='чечевица')],
    [InlineKeyboardButton(text='Цезарь',callback_data='цезарь')],
    [InlineKeyboardButton(text='Дубайский шокалад',callback_data='дубайский шокалад')],
    [InlineKeyboardButton(text='Хамон',callback_data='хамон')],
    [InlineKeyboardButton(text='Кроснадарский напиток',callback_data='кроснадарский напиток')],
])


