# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mkII\hardware_settings.py
# Size of source mod 2**32: 829 bytes
from __future__ import absolute_import, print_function, unicode_literals
from KeyLab_Essential import sysex
from KeyLab_Essential.hardware_settings import HardwareSettingsComponent as HardwareSettingsComponentBase

class HardwareSettingsComponent(HardwareSettingsComponentBase):

    def __init__(self, *a, **k):
        (super(HardwareSettingsComponent, self).__init__)(*a, **k)
        self._vegas_mode_switch = None

    def set_vegas_mode_switch(self, switch):
        self._vegas_mode_switch = switch

    def set_hardware_live_mode_enabled(self, enable):
        super(HardwareSettingsComponent, self).set_hardware_live_mode_enabled(enable)
        if enable:
            if self._vegas_mode_switch:
                self._vegas_mode_switch.send_value(sysex.OFF_VALUE)

# okay decompiling ./MIDIRemoteScripts/KeyLab_mkII/hardware_settings.pyc
