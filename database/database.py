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
            result = await connection.execute(
                """INSERT INTO users (telegram_id)
                VALUES ($1)
                ON CONFLICT (telegram_id) DO NOTHING""",
                telegram_id
            )
            return result

    async def get_user(self, telegram_id: int) -> Optional[asyncpg.Record]:
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(
                "SELECT * FROM users WHERE telegram_id = $1",
                telegram_id
            )

    async def change_difficulty(self, telegram_id: int, difficulty: str):
        async with self.pool.acquire() as connection:
            result = await connection.execute(
                "UPDATE users SET difficulty = $1 WHERE telegram_id = $2",
                difficulty, telegram_id
            )
            return result

    async def change_category(self, telegram_id: int, category: str):
        async with self.pool.acquire() as connection:
            result = await connection.execute(
                "UPDATE users SET theme = $1 WHERE telegram_id = $2",
                category, telegram_id
            )
            return result

    async def increment_games(self, telegram_id: int):
        async with self.pool.acquire() as connection:
            result = await connection.execute(
                "UPDATE users SET games = games + 1 WHERE telegram_id = $1",
                telegram_id
            )
            return result

    async def increment_wins(self, telegram_id: int):
        async with self.pool.acquire() as connection:
            result = await connection.execute(
                "UPDATE users SET wins = wins + 1 WHERE telegram_id = $1",
                telegram_id
            )
            return result

    async def get_stats(self, telegram_id: int):
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(
                "SELECT games, wins FROM users WHERE telegram_id = $1",
                telegram_id
            )

    async def get_difficulty(self, telegram_id: int):
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(
                "SELECT difficulty FROM users WHERE telegram_id = $1",
                telegram_id
            )

    async def get_category(self, telegram_id: int):
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(
                "SELECT theme FROM users WHERE telegram_id = $1",
                telegram_id
            )

    async def close(self):
        if (self.pool):
            await self.pool.close()