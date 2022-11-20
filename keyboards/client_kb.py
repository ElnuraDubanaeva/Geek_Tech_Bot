from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2,

).add(
    KeyboardButton('/quiz'),
    KeyboardButton('/mem'),
    KeyboardButton('/dice'),
    KeyboardButton('/help'),
    KeyboardButton('/reg'),
    KeyboardButton('/get'),
    KeyboardButton('/del'),
    # KeyboardButton('/R')
)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("ДА"),
    KeyboardButton("НЕТ"),

)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("CANCEL")
)
part_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width = 3,
).add(
    KeyboardButton("Backend"),
    KeyboardButton("Frontend"),
    KeyboardButton("Android"),
    KeyboardButton("UX-UI"),
    KeyboardButton('IOS'),
    KeyboardButton('fullstack'),
    KeyboardButton('CANCEL')
)
