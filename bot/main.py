import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import openai

# 🔥 ВСТАНОВЛЮЄМО КЛЮЧІ НАПРЯМУ
TELEGRAM_BOT_TOKEN = "7858075515:AAHkJvKomSWgS6V4-qx4b76dCW04IcOYutE"
OPENAI_API_KEY = "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"

# 🔥 Використовуємо OpenAI Projects API (правильний URL!)
client = openai.OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.openai.com/v1"
)

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
        response = client.chat.completions.create(
            model="gpt-4o-2024-11-20",  # ✅ Використовуємо правильний формат
            messages=[{"role": "user", "content": message.text}]
        )
        reply = response.choices[0].message.content
        await message.reply(reply)
    except Exception as e:
        logging.error(f"Помилка OpenAI API: {e}")
        await message.reply("Виникла помилка. Спробуй ще раз!")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
