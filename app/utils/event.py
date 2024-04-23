from .abstractions import EventType, ServerType


class Event(EventType):
    def __init__(self, type: str) -> None:
        super().__init__()

        self.type = type

        self.__result = None
        self.__is_result_setted = False

    def done(self) -> bool:
        return super().done() or self.__is_result_setted

    def set_result(self, result: object) -> None:
        self.__result = result
        self.__is_result_setted = True

    def apply_result(self) -> None:
        super().set_result(self.__result)

    @classmethod
    def set_server(cls, server: ServerType) -> None:
        cls.server = server
