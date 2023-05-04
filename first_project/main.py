from aiogram import Bot, Dispatcher, executor, types
from keyboards import kb
from config import TOKEN_API

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot = bot)
HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/Random_photo</b> - <em>отправка случайное фото</em>"""


async def on_startup(_):
    print("Я запустился")


@dp.message_handler(commands=['start'])
async def cmd_start (message: types.Message):
    await message.answer(text='Добро пожаловать в наш бот! 🐌 ',
                         reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def cmd_help (message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=['description'])
async def cmd_description (message: types.Message):
    await message.answer(text='Наш бот умеет отправлять рандомные фотки')
    await message.delete()

@dp.message_handler(commands=['Random_photo'])
async def cmd_photot (message: types.Message):
    await message.answer(text='Наш бот умеет отправлять рандомные фотки')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgIAAxkBAAEI1_xkUqSQEN8_C06GEOsE3P-wSPimdQAC8RIAAgU-sEu8tCkctsJQBy8E")
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)