# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\mode.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 626 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import InputControl
from ableton.v2.control_surface.mode import ModesComponent as ModesComponentBase

class ModesComponent(ModesComponentBase):
    __events__ = ('mode_byte', )
    mode_selection_control = InputControl()

    @mode_selection_control.value
    def mode_selection_control(self, value, _):
        modes = self.modes
        if value < len(modes):
            self.selected_mode = modes[value]
            self.notify_mode_byte(value)

# okay decompiling ./MIDIRemoteScripts/novation/mode.pyc
