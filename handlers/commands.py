from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from handlers.hw7 import question
from parsers.perser import parser


async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"привет  {message.from_user.full_name}\n"
                                            f"начинаем \n"
                                            f"викторину -> /quiz \n"
                                            f"прикольный mem  -> /mem\n")


async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "Кто создал Chatgpt?"
    answers = [
        "James Cameron",
        "Sam Altman",
        "Elon Musk",
        "Batman",
        "Spongebob",

    ]

    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        reply_markup=markup
    )


async def get_mem(message: types.Message):
    photo = open(r"", 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


async def find(message: types.Message):
    await message.answer(question(message))


async def get(message: types.Message):
    pars = parser()

    for ps in pars:
        await message.answer(f'{ps["url"]}\n'
                             f'{ps["time"]}\n'
                             f'{ps["title"]}\n')


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_mem, commands=['mem'])
    dp.register_message_handler(find, commands=['find'])
    dp.register_message_handler(get, commands=['ps'])
