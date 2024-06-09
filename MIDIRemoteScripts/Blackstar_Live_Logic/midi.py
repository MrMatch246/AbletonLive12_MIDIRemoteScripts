# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Blackstar_Live_Logic\midi.py
# Size of source mod 2**32: 455 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.midi import SYSEX_END, SYSEX_START
SYSEX_HEADER = (
 SYSEX_START, 0, 32, 114)
NUMERIC_DISPLAY_COMMAND = (0, )
LIVE_INTEGRATION_MODE_ID = (
 SYSEX_START,
 0,
 0,
 116,
 1,
 0,
 77,
 67,
 1,
 0,
 7,
 1,
 0)

# okay decompiling ./MIDIRemoteScripts/Blackstar_Live_Logic/midi.pyc
