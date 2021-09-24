import telebot;
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
# Объект бота
bot = Bot(token="-")
# Диспетчер для бота
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Хочу анекдот!"]
    keyboard.add(*buttons)
    await message.answer("Хотите анекдот?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Хочу анекдот!"))
async def without_puree(message: types.Message):
    await message.answer(prikol())

def prikol():
    anek=[]
    response = requests.get("https://www.anekdot.ru/random/anekdot/", headers={'User-Agent': UserAgent().chrome})
    soup = bs(response.text, "html.parser")
    anekdots = soup.find_all('div', class_='text') 
    for anekdot in anekdots:
        anek.append(anekdot)
    return (anek[0].text)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
