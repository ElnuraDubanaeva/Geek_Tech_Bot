from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = "5696177932:AAH-2SFIk5ARH-BU34w1h7flQpxn21BM1w0"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
admin = [1927522329, ]
