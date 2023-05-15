from  aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('❤', callback_data= 'like'),InlineKeyboardButton('👎', callback_data='dislike')]
])


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://mobimg.b-cdn.net/v3/fetch/75/754da20683ab4a8f859dfa0a7ba0f9ce.jpeg',
                         caption='Нравится ли тебе фото',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def ikb_cb_handler(callback:types.CallbackQuery):
    print(callback)
    if callback.data == 'like':
        await callback.answer('Тебе понравилось фото')
    await callback.answer('Тебе не понравилось фото')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)