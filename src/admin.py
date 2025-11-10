from aiogram import types
from aiogram.filters import CommandStart, Command
from src.config import load_config

CONFIG = load_config()
ADMINS = CONFIG.get("app", {}).get("admins", [])

async def is_admin(user_id: int):
    return user_id in ADMINS

# Admin handler stubs
async def handle_add_case(message: types.Message, case_data: dict):
    # Implement adding a case to configs (or DB) here
    await message.reply("Case added (stub)")
