import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import openai

# 🔥 Пряме встановлення API-ключів (ЗАМІНИ НА СВОЇ)
TELEGRAM_BOT_TOKEN = "7858075515:AAHkJvKomSWgS6V4-qx4b76dCW04IcOYutE"
OPENAI_API_KEY = "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"

# Переконуємося, що ключі не пусті
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не вказано!")
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY не вказано!")

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
