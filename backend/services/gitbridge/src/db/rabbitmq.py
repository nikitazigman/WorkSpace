import aio_pika
from aio_pika.robust_connection import AbstractRobustConnection
from aio_pika.exchange import AbstractExchange
from typing import Annotated
from collections.abc import AsyncGenerator
from src.settings.application import get_app_settings
from fastapi import Depends


settings = get_app_settings()

connection: None | AbstractRobustConnection = None


async def establish_connection():
    global connection
    connection = await aio_pika.connect_robust(settings.rabbit_dsn)


async def close_connection():
    global connection
    await connection.close()


async def declare_exchange() -> None:
    global connection

    if connection is None:
        raise Exception("Connection is not established")

    async with connection.channel() as channel:
        await channel.declare_exchange(
            settings.rabbit_exchange, type=aio_pika.ExchangeType.FANOUT
        )


async def get_exchange() -> AsyncGenerator[AbstractExchange, None]:
    if connection is None:
        raise Exception("Connection is not established")

    async with connection.channel() as channel:
        yield await channel.get_exchange(settings.rabbit_exchange)


DExchange = Annotated[AbstractExchange, Depends(get_exchange)]
