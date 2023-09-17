from aiogram import Bot, Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os


# создание экземпляра бота и диспетчера
# STORAGE = MemoryStorage()
BOT = Bot(token=os.getenv('TOKEN'))
# DP = Dispatcher(BOT, storage=STORAGE)
DP = Dispatcher(BOT)
