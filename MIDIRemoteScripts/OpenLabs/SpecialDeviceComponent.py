# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\OpenLabs\SpecialDeviceComponent.py
# Size of source mod 2**32: 1055 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.DeviceComponent import DeviceComponent as DeviceComponent

class SpecialDeviceComponent(DeviceComponent):

    def __init__(self):
        DeviceComponent.__init__(self)

    def _device_parameters_to_map(self):
        return self._device.parameters[1:]

# okay decompiling ./MIDIRemoteScripts/OpenLabs/SpecialDeviceComponent.pyc
