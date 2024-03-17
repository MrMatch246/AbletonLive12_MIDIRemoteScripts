# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\sysex.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1036 bytes
from __future__ import absolute_import, print_function, unicode_literals
SYSEX_START_BYTE = 240
SYSEX_END_BYTE = 247
NOVATION_MANUFACTURER_ID = (0, 32, 41)
DEVICE_FAMILY_MEMBER_CODE = (0, 0)
STD_MSG_HEADER = (
 SYSEX_START_BYTE,) + NOVATION_MANUFACTURER_ID + (2, )
LAYOUT_COMMAND_BYTE = 0
FADER_COMMAND_BYTE = 1
PRINT_COMMAND_BYTE = 3
NOTE_LAYOUT_COMMAND_BYTE = 15
FIRMWARE_MODE_COMMAND_BYTE = 16
SCALE_FEEDBACK_COMMAND_BYTE = 23
PRINT_ENABLE_COMMAND_BYTE = 24
STOP_FADER_COMMAND_BYTE = 25
STANDALONE_MODE_BYTE = 0
DAW_MODE_BYTE = 1
SESSION_LAYOUT_BYTE = 0
NOTE_LAYOUT_BYTE = 1
KEYS_LAYOUT_BYTE = 5
FADERS_LAYOUT_BYTE = 13
SCALE_LAYOUT_BYTE = 0
DRUM_LAYOUT_BYTE = 1
FADER_VERTICAL_ORIENTATION = 0
FADER_HORIZONTAL_ORIENTATION = 1
FADER_UNIPOLAR = 0
FADER_BIPOLAR = 1

# okay decompiling ./MIDIRemoteScripts/novation/sysex.pyc
