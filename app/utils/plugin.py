from .abstractions import EventType, PluginType, ServerType
from .dispatcher import Dispatcher


class Plugin(Dispatcher, PluginType):
    def __init__(self, server: ServerType) -> None:
        super().__init__()

        self.server = server

    def emit(self, event: EventType) -> EventType:
        return self.server.emit(event)
