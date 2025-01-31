import logging
import requests
import json
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔥 ВСТАНОВЛЮЄМО КЛЮЧІ НАПРЯМУ
TELEGRAM_BOT_TOKEN = "7858075515:AAHkJvKomSWgS6V4-qx4b76dCW04IcOYutE"
OPENAI_API_KEY = "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"
OPENAI_ORG = "org-aljpAbtAOS2HOA91HxWLPd5f"
OPENAI_PROJECT = "proj_kIBGPch0Rb1S16SEVGmKP9jf"

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
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
            "OpenAI-Organization": OPENAI_ORG,
            "OpenAI-Project": OPENAI_PROJECT
        }
        
        data = {
            "model": "gpt-4o-2024-11-20",  # ✅ Використовуємо правильний формат
            "messages": [{"role": "user", "content": message.text}],
            "temperature": 0.7
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", 
                                 headers=headers, 
                                 data=json.dumps(data))

        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            await message.reply(reply)
        else:
            logging.error(f"Помилка OpenAI API: {response.status_code}, {response.text}")
            await message.reply("❌ Виникла помилка OpenAI API. Спробуй ще раз!")

    except Exception as e:
        logging.error(f"Помилка OpenAI API: {e}")
        await message.reply("❌ Виникла помилка. Спробуй ще раз!")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
