import asyncio as aio

from ..utils import Event, Dispatcher, ServerType, load_plugins
from ..events.server.start_event import ServerStartEvent
from ..events.server.stop_event import ServerStopEvent


class Server(Dispatcher, ServerType):
    def __init__(self) -> None:
        super().__init__()

        self.tasks = []

        Event.set_server(self)

        load_plugins(self)

    async def start(self) -> None:
        await aio.gather(*await self.emit(ServerStartEvent()))

        try:
            await aio.gather(*self.tasks)
        finally:
            await aio.gather(*await self.emit(ServerStopEvent()))
