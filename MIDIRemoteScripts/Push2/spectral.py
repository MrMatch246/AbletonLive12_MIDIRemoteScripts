# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\spectral.py
# Size of source mod 2**32: 1706 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import EventObject
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name
from .device_options import DeviceOnOffOption, DeviceSwitchOption

class SpectralDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(SpectralDeviceDecorator, self).__init__)(*a, **k)
        self.freeze_option = DeviceOnOffOption(name="Frozen",
          property_host=(get_parameter_by_name(self, "Frozen")))
        self.unit_option = DeviceSwitchOption(name="Unit",
          parameter=(get_parameter_by_name(self, "Unit")),
          labels=[
         "ms", "Notes"])
        self.delay_unit_option = DeviceSwitchOption(name="Delay Dly. Unit",
          parameter=(get_parameter_by_name(self, "Delay Dly. Unit")),
          labels=[
         "ms","Notes","16th","Tr","Dt"])
        self.fade_type_option = DeviceSwitchOption(name="Fade Type",
          parameter=(get_parameter_by_name(self, "Fade Type")),
          labels=[
         "X-Fade", "Env"])
        self.register_disconnectables(self.options)

    @property
    def options(self):
        return (
         self.freeze_option,
         self.unit_option,
         self.delay_unit_option,
         self.fade_type_option)

    @property
    def parameters(self):
        return tuple(self._live_object.parameters) + self._additional_parameters

# okay decompiling ./MIDIRemoteScripts/Push2/spectral.pyc
