import quart as q

from ...utils import Event
from .abstractions import Type, RequestType


class Request(Event, RequestType):
    def __init__(self) -> None:
        super().__init__(q.request.path)

    def arg(self, name: str, type: Type = str) -> Type:
        return type(q.request.args.get(name))
    
    def cookie(self, name: str, type: Type = str) -> Type:
        return type(q.request.cookies.get(name))
