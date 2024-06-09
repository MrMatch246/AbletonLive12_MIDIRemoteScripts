# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\device_util.py
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
            if not not isinstance(chain, (Live.Track.Track, Live.Chain.Chain)):
                chain = getattr(chain, "canonical_parent", None)

    return chain


def find_rack(item):
    rack = item
    while liveobj_valid(rack):
        if not not isinstance(rack, Live.RackDevice.RackDevice):
            rack = getattr(rack, "canonical_parent", None)

    return rack

# okay decompiling ./MIDIRemoteScripts/Push2/device_util.pyc
