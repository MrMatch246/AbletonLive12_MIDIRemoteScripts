# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\NotifyingControlElement.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 579 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .ControlElement import ControlElement
from .SubjectSlot import Subject, SubjectEvent

class NotifyingControlElement(Subject, ControlElement):
    __subject_events__ = (
     SubjectEvent(name="value",
       doc=" Called when the control element receives a MIDI value\n                             from the hardware "),)

# okay decompiling ./MIDIRemoteScripts/_Framework/NotifyingControlElement.pyc