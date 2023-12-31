# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.types import InputFile
from loguru import logger
import os

# from create_bot import DP
from create_bot import BOT
from keyboards import inline_kb_yon, inline_kb_start, kb_start
from data import MESSAGES, QUESTIONS, get_paper
from states import States
from work_db import check_id_users, add_user, check_user_papers, add_paper


# ответ на запуск бота
# @DP.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_lst = check_id_users()
    user_list = [i[0] for i in user_lst]

    if not (user_id in user_list):
        add_user(user_id)
        logger.info(f'Новый пользователь! {user_id}')

    msg = MESSAGES[0]
    quest = QUESTIONS[0]
    photo = os.getenv('PATH_FOR_IMG') + '0.jpg'
    await BOT.send_photo(message.from_user.id, photo=InputFile(photo))
    await BOT.send_message(message.from_user.id,
                           msg, reply_markup=kb_start)
    await BOT.send_message(message.from_user.id,
                           quest, reply_markup=inline_kb_yon, parse_mode="Markdown")

    logger.info(f'Пользователь {user_id} ввел команду /start')

    # установить состояние пользователя
    await state.set_state(States.step_0)
    logger.info(f'Состояние {user_id} сменилось -> {await state.get_state(message.from_user.id)}')


# @DP.callback_query_handler(text='no')
async def callback_button_no(callback_query: types.CallbackQuery, state: FSMContext):
    # await BOT.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    user_id = callback_query.from_user.id
    state_user_check = await state.get_state(callback_query.from_user.id)

    if state_user_check == 'States:step_0':
        msg = MESSAGES[1.0]
        photo = os.getenv('PATH_FOR_IMG') + '1_0.jpg'
        await BOT.send_photo(callback_query.from_user.id, photo=InputFile(photo))
        await BOT.send_message(callback_query.from_user.id,
                               msg, reply_markup=inline_kb_start)

    elif state_user_check == 'States:step_1':
        msg = MESSAGES[2.0]
        quest = QUESTIONS[2.0]
        photo = os.getenv('PATH_FOR_IMG') + '2_0.jpg'

        # смена состояния
        await state.set_state(States.step_20)
        logger.info(f'Состояние {user_id} сменилось -> {await state.get_state(callback_query.from_user.id)}')

        await BOT.send_photo(callback_query.from_user.id, photo=InputFile(photo))
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown")
        await BOT.send_message(callback_query.from_user.id,
                               quest, reply_markup=inline_kb_yon, parse_mode="Markdown")

    elif state_user_check == 'States:step_20':
        msg = MESSAGES[4.0]
        photo = os.getenv('PATH_FOR_IMG') + '4_0.jpg'

        # смена состояния
        await state.set_state(States.step_0)
        logger.info(f'Состояние {user_id} сменилось -> {await state.get_state(callback_query.from_user.id)}')

        await BOT.send_photo(callback_query.from_user.id, photo=InputFile(photo))
        await BOT.send_message(callback_query.from_user.id,
                               msg, reply_markup=inline_kb_start)

    elif state_user_check == 'States:step_21':
        msg = MESSAGES[3.0]
        photo = os.getenv('PATH_FOR_IMG') + '3_0.jpg'

        # смена состояния
        await state.set_state(States.step_0)
        logger.info(f'Состояние {user_id} сменилось -> {await state.get_state(callback_query.from_user.id)}')

        await BOT.send_photo(callback_query.from_user.id, photo=InputFile(photo))
        await BOT.send_message(callback_query.from_user.id,
                               msg, reply_markup=inline_kb_start)


