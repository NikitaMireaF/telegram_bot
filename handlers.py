from aiogram import Router
from aiogram.dispatcher import router
from aiogram.filters import Command
from keyboard import ikb_hi, ikb_mail
from main import bot
from admin_filter import Admin
from aiogram.enums import ParseMode
import datetime
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message, InlineKeyboardButton
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
id_users = [984974593]

router = Router()


@router.message(Command("start"), Admin())
async def start_message(message: Message):
    await message.answer(f"Приветствую, тебя в боте для рассылки {message.from_user.first_name if message.from_user.first_name else ''}", reply_markup=ikb_hi())


@router.callback_query(F.data == "ikb_hi", Admin())
async def answer_start(callback: types.CallbackQuery):
    await callback.message.answer("Впишите текст рассылки")


@router.message(Admin())
async def get_mail_from_admin(message: Message):
    global text_mail
    text_mail = message.text
    global id_users
    await message.answer(f"Разослать сообщениение \n<b>{text_mail}</b>\nДля <b>{len(id_users)} пользователя?</b> ", parse_mode=ParseMode.HTML, reply_markup=ikb_mail())


@router.callback_query(F.data == "ikb_mail")
async def mail_to_users(callback: types.CallbackQuery):
    global id_users
    global text_mail
    counter = 0
    try:
        for id in id_users:
            await bot.send_message(chat_id=id, text=text_mail)
            counter += 1
        await callback.message.answer(f"Успешно разосланно {counter} сообщений")
    except:
        await callback.message.answer("Что то пошло не так")