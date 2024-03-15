# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\display\type_decl.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1109 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import Any, Callable, NamedTuple, TypeVar
from .state import State

class Event(NamedTuple):
    name: str
    origin: Any
    value: Any


INIT_EVENT = Event(name="init", origin=None, value=None)
DISCONNECT_EVENT = Event(name="disconnect", origin=None, value=None)
ContentType = TypeVar("ContentType")
Render = Callable[([State], ContentType)]

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/display/type_decl.pyc
