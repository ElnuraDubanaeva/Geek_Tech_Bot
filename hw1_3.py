from aiogram import Bot, Dispatcher, types
from decouple import config
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    question = 'Перевод "последовательность" на английском'
    answer = [
        'consistent',
        'consistency',
        'treatment',
        'forgiveness'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Learn new words',
        open_period=10,
        reply_markup=markup,

    )


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)
    question = 'Перевод "частота" на английском'
    answer = [
        'consistent',
        'consistency',
        'treatment',
        'frequency'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Learn new words',
        open_period=10,
        reply_markup=markup,

    )


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name}')


@dp.message_handler(commands=["mem"])
async def mem_handler(message: types.Message):
    photo = open("media/img.png", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
