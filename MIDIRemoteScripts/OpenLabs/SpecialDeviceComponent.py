# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\OpenLabs\SpecialDeviceComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1055 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
import _Framework.DeviceComponent as DeviceComponent

class SpecialDeviceComponent(DeviceComponent):

    def __init__(self):
        DeviceComponent.__init__(self)

    def _device_parameters_to_map(self):
        return self._device.parameters[1[:None]]

# okay decompiling ./MIDIRemoteScripts/OpenLabs/SpecialDeviceComponent.pyc
