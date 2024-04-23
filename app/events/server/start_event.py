from ...utils import Event


class ServerStartEvent(Event):
    def __init__(self) -> None:
        super().__init__("server.start")
