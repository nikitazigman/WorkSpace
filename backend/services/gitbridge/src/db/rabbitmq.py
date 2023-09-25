from abc import ABC, abstractmethod
from src.schemas.tasks import Task
from functools import lru_cache


class IPublisher(ABC):
    @abstractmethod
    async def publish(self, message: Task) -> None:
        ...


class RabbitMQPublisher(IPublisher):
    async def publish(self, message: Task) -> None:
        ...


@lru_cache(maxsize=1)
def get_publisher() -> IPublisher:
    return RabbitMQPublisher()
