import asyncpg
from typing import Optional

class Database:
    def __init__(self):
        self.pool: Optional[asyncpg.Pool] = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            host="localhost",
            port=5432,
            database="quiz_bot",
            user="postgres",
            password="password",
            min_size=1,
            max_size=10
        )
        print("Подключение к БД установлено.")

    async def create_user(self, telegram_id: int):
        async with self.pool.acquire() as connection:
            await connection.execute(
                """INSERT INTO users (telegram_id)
                VALUES ($1)
                ON CONFLICT (telegram_id) DO NOTHING""",
                telegram_id
            )

    async def get_user(self, telegram_id: int) -> Optional[asyncpg.Record]:
        async with self.pool.acquire() as connection:
            await connection.execute(
                "SELECT * FROM users WHERE telegram_id = $1",
                telegram_id
            )

    async def close(self):
        if (self.pool):
            self.pool.close()