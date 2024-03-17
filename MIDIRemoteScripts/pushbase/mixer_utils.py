# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\mixer_utils.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 431 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import old_hasattr

def is_set_to_split_stereo(mixer):
    modes = Live.MixerDevice.MixerDevice.panning_modes
    return modes.stereo_split == getattr(mixer, "panning_mode", modes.stereo)


def has_pan_mode(mixer):
    return old_hasattr(mixer, "panning_mode")

# okay decompiling ./MIDIRemoteScripts/pushbase/mixer_utils.pyc
