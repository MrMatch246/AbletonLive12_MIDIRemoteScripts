# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\device_util.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1134 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import liveobj_valid

def is_drum_pad(item):
    return liveobj_valid(item) and isinstance(item, Live.DrumPad.DrumPad)


def find_chain_or_track(item):
    if is_drum_pad(item) and item.chains:
        chain = item.chains[0]
    else:
        chain = item
        while liveobj_valid(chain):
            chain = isinstance(chain, (Live.Track.Track, Live.Chain.Chain)) or getattr(chain, "canonical_parent", None)

    return chain


def find_rack(item):
    rack = item
    while liveobj_valid(rack):
        rack = isinstance(rack, Live.RackDevice.RackDevice) or getattr(rack, "canonical_parent", None)

    return rack

# okay decompiling ./MIDIRemoteScripts/Push2/device_util.pyc
