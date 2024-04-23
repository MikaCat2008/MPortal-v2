import typing as t

from .abstractions import EventType, ListenerType


class Listener(ListenerType):
    listeners: list[ListenerType] = []

    def __init__(self, type: str, function: t.Coroutine, **options: object) -> None:
        self.type = type
        self.options = options
        self.function = function

        self.listeners.append(self)

    async def __call__(self, event: EventType) -> object:
        return await self.function(event)

    @classmethod
    def on(cls, type: str, **options: object) -> t.Callable:
        def handler(function: t.Coroutine) -> ListenerType:
            return cls(type, function, **options)
        
        return handler

