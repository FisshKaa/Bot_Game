from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" Отправится в путешествие!"),
            KeyboardButton(text=" о идеи"),
            KeyboardButton(text=" кнопка чтобы отправить обратный отзыв "),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?'
)