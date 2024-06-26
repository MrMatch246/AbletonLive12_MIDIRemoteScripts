# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK2\InControlStatusComponent.py
# Size of source mod 2**32: 713 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent as ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot

class InControlStatusComponent(ControlSurfaceComponent):

    def __init__(self, set_is_in_control_on, *a, **k):
        (super(InControlStatusComponent, self).__init__)(*a, **k)
        self._set_is_in_control_on = set_is_in_control_on

    def set_in_control_status_button(self, button):
        self._on_in_control_value.subject = button

    @subject_slot("value")
    def _on_in_control_value(self, value):
        self._set_is_in_control_on(value >= 8)

# okay decompiling ./MIDIRemoteScripts/Launchkey_MK2/InControlStatusComponent.pyc
