# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Pro\SpecialDeviceComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 947 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.DeviceComponent as DeviceComponent
from .consts import DEVICE_MAP_CHANNEL, FADER_TYPE_STANDARD

class SpecialDeviceComponent(DeviceComponent):

    def set_parameter_controls(self, controls):
        if controls:
            for control in controls:
                control.set_channel(DEVICE_MAP_CHANNEL)
                control.set_light_and_type("Device.On", FADER_TYPE_STANDARD)

        super(SpecialDeviceComponent, self).set_parameter_controls(controls)

    def _update_parameter_controls(self):
        if self._parameter_controls is not None:
            for control in self._parameter_controls:
                control.update()

    def update(self):
        super(SpecialDeviceComponent, self).update()
        if self.is_enabled():
            self._update_parameter_controls()

# okay decompiling ./MIDIRemoteScripts/Launchpad_Pro/SpecialDeviceComponent.pyc
