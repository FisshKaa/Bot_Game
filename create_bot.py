import asyncio


from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.keyboard import start_kb
from answer.text import *

from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, or_f, Command
from aiogram.types import Message


from main_settings.config import API_TOKEN

router = Router()
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
admin_id = '999962779'

user_feedback_mode = {}




@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'{start}', reply_markup=start_kb)

@dp.message(or_f(Command("idea"), (F.text.lower() == 'о идеи')))
async def about_cmd(message: Message):
    await message.answer(f"{idea}", reply_markup=start_kb)



@dp.message(or_f(Command('feedback'), (F.text.lower() == 'кнопка чтобы отправить обратный отзыв')))
async def feedback_cmd(message: types.Message):
    user_feedback_mode[message.from_user.id] = True
    await message.answer("Пожалуйста, напишите ваш отзыв:", reply_markup=types.ReplyKeyboardRemove())


@dp.message()
async def handle_message(message: types.Message):
    if user_feedback_mode.get(message.from_user.id):
        await bot.send_message(admin_id, f"Новый отзыв от {message.from_user.username}:\n{message.text}")

        await message.answer("Ваш отзыв отправлен. Спасибо!", reply_markup=start_kb)

        user_feedback_mode[message.from_user.id] = False
    else:
        await message.answer("Я рад с вами поговирить, но нужно нажать на кнопку 'оставить отзыв', если хотите чтобы я прочитал что вы мне написали <3.")




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')