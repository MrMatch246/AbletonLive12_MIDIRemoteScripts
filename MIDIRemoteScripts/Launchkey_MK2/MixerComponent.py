# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK2\MixerComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 354 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.MixerComponent import MixerComponent as MixerComponentBase

class MixerComponent(MixerComponentBase):

    def set_volume_control(self, control):
        self._selected_strip.set_volume_control(control)

# okay decompiling ./MIDIRemoteScripts/Launchkey_MK2/MixerComponent.pyc
