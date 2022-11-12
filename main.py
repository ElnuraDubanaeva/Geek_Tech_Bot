from aiogram.utils import executor
import logging
from config import dp
from handlers import admin, client, callback, extra

client.register_handlers_client(dp)
callback.register_callback_handlers(dp)
admin.register_admin_handler(dp)
extra.register_extra_handler(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

