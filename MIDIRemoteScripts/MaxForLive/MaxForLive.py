# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MaxForLive\MaxForLive.py
# Size of source mod 2**32: 2246 bytes

from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import SimpleControlSurface
from ableton.v2.control_surface.input_control_element import MIDI_CC_TYPE, MIDI_NOTE_TYPE, MIDI_PB_TYPE, InputControlElement
STATUS_TO_TYPE = {144:MIDI_NOTE_TYPE, 
 176:MIDI_CC_TYPE,  224:MIDI_PB_TYPE}

class MaxForLive(SimpleControlSurface):

    def __init__(self, *a, **k):
        (super(MaxForLive, self).__init__)(*a, **k)
        self._registered_control_names = []
        self._registered_messages = []

    def register_midi_controlParse error at or near `COME_FROM' instruction at offset 70_0
