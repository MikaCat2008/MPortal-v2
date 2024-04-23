from .server import ServerPlugin
from .network import NetworkPlugin
from .auth import AuthPlugin

__plugins__ = [
    ServerPlugin,
    NetworkPlugin,
    AuthPlugin
]
