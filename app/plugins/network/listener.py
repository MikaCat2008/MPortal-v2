import typing as t

from ...utils import Listener
from .abstractions import NetworkListenerType


class NetworkListener(Listener, NetworkListenerType):
    listeners: list[NetworkListenerType] = []

    @classmethod
    def route(cls, rule: str, methods: list[str] = ["GET"]) -> t.Callable:
        def handler(function: t.Coroutine) -> NetworkListenerType:
            return cls(rule, function, methods=methods)

        return handler
