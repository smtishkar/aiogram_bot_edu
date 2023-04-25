from aiogram import Bot, Dispatcher, types, executor
import string
import random

bot = Bot('5868878555:AAEetjhGk43IZ2LasbIa9vKbzTNCQ92slrs')
dp = Dispatcher(bot)

count = 0

@dp.message_handler(commands=['description'])
async def desc_command (message: types.message):
    await message.answer('Данные бот отправляет рандомные символы')
    await message.delete()


@dp.message_handler(commands=['count'])
async def check_counts(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count+=1


@dp.message_handler()
async def check_zero (message: types.Message):
    if "0" in message.text:
        await message.reply("YES")
    else:
        await message.reply("NO")


@dp.message_handler()
async def send_random_letter (message: types.Message):
    await message.reply(random.choice(string.ascii_letters))   #рандомная буква

if __name__ == '__main__':
    executor.start_polling(dp)