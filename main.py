from aiogram import Bot, Dispatcher, types, executor


bot = Bot('5868878555:AAEetjhGk43IZ2LasbIa9vKbzTNCQ92slrs')
dp = Dispatcher(bot)
HELP_COMMAND = """
<b>/help</b> - <em>показывает список команд</em>
<b>/give</b> - <em>отправляет стикер</em>
<b>/start</b> - <em>запускает бота</em>"""

async def on_startup(_):            #функция выводит сообщение в консоли, "я запстился", вконце нужно его прписать в запуске
    print("Я запустился")


@dp.message_handler(commands=['help'])                           # вызывает команд help с описанием других команд
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')



@dp.message_handler(commands=['give'])                      # Отправляет стикер
async def send_sticker (message: types.message):
    await message.answer('Смотри какой котик ❤️')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIuj9kSAJARtxuE2DUd79aKvjnhhucAAMKHQACwaggSQiNN_5i8NF4LwQ')


@dp.message_handler(content_types=['sticker'])     # Отправляем стикер и получаем его ID
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)

# @dp.message_handler()                                   # отчечает емоджи на емоджи
# async def send_sticker (message: types.message):
#     if message.text == '❤️':
#         await message.answer('🖤')

@dp.message_handler()                           # Подсчет количества галочек
async def count(message: types.Message):
    await message.answer(text= str(message.text.count('✅')))





if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)