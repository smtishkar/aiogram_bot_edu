from aiogram import Bot, Dispatcher, types, executor

bot = Bot('5868878555:AAEetjhGk43IZ2LasbIa9vKbzTNCQ92slrs')
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_upper (message: types.Message):
    if message.text.count(' ')>=1:
        await message.answer(text = message.text.upper())


if __name__ == '__main__':
    executor.start_polling(dp)