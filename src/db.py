import aiosqlite
import os
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "gfx_play.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                telegram_id INTEGER UNIQUE,
                stars INTEGER DEFAULT 0,
                lang TEXT
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                item_id TEXT,
                quantity INTEGER DEFAULT 1
            )
        ''')
        await db.commit()

if __name__ == "__main__":
    import asyncio
    asyncio.run(init_db())
