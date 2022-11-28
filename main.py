from aiogram.utils import executor
import logging
from config import dp
from handlers import admin, client, callback, extra, fsm_admin_mentor, schedule
from database.bot_db import create_sql
import asyncio


async def on_startup(_):
    asyncio.create_task(schedule.scheduler())
    create_sql()


client.register_handlers_client(dp)
callback.register_callback_handlers(dp)
fsm_admin_mentor.register_handlers_fsm_mentor(dp)
schedule.register_handlers_schedule(dp)

extra.register_extra_handler(dp)
admin.register_admin_handler(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
