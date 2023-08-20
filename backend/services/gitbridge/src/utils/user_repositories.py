from abc import ABC, abstractmethod
from src.schemas.user import User
from uuid import UUID
from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from loguru import logger

mock_user = User(
    id=UUID("6f7906f6-86ba-4f08-aa49-86235db8b011"),
    secret_key="test_secret",
)


class IUserRepo(ABC):
    @abstractmethod
    async def get_user(self, user_id: UUID) -> User:
        ...


class UserRepository(IUserRepo):
    async def get_user(self, user_id: UUID) -> User:
        logger.debug("Getting user from UserAPI service...")
        return mock_user


@lru_cache(maxsize=1)
def get_user_repository() -> IUserRepo:
    return UserRepository()


DUserRepo = Annotated[IUserRepo, Depends(get_user_repository)]
