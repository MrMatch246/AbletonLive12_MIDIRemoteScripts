# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ATOM\drum_group.py
# Size of source mod 2**32: 966 bytes
from __future__ import absolute_import, division, print_function, unicode_literals
from ableton.v3.control_surface.components import DrumGroupComponent as DrumGroupComponentBase
from .note_pad import NotePadMixin
COMPLETE_QUADRANTS_RANGE = range(4, 116)
MAX_QUADRANT_INDEX = 7
NUM_PADS = 16
PADS_PER_ROW = 4

class DrumGroupComponent(NotePadMixin, DrumGroupComponentBase):

    @staticmethod
    def _filled_color(pad):
        pad_quadrant = MAX_QUADRANT_INDEX
        if pad.note in COMPLETE_QUADRANTS_RANGE:
            pad_quadrant = (pad.note - PADS_PER_ROW) // NUM_PADS
        return "DrumGroup.PadQuadrant{}".format(pad_quadrant)

# okay decompiling ./MIDIRemoteScripts/ATOM/drum_group.pyc
