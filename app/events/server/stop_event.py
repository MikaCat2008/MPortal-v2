from ...utils import Event


class ServerStopEvent(Event):
    def __init__(self) -> None:
        super().__init__("server.stop")
