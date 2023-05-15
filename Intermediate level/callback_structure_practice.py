from  aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

is_voted = False

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Like', callback_data='like'), InlineKeyboardButton('Dislike', callback_data='dislike')],
    [InlineKeyboardButton('close keyboard', callback_data= 'close')]
])


@dp.message_handler(commands=['start'])
async def cmd_start (message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://mobimg.b-cdn.net/v3/fetch/75/754da20683ab4a8f859dfa0a7ba0f9ce.jpeg',
                         caption='Нравится ли фото?',
                         reply_markup=ikb)



@dp.callback_query_handler(text= 'close')
async def ikb_close_cb_handler(callback: types.CallbackQuery):
    await callback.message.delete()


@dp.callback_query_handler()
async def ikb_close_cb_handler(callback: types.CallbackQuery):

    # await callback.answer(str(callback.data))               # Выводит callback.data
    # await callback.answer(show_alert=True,                      # Выводит текстовое сообщение
    #                       text=str(callback.data))

    global is_voted
    if not is_voted:
        if callback.data == 'like':
            await callback.answer(show_alert=False,
                                text='Тебе понравилось')
            is_voted = True
        await callback.answer(show_alert=False,
                              text='Тебе не понравилось')
        is_voted = True
    await callback.answer(show_alert=True,text= 'Ты уже голосовал')



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)