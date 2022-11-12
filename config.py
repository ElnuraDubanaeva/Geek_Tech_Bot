from decouple import config
from aiogram import Bot, Dispatcher

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
admin = [1927522329, ]
