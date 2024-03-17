# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\roar_decoration.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1023 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .decoration import LiveObjectDecorator
from .internal_parameter import EnumWrappingParameter

class RoarDeviceDecorator(LiveObjectDecorator):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._additional_parameters = self._create_parameters()
        self.register_disconnectables(self._additional_parameters)

    @property
    def parameters(self):
        return tuple(self._live_object.parameters) + self._additional_parameters

    def _create_parameters(self):
        return (
         EnumWrappingParameter(name="Routing",
           parent=self,
           values_host=(self._live_object),
           index_property_host=self,
           values_property="routing_mode_list",
           index_property="routing_mode_index"),)

# okay decompiling ./MIDIRemoteScripts/ableton/v2/control_surface/roar_decoration.pyc
