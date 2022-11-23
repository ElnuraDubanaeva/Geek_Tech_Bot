from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, admin
from keyboards.client_kb import submit_markup, cancel_markup, part_markup
from database.bot_db import insert_sql


class FSMAdmin(StatesGroup):
    mentor_id = State()
    mentor_name = State()
    mentor_number = State()
    mentor_group = State()
    mentor_age = State()
    mentor_part = State()
    mentor_username = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in admin:
        await FSMAdmin.mentor_id.set()
        await message.answer('Укажите id ментора:')
    else:
        await message.answer('Только админ может регистрировать ментора')


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor_id'] = message.text
    await FSMAdmin.next()
    await message.answer('Укажите имя ментора:', reply_markup=cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor_name'] = message.text
    await FSMAdmin.next()
    await message.answer('Укажите number ментора:', reply_markup=cancel_markup)


async def load_mentor_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor_number'] = f'+996{message.text}'
    await FSMAdmin.next()
    await message.answer('Укажите группу ментора:', reply_markup=cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor_group'] = message.text
    await FSMAdmin.next()
    await message.answer('Возраст ментора:')


async def load_age(message: types.Message, state: FSMContext):
    try:
        if 18 <= int(message.text) < 50:
            async with state.proxy() as data:
                data['mentor_age'] = message.text
            await FSMAdmin.next()
            await message.answer('Выберите направление ментора: ', reply_markup=part_markup)
        else:
            await message.answer('Возраст не подходит')
    except:
        await message.answer('Пишите цифры')


async def load_part(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor_part'] = message.text
    await FSMAdmin.next()
    await message.answer('Укажите username ментора c@')


async def load_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor_username'] = message.text
        await message.answer(f"\nNumber: {data['mentor_number']}"
                             f"\nName: {data['mentor_name']}"
                             f"\nGroup: {data['mentor_group']}"
                             f"\nDepartment: {data['mentor_part']}"
                             f"\nAge: {data['mentor_age']}"
                             f"\nUsername: {data['mentor_username']}")
        await FSMAdmin.next()
        await message.answer('Все данные правильны?', reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text == "ДА":
        await insert_sql(state)
        await state.finish()
        await message.answer("Регистрация успешно завершена")
    elif message.text == "НЕТ":
        await state.finish()
        await bot.send_message(message.from_user.id, "Отмена")
    else:
        await message.answer("Да или Нет!?")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Отмена")


def register_handlers_fsm_mentor(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id,state=FSMAdmin.mentor_id)
    dp.register_message_handler(load_name, state=FSMAdmin.mentor_name)
    dp.register_message_handler(load_mentor_id, state=FSMAdmin.mentor_number)
    dp.register_message_handler(load_group, state=FSMAdmin.mentor_group)
    dp.register_message_handler(load_part, state=FSMAdmin.mentor_part)
    dp.register_message_handler(load_age, state=FSMAdmin.mentor_age)
    dp.register_message_handler(load_username, state=FSMAdmin.mentor_username)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
