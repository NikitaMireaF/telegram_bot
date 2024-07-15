from aiogram.filters import BaseFilter
from aiogram.types import Message
admins_id = [6799017808]


class Admin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        id = message.from_user.id
        if id in admins_id:
            return True
        return False
