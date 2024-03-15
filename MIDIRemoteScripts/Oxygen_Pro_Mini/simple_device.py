# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Oxygen_Pro_Mini\simple_device.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1197 bytes
from __future__ import absolute_import, print_function, unicode_literals
from novation.simple_device import SimpleDeviceParameterComponent as SimpleDeviceParameterComponentBase
NUM_CONTROLS = 4

class SimpleDeviceParameterComponent(SimpleDeviceParameterComponentBase):

    def __init__(self, *a, **k):
        (super(SimpleDeviceParameterComponent, self).__init__)(*a, **k)
        self._parameter_offset = 0

    def toggle_parameter_offset(self):
        self._parameter_offset = NUM_CONTROLS - self._parameter_offset
        self.update()

    @SimpleDeviceParameterComponentBase.selected_bank.getter
    def selected_bank(self):
        bank = self._banks[0] or []
        if self._parameter_offset:
            if len(bank) > self._parameter_offset:
                offset_bank = bank[self._parameter_offset[:None]]
                if any(offset_bank):
                    return offset_bank
        return bank

# okay decompiling ./MIDIRemoteScripts/Oxygen_Pro_Mini/simple_device.pyc
