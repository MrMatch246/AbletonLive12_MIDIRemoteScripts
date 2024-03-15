# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Komplete_Kontrol\sysex.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 910 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import midi
HEADER = (
 midi.SYSEX_START, 0, 33, 9, 0, 0, 68, 67, 1, 0)
TRACK_TYPE_DISPLAY_HEADER = HEADER + (64, )
TRACK_CHANGED_DISPLAY_HEADER = HEADER + (65, 0, 0)
TRACK_SELECT_DISPLAY_HEADER = HEADER + (66, )
TRACK_MUTE_DISPLAY_HEADER = HEADER + (67, )
TRACK_SOLO_DISPLAY_HEADER = HEADER + (68, )
TRACK_ARM_DISPLAY_HEADER = HEADER + (69, )
TRACK_VOLUME_DISPLAY_HEADER = HEADER + (70, 0)
TRACK_PANNING_DISPLAY_HEADER = HEADER + (71, 0)
TRACK_NAME_DISPLAY_HEADER = HEADER + (72, 0)
TRACK_METER_DISPLAY_HEADER = HEADER + (73, 2, 0)
TRACK_MUTED_VIA_SOLO_DISPLAY_HEADER = HEADER + (74, )
EMPTY_TRACK_TYPE_VALUE = 0
DEFAULT_TRACK_TYPE_VALUE = 1
MASTER_TRACK_TYPE_VALUE = 6

# okay decompiling ./MIDIRemoteScripts/_Komplete_Kontrol/sysex.pyc
