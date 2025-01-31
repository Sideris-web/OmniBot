import os
import telebot
import openai

# Отримуємо токени з перемінних середовища
import os
from dotenv import load_dotenv

load_dotenv()  # Завантажує змінні середовища

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

print(f"🔹 Завантажено TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN}")
print(f"🔹 Завантажено OPENAI_API_KEY: {OPENAI_API_KEY}")

# Підключаємо API OpenAI
openai.api_key = OPENAI_API_KEY

# Запускаємо Telegram бота
print(f"🔹 TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN}")
print(f"🔹 OPENAI_API_KEY: {OPENAI_API_KEY}")
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": message.text}]
    )
    bot.reply_to(message, response.choices[0].message.content)

print("✅ OmniBot запущено!")
bot.polling()
