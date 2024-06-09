# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\display\event_signal\core.py
# Size of source mod 2**32: 524 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import Any
from notifications.type_decl import NOTIFICATION_EVENT_ID
from ..state import State
from ..type_decl import Event
from .type_decl import EventSignalFn

def on_notification() -> EventSignalFn[Any]:

    def signal_fn(_: State, event: Event):
        if event.name == NOTIFICATION_EVENT_ID:
            return event.value

    return signal_fn

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/display/event_signal/core.pyc
