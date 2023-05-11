import random

from aiogram import Bot, Dispatcher, executor, types
from keyboards import kb, kb_photo, ikb
from config import TOKEN_API
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove               #Чтобы убирать клваатуру после команды
from random import choice

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot = bot)
HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/Random photo</b> - <em>отправка случайное фото</em>"""


arr_photos = ["https://yandex.ru/images/search?pos=40&img_url=https%3A%2F%2Fsun9-9.userapi.com%2Fimpg%2FU8DJ2JiZtnRCMyufsqGVeaCoEnrI3zt6OwfOBA%2F4XbMeBkLWXk.jpg%3Fsize%3D800x527%26quality%3D96%26sign%3D1c2c9c269893d023bee6aba85787d9a4%26c_uniq_tag%3DlxQMy7HkDGAKV4NrWRpkdoXesyGRinlPJDqMHcxpG6Q%26type%3Dalbum&text=коты+смешные&rpt=simage&lr=213",
              "https://yandex.ru/images/search?p=1&text=коты+смешные&pos=34&rpt=simage&img_url=https%3A%2F%2Fimg1.goodfon.ru%2Foriginal%2F5184x3456%2Fb%2F72%2Fskottish-fold-morda-shapka.jpg&lr=213",
              "https://yandex.ru/images/search?p=2&text=коты+смешные&pos=26&rpt=simage&img_url=https%3A%2F%2Fkrasivosti.pro%2Fuploads%2Fposts%2F2021-03%2F1616466037_28-p-tri-kota-i-koshechka-foto-koshka-34.jpg&lr=213"]

photos = dict(zip(arr_photos, ['Кота-кактус', 'Дай пять', 'Странное фото']))             #zip - чтобы сшить два массива в одном словаре
random_photo = random.choice(list(photos.keys()))

flag = False

async def on_startup(_):
    print("Я запустился")


async def send_random(message: types.Message):
    global random_photo
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb)


@dp.message_handler(Text(equals='Random photo'))
async def open_kb_photo (message: types.Message):
    await message.answer(text="Рандомная фотка!",reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()


@dp.message_handler(Text(equals='Главное меню'))
async def open_kb (message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню',
                         reply_markup=kb)
    await message.delete()

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


@dp.message_handler(commands='location')
async def cmd_location(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.randint(0,50),
                            longitude=random.randint(0,50))

@dp.message_handler(commands=['Random photo'])
async def cmd_photo (message: types.Message):
    await message.answer(text='Наш бот умеет отправлять рандомные фотки')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgIAAxkBAAEI1_xkUqSQEN8_C06GEOsE3P-wSPimdQAC8RIAAgU-sEu8tCkctsJQBy8E")
    await message.delete()


@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_photo             #! Недопустимо использование глобальных переменных
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer('Вам понравилась фотка')
            flag = not flag
        else:
            await callback.answer('Вы уже лайкали')
        # await callback.message.answer('Вам понравилась фотка')
    elif callback.data == 'dislike':
        await callback.answer('Вам не понравилась фотка')
        # await callback.message.answer('Вам не понравилась фотка')
    elif callback.data == 'main':
        await callback.message.answer(text='Добро пожаловать в главное мению',
                                      reply_markup=kb)
        await callback.message.delete()
        await callback.answer()
    else:
        # random_photo = random.choice(list(photos.keys()))           # Так кнопка отрабатывает один раз, а потом исключения, поэтому надо получить новый файл
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption= photos[random_photo]),
                                                           reply_markup=ikb)
        await callback.answer()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)