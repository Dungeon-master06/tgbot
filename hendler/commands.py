from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, LinkPreviewOptions
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(Command('start'))
async def satus(message: Message):
    await message.answer('Привет я бот по доставке еды, чем я могу вам помочь?')



@router.message(Command('help'))
async def help(message: Message):
    await message.reply('Чем я могу вам помочь?')

@router.message(Command('adress'))
async def adress(message: Message):
    await message.answer('Укажите адресс доставки')

@router.message(Command('contact'))
async def contact(message: Message):
    await message.reply('Укажите контакт: Номер телефона или email. Например: +7 999 999 99 99')

@router.message(F.text == 'Меню')
async def menu(message: Message):
    await message.answer('Меню отсутствует')

@router.message(F.text.lower() == 'категории')
async def categories(message: Message):
    await message.answer('Категории отсутствуют')

@router.message(Command('link'))
async def link(message: Message):
    link1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    link_preview_options = LinkPreviewOptions(is_disabled=True)
    await message.answer(link1, link_preview_options=link_preview_options)

@router.message(Command('link2'))
async def link2(message: Message):
    link2 = "https://www.youtube.com/watch?v=7hGU_pwEq5Q"
    link_preview_options2=LinkPreviewOptions(prefer_small_media=True)
    await message.answer(link2, link_preview_options=link_preview_options2)

@router.message(Command('link3'))
async def link3(message: Message):
    link3 = "https://www.youtube.com/watch?v=hcXDTvp6Xz4"
    link_preview_options3=LinkPreviewOptions(prefer_large_media=True)
    await message.answer(link3, link_preview_options=link_preview_options3)

@router.message(Command('link4'))
async def link4(message: Message):
    link4 = "https://www.youtube.com/watch?v=8JtFfExSCNw"
    link_preview_options4=LinkPreviewOptions(prefer_small_media=True,show_above_text=True)
    await message.answer(link4, link_preview_options=link_preview_options4)

@router.message(Command('link5'))
async def link5(message: Message):
    link5 = "https://t.me/qwertyugfdsadfffffffbot"
    link_preview_options = LinkPreviewOptions(is_disabled=True)
    await message.answer(link5, link_preview_options=link_preview_options)