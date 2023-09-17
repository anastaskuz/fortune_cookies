# from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


# создание кнопок с callback_data
inline_btn_yes = InlineKeyboardButton('Да', callback_data='yes')
inline_btn_no = InlineKeyboardButton('Нет', callback_data='no')
inline_btn_start = InlineKeyboardButton('Начать с начала', callback_data='start')


inline_kb_yon = InlineKeyboardMarkup().add(inline_btn_yes, inline_btn_no)
inline_kb_start = InlineKeyboardMarkup().add(inline_btn_start)
