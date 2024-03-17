# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\BLOCKS\mode.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 499 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import ButtonControl
from ableton.v2.control_surface.mode import ModesComponent as ModesComponentBase

class ModesComponent(ModesComponentBase):
    cycle_mode_button = ButtonControl()

    @cycle_mode_button.pressed
    def cycle_mode_button(self, button):
        if len(self._mode_list):
            self.cycle_mode(1)

# okay decompiling ./MIDIRemoteScripts/BLOCKS/mode.pyc
