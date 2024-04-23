from ...utils import Plugin, Listener, ServerType
from ...events.server import ServerStartEvent, ServerStopEvent


class ServerPlugin(Plugin):
    def __init__(self, server: ServerType) -> None:
        super().__init__(server)

        self.add_listener(Listener.on("server.start")(self.on_server_start), base=True)
        self.add_listener(Listener.on("server.stop")(self.on_server_start), base=True)

    async def on_server_start(self, event: ServerStartEvent) -> None:
        event.set_result(None)

    async def on_server_stop(self, event: ServerStopEvent) -> None:
        event.set_result(None)
