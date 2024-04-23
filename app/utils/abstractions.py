from __future__ import annotations

import asyncio as aio, typing as t
from abc import ABC, abstractmethod
from collections import defaultdict

Type = t.TypeVar("Type")


class EventType(aio.Future):
    type: str
    server: ServerType
    __result: object
    __is_result_setted: bool

    @abstractmethod
    def apply_result(self) -> None:
        ...

    @classmethod
    @abstractmethod
    def set_server(cls, server: ServerType) -> None:
        ...


class ListenerType(ABC):
    type: str
    options: dict
    function: t.Coroutine

    listeners: list[ListenerType]


class DispatcherType(ABC):
    listeners: defaultdict[str, list[ListenerType]]
    base_listeners: dict[str, ListenerType]

    @abstractmethod
    def add_listener(self, listener: ListenerType) -> None:
        ...

    @abstractmethod
    def emit(self, event: EventType) -> EventType:
        ...



class ServerType(DispatcherType):
    tasks: list[t.Coroutine]

    @abstractmethod
    def start(self) -> None:
        ...


class PluginType(DispatcherType):
    ...
