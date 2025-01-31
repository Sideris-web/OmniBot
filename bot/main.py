import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import openai

# Завантажуємо API-ключі з оточення
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Налаштовуємо OpenAI API
openai.api_key = OPENAI_API_KEY

# Ініціалізуємо Telegram бота
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

# Логування
logging.basicConfig(level=logging.INFO)

# Обробка команд
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привіт! Я OmniBot 🤖. Запитай мене що завгодно!")

# Обробка повідомлень
@dp.message_handler()
async def chat_with_gpt(message: types.Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": message.text}]
        )
        reply = response["choices"][0]["message"]["content"]
        await message.reply(reply)
    except Exception as e:
        logging.error(f"Помилка OpenAI API: {e}")
        await message.reply("Виникла помилка. Спробуй ще раз!")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
