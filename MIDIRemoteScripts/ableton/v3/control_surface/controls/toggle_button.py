# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\controls\toggle_button.py
# Size of source mod 2**32: 1317 bytes
from __future__ import absolute_import, print_function, unicode_literals
from . import ButtonControl, Connectable, control_event

class ToggleButtonControl(ButtonControl):
    toggled = control_event("toggled")

    class State(ButtonControl.State, Connectable):
        requires_listenable_connected_property = True

        def connect_property(self, *a):
            (super().connect_property)(*a)
            self.is_on = self.connected_property_value

        def on_connected_property_changed(self, value):
            self.is_on = value

        def _on_pressed(self):
            super()._on_pressed()
            self.is_on = not self._is_on
            self._call_listener("toggled", self.is_on)
            self.connected_property_value = self.is_on

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/controls/toggle_button.pyc
