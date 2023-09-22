from loguru import logger
from aiogram import executor
import os

from create_bot import DP
from work_db import create_db, create_table
from handlers import register_handlers_main


# хэндлеры
register_handlers_main(DP)


if __name__ == '__main__':
    if not ('fortune_cookies.db' in os.listdir(os.getenv('PATH_FOR_DB'))):
        create_db()
        create_table()

    logger.info('Бот активен')
    # запуск бота
    # skip_updates - чтобы когда бот вышел из неактивного режима,
    # все пришедшие ему сообщения за это время на него не свалились
    executor.start_polling(DP, skip_updates=True)
