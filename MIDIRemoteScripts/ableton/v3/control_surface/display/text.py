# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\display\text.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 2792 bytes
from __future__ import absolute_import, print_function, unicode_literals
from collections import UserString
from enum import Enum, auto
from typing import Callable, Optional, Tuple, Union
from ...base import as_ascii
from ..elements import adjust_string

class Text(UserString):

    class ContentWidth:
        pass

    class Justification(Enum):
        LEFT = auto()
        CENTER = auto()
        RIGHT = auto()
        NONE = auto()

    def __init__(self, string='', justification=None, max_width=None):
        super().__init__(string)
        self.justification = justification
        self.max_width = max_width

    def as_ascii(self, adjust_string_fn: Callable[([str, int], str)]=adjust_string) -> Tuple[(int, ...)]:
        return tuple(as_ascii(self.as_string(adjust_string_fn=adjust_string_fn)))

    def as_string(self, adjust_string_fn: Callable[([str, int], str)]=adjust_string) -> str:
        max_width = self.max_width = len(self) if (self.max_width is None or isinstance(self.max_width, Text.ContentWidth)) else (self.max_width)
        justify = self.justification or Text.Justification.LEFT
        formatted = adjust_string_fn(str(self), max_width).rstrip() if self else ""
        if justify == Text.Justification.LEFT:
            return formatted.ljust(max_width)
        if justify == Text.Justification.CENTER:
            return formatted.center(max_width)
        if justify == Text.Justification.RIGHT:
            return formatted.rjust(max_width)
        return formatted

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/display/text.pyc
