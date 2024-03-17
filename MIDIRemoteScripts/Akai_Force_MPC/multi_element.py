# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Akai_Force_MPC\multi_element.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1063 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import old_hasattr
from ableton.v2.control_surface.elements import MultiElement as MultiElementBase

class MultiElement(MultiElementBase):

    def __init__(self, *a, **k):
        (super(MultiElement, self).__init__)(*a, **k)
        self._parameter_to_map_to = None

    @property
    def touch_element(self):
        for control in self.owned_control_elements():
            if old_hasattr(control, "touch_element"):
                return control.touch_element

    def connect_to(self, parameter):
        self._parameter_to_map_to = parameter
        for control in self.owned_control_elements():
            control.connect_to(parameter)

    def release_parameter(self):
        self._parameter_to_map_to = None
        for control in self.owned_control_elements():
            control.release_parameter()

    def mapped_parameter(self):
        return self._parameter_to_map_to

# okay decompiling ./MIDIRemoteScripts/Akai_Force_MPC/multi_element.pyc
