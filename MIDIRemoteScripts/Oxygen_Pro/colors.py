# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Oxygen_Pro\colors.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 395 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import Color

class Basic:
    ON = Color(127)
    OFF = Color(0)


class Rgb:
    GREEN = Color(12)
    GREEN_BLINK = Color(76)
    RED = Color(3)
    RED_BLINK = Color(67)
    AMBER = Color(11)
    WHITE = Color(63)

# okay decompiling ./MIDIRemoteScripts/Oxygen_Pro/colors.pyc