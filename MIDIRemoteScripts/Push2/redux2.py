# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\redux2.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 861 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import EventObject
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name
from .device_options import DeviceOnOffOption

class Redux2DeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(Redux2DeviceDecorator, self).__init__)(*a, **k)
        self.postFilter_on_option = DeviceOnOffOption(name="Post-Filter",
          property_host=(get_parameter_by_name(self, "Post-Filter On")))
        self.register_disconnectables(self.options)

    @property
    def options(self):
        return (
         self.postFilter_on_option,)

    @property
    def parameters(self):
        return tuple(self._live_object.parameters)

# okay decompiling ./MIDIRemoteScripts/Push2/redux2.pyc
