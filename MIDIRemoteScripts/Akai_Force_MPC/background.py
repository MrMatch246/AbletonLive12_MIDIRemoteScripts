# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Akai_Force_MPC\background.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 455 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import BackgroundComponent

class LightingBackgroundComponent(BackgroundComponent):

    def _clear_control(self, name, control):
        super(LightingBackgroundComponent, self)._clear_control(name, control)
        if control:
            control.set_light("Background.On")

# okay decompiling ./MIDIRemoteScripts/Akai_Force_MPC/background.pyc
