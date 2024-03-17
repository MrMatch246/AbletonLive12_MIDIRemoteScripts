# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\device_chain_utils.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 740 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from itertools import chain
import Live
from ableton.v2.base import find_if, liveobj_valid

def is_empty_drum_pad(drum_pad):
    return isinstance(drum_pad, Live.DrumPad.DrumPad) and (not drum_pad.chains or not drum_pad.chains[0].devices)


def is_first_device_on_pad(device, drum_pad):
    return find_if((lambda pad: pad.chains and pad.chains[0].devices and pad.chains[0].devices[0] == device), drum_pad.canonical_parent.drum_pads)


def is_simpler(device):
    return device and device.class_name == "OriginalSimpler"

# okay decompiling ./MIDIRemoteScripts/pushbase/device_chain_utils.pyc
