# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Oxygen_5th_Gen\oxygen_5th_gen.py
# Size of source mod 2**32: 754 bytes
from __future__ import absolute_import, print_function, unicode_literals
from Oxygen_Pro.oxygen_pro import Oxygen_Pro
LIVE_MODE_BYTE = 0

class Oxygen_5th_Gen(Oxygen_Pro):
    live_mode_byte = LIVE_MODE_BYTE
    has_session_component = False

    def __init__(self, *a, **k):
        (super(Oxygen_5th_Gen, self).__init__)(*a, **k)
        self.set_pad_translations(tuple([tuple([col, row, 36 + (3 - row) * 4 + col, 0]) for row in range(3, -1, -1) for col in iter((range(4)))]))

# okay decompiling ./MIDIRemoteScripts/Oxygen_5th_Gen/oxygen_5th_gen.pyc
