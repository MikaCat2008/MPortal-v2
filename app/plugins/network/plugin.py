import typing as t, functools as ft

import quart as q

from ...utils import Plugin, Listener, ServerType
from ...events.server.start_event import ServerStartEvent
from .request import Request


class NetworkPlugin(Plugin):
    def __init__(self, server: ServerType) -> None:
        super().__init__(server)

        self.app = q.Quart(__name__)

        self.add_listener(Listener.on("server.start")(self.server_start))

    async def app_task(self) -> None:
        @self.app.before_request
        async def before_request() -> q.Response:
            request = Request()
            
            await self.emit(request)

            return await request

        await self.app.run_task("localhost", 8080)

    async def server_start(self, event: ServerStartEvent) -> None:
        self.server.tasks.append(self.app_task())