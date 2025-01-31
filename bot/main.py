import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import openai

# 🔥 ВСТАНОВЛЮЄМО КЛЮЧІ НАПРЯМУ
TELEGRAM_BOT_TOKEN = "7858075515:AAHkJvKomSWgS6V4-qx4b76dCW04IcOYutE"
OPENAI_API_KEY = "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"
ORGANIZATION_ID = "org-aljpAbtAOS2HOA91HxWLPd5f"  # 📌 Додай сюди свій ID організації

# 🔥 Переконуємось, що ключі не пусті
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не вказано!")
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY не вказано!")

# 🔥 Використовуємо OpenAI Projects API (з правильним URL!)
client = openai.OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.openai.com/v1",
    organization=ORGANIZATION_ID
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
            model="gpt-4o-2024-11-20",  # ✅ Використовуємо модель, яка дозволена
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
