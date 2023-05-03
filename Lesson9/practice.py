from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton

from config import TOKEN_API
from keyboards import kb, ikb


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)




async def on_startup(_):
    print('Я был запущен')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text= "Добро пожаловать в ш=главное меню",
                         reply_markup=kb)

@dp.message_handler(commands=['links'])
async def links_command(message: types.Message):
    await message.answer(text='выберите опцию....',
                         reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)