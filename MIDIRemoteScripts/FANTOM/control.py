# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\FANTOM\control.py
# Size of source mod 2**32: 941 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.controls import Control

class DisplayControl(Control):

    class State(Control.State):

        def __init__(self, *a, **k):
            (super().__init__)(*a, **k)
            self._data = ""

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, data):
            self._data = data
            self._send_current_data()

        def set_control_element(self, control_element):
            super().set_control_element(control_element)
            self._send_current_data()

        def update(self):
            super().update()
            self._send_current_data()

        def _send_current_data(self):
            if self._control_element:
                self._control_element.display_data(self._data)

# okay decompiling ./MIDIRemoteScripts/FANTOM/control.pyc
