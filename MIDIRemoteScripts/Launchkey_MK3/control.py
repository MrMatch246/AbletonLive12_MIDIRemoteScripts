# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK3\control.py
# Size of source mod 2**32: 1137 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.control import Control
DEFAULT_MESSAGE = "-"

class DisplayControl(Control):

    class State(Control.State):

        def __init__(self, *a, **k):
            (super(DisplayControl.State, self).__init__)(*a, **k)
            self._message = DEFAULT_MESSAGE

        @property
        def message(self):
            return self._message

        @message.setter
        def message(self, message):
            self._message = DEFAULT_MESSAGE if message is None else message
            self._send_current_message()

        def set_control_element(self, control_element):
            super(DisplayControl.State, self).set_control_element(control_element)
            self._send_current_message()

        def update(self):
            super(DisplayControl.State, self).update()
            self._send_current_message()

        def _send_current_message(self):
            if self._control_element:
                self._control_element.display_message(self._message)

# okay decompiling ./MIDIRemoteScripts/Launchkey_MK3/control.pyc
