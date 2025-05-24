from motor.motor_asyncio import AsyncIOMotorClient
from ..config import settings
from ..models.user import UserInDB

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

async def get_user(email: str) -> UserInDB | None:
    user = await db.users.find_one({"email": email})
    if user:
        return UserInDB(**user)
    return None

async def create_user(user: UserCreate) -> UserInDB:
    hashed_password = get_password_hash(user.password)
    db_user = {
        "email": user.email,
        "name": user.name,
        "hashed_password": hashed_password,
        "is_admin": user.is_admin,
        "created_at": datetime.utcnow()
    }
    result = await db.users.insert_one(db_user)
    return UserInDB(**db_user, id=str(result.inserted_id))
