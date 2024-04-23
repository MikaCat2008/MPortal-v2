from __future__ import annotations

import typing as t
from abc import abstractmethod

from ...utils import EventType, ListenerType

Type = t.TypeVar("Type")


class RequestType(EventType):
    ...


class NetworkListenerType(ListenerType):
    listeners: list[NetworkListenerType]

    @classmethod
    @abstractmethod
    def route(self, rule: str, methods: list[str] = ["GET"]) -> t.Callable:
        ...
