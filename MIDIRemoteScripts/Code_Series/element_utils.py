# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Code_Series\element_utils.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 874 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import depends
from ableton.v2.control_surface import MIDI_CC_TYPE, MIDI_NOTE_TYPE, MIDI_PB_TYPE
from ableton.v2.control_surface.elements import ButtonElement, EncoderElement, SliderElement
IS_MOMENTARY = True
CHANNEL = 0

@depends(skin=None)
def make_button(identifier, name, **k):
    return ButtonElement(
 IS_MOMENTARY, MIDI_NOTE_TYPE, CHANNEL, identifier, name=name, **k)


def make_slider(channel, name):
    return SliderElement(MIDI_PB_TYPE, channel, 0, name=name)


def make_encoder(identifier, name):
    return EncoderElement(MIDI_CC_TYPE,
      0,
      identifier,
      (Live.MidiMap.MapMode.relative_smooth_signed_bit),
      name=name)

# okay decompiling ./MIDIRemoteScripts/Code_Series/element_utils.pyc
