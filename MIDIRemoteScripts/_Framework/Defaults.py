# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\Defaults.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 432 bytes
from __future__ import absolute_import, division, print_function, unicode_literals
from past.utils import old_div
TIMER_DELAY = 0.1
MOMENTARY_DELAY = 0.3
MOMENTARY_DELAY_TICKS = int(old_div(MOMENTARY_DELAY, TIMER_DELAY))

# okay decompiling ./MIDIRemoteScripts/_Framework/Defaults.pyc