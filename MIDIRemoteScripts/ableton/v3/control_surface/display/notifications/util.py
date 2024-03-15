# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\display\notifications\util.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 597 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from typing_extensions import LiteralString
else:
    LiteralString = str

def toggle_text_generator(format_string: "LiteralString") -> "Callable[[bool], str]":

    def notification_fn(is_on):
        return format_string.format("on" if is_on else "off")

    return notification_fn

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/display/notifications/util.pyc
