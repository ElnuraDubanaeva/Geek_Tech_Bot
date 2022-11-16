from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, admin
from keyboards.client_kb import submit_markup, cancel_markup, part_markup, start_markup


class FSMAdmin(StatesGroup):
    mentor_id = State()
    name = State()
    group = State()
    part = State()
    age = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in admin:
        await FSMAdmin.name.set()
        await message.answer('Укажите имя ментора:')
    else:
        await message.answer('Только админ может регистрировать ментора')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Укажите id ментора:', reply_markup=cancel_markup)


async def load_mentor_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor_id'] = message.text
    await FSMAdmin.next()
    await message.answer('Укажите группу ментора:', reply_markup=cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMAdmin.next()
    await message.answer('Выберите направление ментора: ', reply_markup=part_markup)


async def load_part(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['part'] = message.text
    await FSMAdmin.next()
    await message.answer('Возраст ментора:')


async def load_age(message: types.Message, state: FSMContext):
    try:
        if 18 <= int(message.text) < 50:
            async with state.proxy() as data:
                data['part'] = message.text
            await FSMAdmin.next()
            await message.answer('Все данные правильны?', reply_markup=submit_markup)
        else:
            await message.answer('Возраст не подходит')
    except:
        await message.answer('Пишите цифры')


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        # Запись в БД
        await state.finish()
        await message.answer("Регистрация успешно завершена")
    elif message.text.lower() == "нет":
        await state.finish()
        await bot.send_message(message.from_user.id, "Отмено")
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
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_mentor_id, state=FSMAdmin.mentor_id)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_part, state=FSMAdmin.part)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
