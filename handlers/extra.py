from config import bot
from aiogram import types, Dispatcher
from parser.lyric import parser_name


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith('Billie Eilish '):
        items = parser_name()
        for item in items:
            if message.text.replace('Billie Eilish ','') == item["name"]:
                song = open(f'media/{item["name"]}.mp3','rb')
                if song:
                    await bot.send_audio(message.from_user.id,song)
                else:
                    continue
    elif message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_extra_handler(dp: Dispatcher):
    dp.register_message_handler(echo)
