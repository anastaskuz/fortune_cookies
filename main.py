from loguru import logger
from aiogram import executor

from create_bot import DP
from handlers import register_handlers_main


# хэндлеры
register_handlers_main(DP)


if __name__ == '__main__':
    logger.info('Запущен бот')
    # запуск бота
    # skip_updates - чтобы когда бот вышел из неактивного режима,
    # все пришедшие ему сообщения за это время на него не свалились
    executor.start_polling(DP, skip_updates=True)
