import os
import logging  #модуль для логирования (отключать на проде т.к замедляет бота)
import asyncio
from aiogram import Bot, Dispatcher, F #здесь F это класс у которого есть magic filter
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')

@dp.message(Command('help'))   #различные команды
async def get_help(message: Message):
    await message.answer('Это команда /help')

@dp.message(F.text == 'Как дела') #обратное сообщению юзеру на определленное сообщение (не ответное сообщение!)
async def how_are_you(message: Message):
    await message.answer('OK!')

@dp.message(F.photo) #"ловим" фото/рисунок от юзера от отправляем в ответ айди этого фото
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

@dp.message(F.text == 'фотку') #отправка фото(по id файла) юзеру на определленное сообщение здесь "фотку"
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAANyZlckDbNhjVoeXf3AhZEIpLOtjaMAAoLfMRtdfrhKHaqneuL8Qn0BAAMCAAN4AAM1BA',
                               caption='Это описание фотки')

@dp.message(F.text == 'мяу') #отправка фото(по ссылке) юзеру на определленное сообщение здесь "мяу"
async def get_photo(message: Message):
    await message.answer_photo(photo='https://ru.freepik.com/free-photo/close-up-on-kitten-surrounded-by-flowers_65553514.htm#query=%D0%BC%D0%B8%D0%BB%D1%8B%D0%B9%20%D0%BA%D0%BE%D1%82%D0%B8%D0%BA&position=9&from_view=keyword&track=ais_user&uuid=3e891b3d-6f53-47d2-ab9d-4b48fb3f28db.jpg',
                               caption='Это картинка из интернета')

@dp.message(Command('my_id')) #здесь ОТВЕТ на КОМАНДУ "my_id" айди юзера и его имя
async def get_user_id(message: Message):
    await message.reply(f'Привет\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')

async def main() -> None:
    load_dotenv()
    bot = Bot(os.getenv('TOKENF'))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO) #добавили строчку логирования
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')