# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\fixed_radio_button_group.py
# Size of source mod 2**32: 1151 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import RadioButtonGroup

class FixedRadioButtonGroup(RadioButtonGroup):

    def __init__(self, control_count, *a, **k):
        (super(FixedRadioButtonGroup, self).__init__)(a, control_count=control_count, **k)

    class State(RadioButtonGroup.State):

        @property
        def active_control_count(self):
            return self._active_control_count

        @active_control_count.setter
        def active_control_count(self, control_count):
            self._active_control_count = control_count
            for (index, control) in enumerate(self._controls):
                control._get_state(self._manager).enabled = index < control_count

# okay decompiling ./MIDIRemoteScripts/novation/fixed_radio_button_group.pyc
