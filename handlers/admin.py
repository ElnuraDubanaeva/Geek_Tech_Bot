from aiogram import types, Dispatcher
from config import admin, bot
from random import choice
from database.bot_db import delete_sql, all_sql, get_all_usernames
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def delete_data(message: types.Message):
    if message.from_user.id not in admin:
        await message.answer('Only admins can delete the data')
    else:
        mentors = await all_sql()
        for mentor in mentors:
            await message.answer(f"Number: {mentor[2]}"
                                 f"\nName: {mentor[1]}"
                                 f"\nGroup: {mentor[3]}"
                                 f"\nDepartment: {mentor[5]}"
                                 f"\nAge: {mentor[4]}"
                                 f"\nUsername: {mentor[6]}",
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(f"delete {mentor[1]}",
                                                          callback_data=f"delete {mentor[0]}")))


async def complete_delete(call: types.CallbackQuery):
    await delete_sql(call.data.replace('delete ', ''))
    await call.answer(text="deleted!", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)

#
# async def mailing(message: types.Message):
#     if message.from_user.id not in admin:
#         await message.answer('Only admins can delete the data')
#     else:
#         mentor_usernames = await get_all_usernames()
#         for mentor_username in mentor_usernames:
#             message.from_user.username = mentor_username[0]
#             await bot.send_message(chat_id=message.from_user.username.id, text=message.text.replace('/R', ''))


async def game(message: types.Message):
    emojis = '🏀 ⚽ 🎲 🎳 🎰 🎯'.split()
    if message.from_user.id in admin:
        if message.text.startswith('game'):
            await bot.send_dice(message.chat.id, emoji=choice(emojis))
        else:
            await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await message.reply(f'Only admins can start the game')


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))
    # dp.register_message_handler(mailing, commands=['R'])
    dp.register_message_handler(game)
