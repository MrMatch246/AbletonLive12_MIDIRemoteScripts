# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launch_Control\Sysex.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 496 bytes
from __future__ import absolute_import, print_function, unicode_literals
MODE_CHANGE_PREFIX = (240, 0, 32, 41, 2, 10, 119)
MIXER_MODE = (240, 0, 32, 41, 2, 10, 119, 8, 247)
SESSION_MODE = (240, 0, 32, 41, 2, 10, 119, 9, 247)
DEVICE_MODE = (240, 0, 32, 41, 2, 10, 119, 10, 247)

def make_automatic_flashing_message(channel):
    return (
     176 + channel, 0, 40)

# okay decompiling ./MIDIRemoteScripts/Launch_Control/Sysex.pyc