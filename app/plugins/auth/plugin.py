import quart as q

from ...utils import Plugin, ServerType
from ..network import RequestType, NetworkListener


class AuthPlugin(Plugin):
    def __init__(self, server: ServerType) -> None:
        super().__init__(server)

        self.add_listener(NetworkListener.route("/login")(self.login_page), base=True)

    async def login_page(self, request: RequestType) -> None:
        request.set_result("asd")
