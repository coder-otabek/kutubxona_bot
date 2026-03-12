import aiosqlite

class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    async def create_table(self):
        async with aiosqlite.connect(self.db_path) as db:
            # ✅ Foydalanuvchilar jadvali (FAqat username qo‘shildi)
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id BIGINT PRIMARY KEY,
                    name TEXT,
                    username TEXT,
                    email TEXT,
                    contact TEXT
                )
            """)

            # ✅ Guruhlar jadvali (o‘sha holatda)
            await db.execute("""
                CREATE TABLE IF NOT EXISTS groups (
                    group_id BIGINT PRIMARY KEY,
                    title TEXT,
                    username TEXT,
                    link TEXT
                )
            """)
            await db.commit()

        # ✅ eski DB bo‘lsa, groups jadvaliga column qo‘shib ketadi
        await self.add_group_columns()

        # ✅ eski DB bo‘lsa, users jadvaliga username column qo‘shib ketadi
        await self.add_user_username_column()

    async def add_group_columns(self):
        """
        Eski bazalarda groups jadvalida username/link bo‘lmasa qo‘shib beradi.
        """
        async with aiosqlite.connect(self.db_path) as db:
            try:
                await db.execute("ALTER TABLE groups ADD COLUMN username TEXT")
                await db.commit()
            except Exception:
                pass

            try:
                await db.execute("ALTER TABLE groups ADD COLUMN link TEXT")
                await db.commit()
            except Exception:
                pass

    async def add_user_username_column(self):
        """
        Eski bazalarda users jadvalida username column bo‘lmasa qo‘shib beradi.
        """
        async with aiosqlite.connect(self.db_path) as db:
            try:
                await db.execute("ALTER TABLE users ADD COLUMN username TEXT")
                await db.commit()
            except Exception:
                pass

    # ====== users metodlari ======
    async def get_user(self, user_id):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) as cursor:
                return await cursor.fetchone()

    async def count_users(self):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT COUNT(*) FROM users") as cursor:
                result = await cursor.fetchone()
                return result[0] if result else 0
    async def add_user(self, user_id, name, username=None):
        async with aiosqlite.connect(self.db_path) as db:
            # ✅ username ham saqlanadi
            await db.execute(
                "INSERT OR IGNORE INTO users (user_id, name, username) VALUES (?, ?, ?)",
                (user_id, name, username)
            )
            # ✅ bor bo‘lsa ham name/username yangilanib turadi
            await db.execute(
                "UPDATE users SET name = ?, username = ? WHERE user_id = ?",
                (name, username, user_id)
            )
            await db.commit()

    async def update_user_name(self, user_id, name):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id))
            await db.commit()

    async def get_all_users(self):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT * FROM users") as cursor:
                return await cursor.fetchall()

    # ====== groups metodlari ======
    async def add_group(self, group_id, title, username=None, link=None):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "INSERT OR IGNORE INTO groups (group_id, title, username, link) VALUES (?, ?, ?, ?)",
                (group_id, title, username, link)
            )
            # agar oldin bor bo‘lsa ham title/link yangilanib turadi
            await db.execute(
                "UPDATE groups SET title = ?, username = ?, link = ? WHERE group_id = ?",
                (title, username, link, group_id)
            )
            await db.commit()

    async def get_all_groups(self):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT * FROM groups") as cursor:
                return await cursor.fetchall()

    async def update_user_info(self, user_id: int, name: str = None, email: str = None, contact: str = None):
        """
        users jadvalidagi name/email/contact ni yangilaydi.
        Qaysi maydon berilsa, o‘sha update bo‘ladi.
        """
        fields = []
        values = []

        if name is not None:
            fields.append("name = ?")
            values.append(name)

        if email is not None:
            fields.append("email = ?")
            values.append(email)

        if contact is not None:
            fields.append("contact = ?")
            values.append(contact)

        if not fields:
            return  # update qiladigan narsa yo‘q

        values.append(user_id)

        sql = f"UPDATE users SET {', '.join(fields)} WHERE user_id = ?"

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(sql, tuple(values))
            await db.commit()

    async def count_groups(self):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT COUNT(*) FROM groups") as cursor:
                result = await cursor.fetchone()
                return result[0] if result else 0