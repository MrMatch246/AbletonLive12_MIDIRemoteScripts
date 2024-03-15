# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_88\KeyLab88.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 862 bytes
from __future__ import absolute_import, print_function, unicode_literals
import KeyLab.KeyLab as KeyLab

class KeyLab88(KeyLab):

    def _setup_hardware_encoder(self, hardware_id, identifier, channel=0):
        self._set_encoder_cc_msg_type(hardware_id)
        self._set_identifier(hardware_id, identifier)
        self._set_channel(hardware_id, channel)
        self._set_binary_offset_mode(hardware_id)

    def _setup_hardware_button(self, hardware_id, identifier, channel=0, **k):
        self._set_button_msg_type(hardware_id, "cc")
        self._set_channel(hardware_id, channel)
        self._set_identifier(hardware_id, identifier)
        self._set_value_minimum(hardware_id)
        self._set_value_maximum(hardware_id)
        self._set_momentary_mode(hardware_id, is_momentary=True)

# okay decompiling ./MIDIRemoteScripts/KeyLab_88/KeyLab88.pyc
