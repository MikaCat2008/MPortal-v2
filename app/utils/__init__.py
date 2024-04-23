import os, importlib as imp

import quart as q

from .abstractions import *
from .event import Event
from .plugin import Plugin
from .listener import Listener
from .dispatcher import Dispatcher

PLUGINS_PATH = "app\\plugins"


def add_plugin(server: ServerType, plugin: PluginType) -> None:
    for listeners in plugin.listeners.values():        
        for listener in listeners:
            server.add_listener(listener)

    server.base_listeners |= plugin.base_listeners


def find_plugins() -> list[type[PluginType]]:
    plugins = []

    plugins_module = imp.import_module(".", PLUGINS_PATH.replace("\\", "."))

    for plugin in plugins_module.__plugins__:        
        plugins.append(plugin)

    return plugins


def load_plugins(server: ServerType) -> None:
    for plugin in find_plugins():
        add_plugin(server, plugin(server))
