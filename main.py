import os
import telebot
import openai

# Отримуємо токени з перемінних середовища
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Підключаємо API OpenAI
openai.api_key = OPENAI_API_KEY

# Запускаємо Telegram бота
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
