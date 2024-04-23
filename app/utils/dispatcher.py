import asyncio as aio
from collections import defaultdict

from .abstractions import EventType, ListenerType, DispatcherType


class Dispatcher(DispatcherType):
    def __init__(self) -> None:
        self.listeners = defaultdict(list)
        self.base_listeners = {}
    
    def add_listener(self, listener: ListenerType, base: bool = False) -> None:
        self.listeners[listener.type].append(listener)
        
        if base:
            self.base_listeners[listener.type] = listener

    async def emit(self, event: EventType) -> EventType:
        listeners = self.listeners[event.type]
        base_listener = self.base_listeners.get(event.type)

        for listener in listeners:
            await listener(event)

        if not event.done() and base_listener:
            await base_listener(event)

        event.apply_result()

        return event
