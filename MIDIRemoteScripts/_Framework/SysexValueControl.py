# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\SysexValueControl.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1115 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .InputControlElement import MIDI_SYSEX_TYPE, InputControlElement

class SysexValueControl(InputControlElement):

    def __init__(self, message_prefix=None, value_enquiry=None, default_value=None, *a, **k):
        (super(SysexValueControl, self).__init__)(a, msg_type=MIDI_SYSEX_TYPE, sysex_identifier=message_prefix, **k)
        self._value_enquiry = value_enquiry
        self._default_value = default_value

    def send_value(self, value_bytes):
        self.send_midi(self.message_sysex_identifier() + value_bytes + (247, ))

    def enquire_value(self):
        self.send_midi(self._value_enquiry)

    def reset(self):
        if self._default_value != None:
            self.send_value(self._default_value)

# okay decompiling ./MIDIRemoteScripts/_Framework/SysexValueControl.pyc