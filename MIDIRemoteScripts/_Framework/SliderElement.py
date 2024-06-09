# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\SliderElement.py
# Size of source mod 2**32: 619 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from .EncoderElement import EncoderElement
from .InputControlElement import MIDI_NOTE_TYPE

class SliderElement(EncoderElement):

    def __init__(self, msg_type, channel, identifier, *a, **k):
        (super(SliderElement, self).__init__)(
 msg_type, channel, identifier, *a, map_mode=Live.MidiMap.MapMode.absolute, **k)

# okay decompiling ./MIDIRemoteScripts/_Framework/SliderElement.pyc
