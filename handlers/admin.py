from aiogram import types, Dispatcher
from config import admin, bot
from random import choice


async def game(message: types.Message):
    emojis = ['🏀,⚽️,🎲,🎳,🎰,🎯']
    if message.from_user.id in admin:
        if message.text.startswith('game'):
            await bot.send_dice(message.chat.id, emoji=choice(emojis))
    else:
        await message.reply(f'Only admins can start the game')


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(game, content_types=['text'])
