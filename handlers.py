from aiogram import types, Dispatcher
from loguru import logger

# from create_bot import DP
from create_bot import BOT
from keyboards import inline_kb_yon, inline_kb_start
from data import MESSAGES, get_paper

# {id: [state(0, 1, 2, 3, 4), 'paper', 'paper', ...]}
USERS = {}


# ответ на запуск бота
# @DP.message_handler(commands=['start'])
async def command_start(message: types.Message):
    user_id = message.from_user.id
    if not (user_id in USERS.keys()):
        USERS[user_id] = []
        logger.info(f'Новый пользователь! {user_id}')

    msg = MESSAGES[0]
    await BOT.send_message(message.from_user.id,
                           msg, reply_markup=inline_kb_yon)
    USERS[user_id][0] = 0

    logger.info(f'пользователь {user_id} ввел команду /start')


# @DP.callback_query_handler(text='no')
async def callback_button_no(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if USERS[user_id][0] == 0:
        msg = MESSAGES[1.0]
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown", reply_markup=inline_kb_start)

    elif USERS[user_id][0] == 1:
        msg = MESSAGES[2.0]
        USERS[user_id][0] = 2.0
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown", reply_markup=inline_kb_yon)

    elif USERS[user_id][0] == 2.0:
        msg = MESSAGES[4.0]
        USERS[user_id][0] = 0
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown", reply_markup=inline_kb_start)

    elif USERS[user_id][0] == 2.1:
        msg = MESSAGES[3.0]
        USERS[user_id][0] = 0
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown", reply_markup=inline_kb_start)


# @DP.callback_query_handler(text='yes')
async def callback_button_yes(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if USERS[user_id][0] == 0:
        msg = MESSAGES[1.1]
        USERS[user_id][0] = 1
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown", reply_markup=inline_kb_start)

    elif USERS[user_id][0] == 1:
        paper = get_paper()
        msg = MESSAGES[2.1].replace('PAPER', paper)
        USERS[user_id][0] = 2.1
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown", reply_markup=inline_kb_start)

    elif USERS[user_id][0] == 2.0:
        msg = MESSAGES[4.1]
        USERS[user_id][0] = 0
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown", reply_markup=inline_kb_start)

    elif USERS[user_id][0] == 2.1:
        msg = MESSAGES[3.1]
        USERS[user_id][0] = 0
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown", reply_markup=inline_kb_start)


# @DP.callback_query_handler(text='start')
async def callback_button_start(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    msg = MESSAGES[0]
    await BOT.send_message(callback_query.from_user.id,
                           msg, reply_markup=inline_kb_yon)
    USERS[user_id][0] = 0

    logger.info(f'пользователь {user_id} начал с начала')


# регистрация всех хэндлеров в отдельной ф-ии
# чтобы потом передать именно ее в нужное место
def register_handlers_main(DP: Dispatcher):
    DP.register_message_handler(command_start, commands=['start'])
    DP.register_callback_query_handler(callback_button_no, text='no')
    DP.register_callback_query_handler(callback_button_yes, text='yes')
    DP.register_callback_query_handler(callback_button_start, text='start')
