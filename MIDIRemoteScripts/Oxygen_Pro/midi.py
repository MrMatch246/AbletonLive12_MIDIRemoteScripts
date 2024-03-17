# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Oxygen_Pro\midi.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1299 bytes
from __future__ import absolute_import, print_function, unicode_literals
SYSEX_START_BYTE = 240
SYSEX_END_BYTE = 247
M_AUDIO_MANUFACTURER_ID = (0, 1, 5)
SYSEX_HEADER = (
 SYSEX_START_BYTE,) + M_AUDIO_MANUFACTURER_ID + (127, 0, 0)
LED_CONTROL_BYTES = (107, 0, 1)
LED_ENABLE_BYTE = 1
LED_MODE_BYTES = (108, 0, 1)
FIRMWARE_CONTROL_BYTE = 0
SOFTWARE_CONTROL_BYTE = 3
FIRMWARE_MODE_BYTES = (109, 0, 1)
LIVE_MODE_BYTE = 2
CONTROL_MODE_BYTES = (110, 0, 1)
RECORD_MODE_BYTE = 2
DEVICE_MODE_BYTE = 7

# okay decompiling ./MIDIRemoteScripts/Oxygen_Pro/midi.pyc
