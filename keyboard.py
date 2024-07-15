from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton


def ikb_hi():
    btn1 = InlineKeyboardButton(text="Привет! Начать работу!", callback_data="ikb_hi")
    builder = InlineKeyboardMarkup(inline_keyboard=[[btn1]])
    return builder

def ikb_mail():
    btn1 = InlineKeyboardButton(text="Пуск", callback_data="ikb_mail")
    btn2 = InlineKeyboardButton(text="Отмена", callback_data="ikb_cancel")
    builder = InlineKeyboardMarkup(inline_keyboard=[[btn1], [btn2]])
    return builder