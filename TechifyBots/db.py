from typing import Any
from config import DB_URI, DB_NAME
from motor import motor_asyncio
from pymongo import ReturnDocument
from pymongo.errors import DuplicateKeyError
from bson import ObjectId

client = motor_asyncio.AsyncIOMotorClient(DB_URI)
db = client[DB_NAME]

class Techifybots:
    def __init__(self):
        self.users = db["users"]
        self.cache: dict[int, dict[str, Any]] = {}

    async def add_user(self, user_id: int, name: str) -> dict[str, Any] | None:
        try:
            user = {"user_id": int(user_id), "name": name}
            saved = await self.users.find_one_and_update(
                {"user_id": user["user_id"]},
                {"$set": user},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )
            if saved:
                self.cache[user["user_id"]] = saved
            return saved
        except DuplicateKeyError:
            existing = await self.users.find_one({"user_id": int(user_id)})
            if existing:
                self.cache[int(user_id)] = existing
            return existing
        except Exception as e:
            print("Error in add_user:", e)
            return None

    async def get_user(self, user_id: int) -> dict[str, Any] | None:
        try:
            if user_id in self.cache:
                return self.cache[user_id]
            user = await self.users.find_one({"user_id": int(user_id)})
            if user:
                self.cache[user_id] = user
            return user
        except Exception as e:
            print("Error in get_user:", e)
            return None

    async def get_all_users(self) -> list[dict[str, Any]]:
        try:
            users: list[dict[str, Any]] = []
            async for user in self.users.find():
                users.append(user)
            return users
        except Exception as e:
            print("Error in get_all_users:", e)
            return []

    async def delete_user(self, identifier: int | str | ObjectId) -> bool:
        try:
            query = {}
            if isinstance(identifier, int):
                query = {"user_id": identifier}
                self.cache.pop(identifier, None)
            elif isinstance(identifier, (str, ObjectId)):
                query = {"_id": ObjectId(identifier)} if isinstance(identifier, str) else {"_id": identifier}
                doc = await self.users.find_one(query)
                if doc and "user_id" in doc:
                    self.cache.pop(int(doc["user_id"]), None)
            else:
                return False
            result = await self.users.delete_one(query)
            return result.deleted_count > 0
        except Exception as e:
            print("Error in delete_user:", e)
            return False

tb = Techifybots()