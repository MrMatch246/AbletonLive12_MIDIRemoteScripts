# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\OptionalElement.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1179 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .ComboElement import ToggleElement
from .SubjectSlot import SlotManager, subject_slot

class ChoosingElement(ToggleElement, SlotManager):

    def __init__(self, flag=None, *a, **k):
        (super(ChoosingElement, self).__init__)(*a, **k)
        self._on_flag_changed.subject = flag
        self._on_flag_changed(flag.value)

    @subject_slot("value")
    def _on_flag_changed(self, value):
        self.set_toggled(value)


class OptionalElement(ChoosingElement):

    def __init__(self, control=None, flag=None, value=None, *a, **k):
        on_control = control if value else None
        off_control = None if value else control
        (super(OptionalElement, self).__init__)(a, on_control=on_control, off_control=off_control, flag=flag, **k)

# okay decompiling ./MIDIRemoteScripts/_Framework/OptionalElement.pyc