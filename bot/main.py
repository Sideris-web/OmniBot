import logging

from plugin_manager import PluginManager
from openai_helper import OpenAIHelper, default_max_tokens, are_functions_available
from telegram_bot import ChatGPTTelegramBot


def main():
    # 🔥 Пряме встановлення API-ключів
    TELEGRAM_BOT_TOKEN = "7858075515:AAHkJvKomSWgS6V4-qx4b76dCW04IcOYutE"  # 🔥 Замініть на свій токен
    OPENAI_API_KEY = "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"  # 🔥 Замініть на свій OpenAI ключ

    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)

    # Setup configurations
    model = "gpt-4o"
    functions_available = are_functions_available(model=model)
    max_tokens_default = default_max_tokens(model=model)

    openai_config = {
        "api_key": OPENAI_API_KEY,
        "show_usage": False,
        "stream": True,
        "max_history_size": 15,
        "max_conversation_age_minutes": 180,
        "assistant_prompt": "You are a helpful assistant.",
        "max_tokens": max_tokens_default,
        "n_choices": 1,
        "temperature": 1.0,
        "model": model,
        "enable_functions": functions_available,
        "presence_penalty": 0.0,
        "frequency_penalty": 0.0,
        "bot_language": "en",
    }

    telegram_config = {
        "token": TELEGRAM_BOT_TOKEN,
        "admin_user_ids": "-",
        "allowed_user_ids": "*",
        "enable_quoting": True,
        "enable_image_generation": True,
        "enable_transcription": True,
        "enable_vision": True,
        "enable_tts_generation": True,
        "budget_period": "monthly",
        "user_budgets": "*",
        "guest_budget": 100.0,
        "stream": True,
        "proxy": None,
        "bot_language": "en",
    }

    plugin_config = {"plugins": []}

    # Setup and run ChatGPT and Telegram bot
    plugin_manager = PluginManager(config=plugin_config)
    openai_helper = OpenAIHelper(config=openai_config, plugin_manager=plugin_manager)
    telegram_bot = ChatGPTTelegramBot(config=telegram_config, openai=openai_helper)
    telegram_bot.run()


if __name__ == "__main__":
    main()
