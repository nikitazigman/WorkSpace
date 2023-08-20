from abc import ABC, abstractmethod
from src.schemas.tasks import Task
from typing import Annotated
from fastapi import Depends
from loguru import logger
from src.db.rabbitmq import DExchange
from aio_pika.exchange import AbstractExchange
from aio_pika.message import Message
from uuid import uuid4


class IPublisher(ABC):
    @abstractmethod
    async def publish(self, message: Task) -> None:
        ...


class RabbitMQPublisher(IPublisher):
    def __init__(self, exchange: AbstractExchange) -> None:
        self.exchange = exchange

    async def publish(self, message: Task) -> None:
        logger.debug("Publishing message to RabbitMQ...")
        rabbitmq_message = Message(
            body=message.model_dump_json().encode("utf-8"),
            content_type="application/json",
            message_id=str(uuid4()),
        )
        await self.exchange.publish(message=rabbitmq_message, routing_key="")


def get_publisher(exchange: DExchange) -> IPublisher:
    return RabbitMQPublisher(exchange)


DPublisher = Annotated[IPublisher, Depends(get_publisher)]
