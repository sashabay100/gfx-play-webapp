import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from src.config import load_config
from src.i18n import I18n
from dotenv import load_dotenv

load_dotenv()

CONFIG = load_config()
I18N = I18n("locales", CONFIG.get("app", {}).get("default_language", "en"))
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set in environment")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    lang = CONFIG.get("app", {}).get("default_language", "en")
    i18n = I18N.t(lang)
    
    # Create Web App button
    web_app = WebAppInfo(url="https://your-webapp-url.com")  # Замените на ваш URL
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🎮 Open GFX Play", web_app=web_app)]],
        resize_keyboard=True
    )
    
    await message.reply(i18n["welcome_message"], reply_markup=keyboard)

@dp.callback_query()
async def process_callback(callback_query: types.CallbackQuery):
    action = callback_query.data
    lang = CONFIG.get("app", {}).get("default_language", "en")
    i18n = I18N.t(lang)
    
    # Implement different actions based on callback data
    actions = {
        "inventory": "Your inventory is empty",
        "roulette": "Daily spin will be available soon",
        "minecraft": "Minecraft section is under development",
        "giveaways": "No active giveaways at the moment",
        "upgrades": "Upgrade system coming soon",
        "cases": "Case opening system will be available shortly"
    }
    
    await callback_query.answer(actions.get(action, "Feature coming soon"))

async def main():
    try:
        print("Starting bot...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
