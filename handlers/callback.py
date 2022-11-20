from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Вопрос можно ли делать так чтобы викторину отправлял в чат айди а не в юзер айди?
# @dp.callback_query_handler(text="button_call_2")


async def quiz_2(call: types.CallbackQuery):
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


# @dp.callback_query_handler(text="button_call_3")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data='button_call_3')
    markup.add(button_call_3)
    question = 'Перевод "бессмертный" на английском'
    answer = [
        'consistent',
        'immortal',
        'treatment',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Learn new words',
        open_period=10,
        reply_markup=markup,

    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")