# @DP.callback_query_handler(text='yes')
async def callback_button_yes(callback_query: types.CallbackQuery, state: FSMContext):
    # await BOT.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    user_id = callback_query.from_user.id
    state_user_check = await state.get_state(callback_query.from_user.id)

    if state_user_check == 'States:step_0':
        msg = MESSAGES[1.1]
        quest = QUESTIONS[1.1]
        photo = os.getenv('PATH_FOR_IMG') + '1_1.jpg'

        # смена состояния
        await state.set_state(States.step_1)
        logger.info(f'Состояние {user_id} сменилось -> {await state.get_state(callback_query.from_user.id)}')

        await BOT.send_photo(callback_query.from_user.id, photo=InputFile(photo))
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown")
        await BOT.send_message(callback_query.from_user.id,
                               quest, reply_markup=inline_kb_yon, parse_mode="Markdown")

    elif state_user_check == 'States:step_1':
        paper = get_paper()
        msg = MESSAGES[2.1].replace('PAPER', paper)
        quest = QUESTIONS[2.1]
        photo = os.getenv('PATH_FOR_IMG') + '2_1.jpg'

        # !!! добавить функцию добавления бумажки в бд !!!

        # смена состояния
        await state.set_state(States.step_21)
        logger.info(f'Состояние {user_id} сменилось -> {await state.get_state(callback_query.from_user.id)}')

        await BOT.send_photo(callback_query.from_user.id, photo=InputFile(photo))
        await BOT.send_message(callback_query.from_user.id,
                               msg, parse_mode="Markdown")
        await BOT.send_message(callback_query.from_user.id,
                               quest, reply_markup=inline_kb_yon, parse_mode="Markdown")

    elif state_user_check == 'States:step_20':
        msg = MESSAGES[4.1]
        photo = os.getenv('PATH_FOR_IMG') + '4_1.jpg'

        # смена состояния
        await state.set_state(States.step_0)
        logger.info(f'Состояние {user_id} сменилось -> {await state.get_state(callback_query.from_user.id)}')

        await BOT.send_photo(callback_query.from_user.id, photo=InputFile(photo))
        await BOT.send_message(callback_query.from_user.id,
                               msg, reply_markup=inline_kb_start)

    elif state_user_check == 'States:step_21':
        msg = MESSAGES[3.1]
        photo = os.getenv('PATH_FOR_IMG') + '3_1.jpg'

        # смена состояния
        await state.set_state(States.step_0)
        logger.info(f'Состояние {user_id} сменилось -> {await state.get_state(callback_query.from_user.id)}')

        await BOT.send_photo(callback_query.from_user.id, photo=InputFile(photo))
        await BOT.send_message(callback_query.from_user.id,
                               msg, reply_markup=inline_kb_start)


# @DP.callback_query_handler(text='start')
async def callback_button_start(callback_query: types.CallbackQuery, state: FSMContext):
    # await BOT.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    user_id = callback_query.from_user.id
    msg = MESSAGES[0]
    quest = QUESTIONS[0]
    photo = os.getenv('PATH_FOR_IMG') + '0.jpg'
    await BOT.send_photo(callback_query.from_user.id, photo=InputFile(photo))
    await BOT.send_message(callback_query.from_user.id,
                           msg, parse_mode="Markdown")
    await BOT.send_message(callback_query.from_user.id,
                           quest, reply_markup=inline_kb_yon, parse_mode="Markdown")

    # смена состояния
    await state.set_state(States.step_0)
    logger.info(f'Состояние {user_id} сменилось -> {await state.get_state(callback_query.from_user.id)}')
    logger.info(f'Пользователь {user_id} начал с начала')

'''
# @DP.message_handler()
async def view_history_paper(message: types.Message, state: FSMContext):
    if message.text == 'Заглянуть в карман':
        user_id = message.from_user.id
        papers_list = check_user_papers()

        if not (papers_list):
            msg = MESSAGES['no_papers']

        elif len(papers_list) == 1:
            paper = get_paper_db(papers_list[0])
            msg= MESSAGES['one_paper'] + paper

        else:
            papers = get_paper_db(papers_list)
            msg = MESSAGES['papers']

        await BOT.send_message(message.from_user.id,
                               msg)


        logger.info(f'Пользователь {user_id} проверяет карманы')

    else:
        logger.warning(f'Пользователь {user_id} пытается разговаривать с ботом')
'''


# регистрация всех хэндлеров в отдельной ф-ии
# чтобы потом передать именно ее в нужное место
def register_handlers_main(DP: Dispatcher):
    DP.register_message_handler(command_start, commands=['start'], state='*')
    DP.register_callback_query_handler(callback_button_no, text='no', state='*')
    DP.register_callback_query_handler(callback_button_yes, text='yes', state='*')
    DP.register_callback_query_handler(callback_button_start, text='start', state='*')
