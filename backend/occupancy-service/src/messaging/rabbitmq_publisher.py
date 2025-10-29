import asyncio
import json
import aio_pika

class RabbitMQPublisher:
    def __init__(self, url: str, exchange: str = "occupancy", routing_key: str = "occupancy.updated"):
        self.url = url
        self.exchange_name = exchange
        self.routing_key = routing_key
        self._conn: aio_pika.RobustConnection | None = None
        self._ch: aio_pika.abc.AbstractChannel | None = None
        self._ex: aio_pika.abc.AbstractExchange | None = None
        self.loop: asyncio.AbstractEventLoop | None = None  # <— ADĂUGAT

    async def connect(self):
        
        self.loop = asyncio.get_running_loop()
        self._conn = await aio_pika.connect_robust(self.url, loop=self.loop)
        self._ch = await self._conn.channel()
        self._ex = await self._ch.declare_exchange(self.exchange_name, aio_pika.ExchangeType.TOPIC, durable=True)

    async def close(self):
        if self._conn:
            await self._conn.close()

    async def publish(self, message: dict):
        if not self._ex:
            return
        await self._ex.publish(
            aio_pika.Message(body=json.dumps(message).encode("utf-8")),
            routing_key=self.routing_key,
        )

    
    def publish_threadsafe(self, message: dict):
        if not self.loop:
            return
        asyncio.run_coroutine_threadsafe(self.publish(message), self.loop)
