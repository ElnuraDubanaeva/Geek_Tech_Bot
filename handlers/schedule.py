import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio
from parser.lyric import parser_music


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('Okay!')


async def reminder():
    await bot.send_message(chat_id, f'''Почему важно писать #StandUp?
                                                    \n1. Судя по этим вашим «отчетам» мы можем вовремя придти к вам на помощь 🏃🏻‍♀️
                                                    \n2. От этих стендапов зависит ваша скидка 🏷
                                                    \n3. Важно писать стендапы потому, что мы это считаем, нам важно это знать☝️
                                                    \n4. От этого зависит успеваемость вашей группы🫂
                                                    \n5. Надеюсь видеть в группах много StandUp‘ов 😌''')


async def scheduler():
    aioschedule.every().thursday.at('15:13').do(reminder)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


async def download_music():
    items = await parser_music()
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(20)
        return items


async def scheduler_2():
    aioschedule.every().thursday.at('19:30').do(download_music)


def register_handlers_schedule(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'remind' in word.text)
