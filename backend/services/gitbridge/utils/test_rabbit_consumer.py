import asyncio

from aio_pika import ExchangeType, connect
from aio_pika.abc import AbstractIncomingMessage
from src.settings.application import get_app_settings

settings = get_app_settings()


async def on_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        print(f"[x] {message.body!r}")


async def main() -> None:
    # Perform connection
    connection = await connect(settings.rabbit_dsn)

    async with connection:
        # Creating a channel
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        task_exchange = await channel.get_exchange(settings.rabbit_exchange)

        # Declaring queue
        queue = await channel.declare_queue("test_queue", exclusive=True)

        # Binding the queue to the exchange
        await queue.bind(task_exchange)

        # Start listening the queue
        await queue.consume(on_message)

        print(" [*] Waiting for logs. To exit press CTRL+C")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
