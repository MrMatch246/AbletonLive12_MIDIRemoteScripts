# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_MPDMkIIBase\ControlElementUtils.py
# Size of source mod 2**32: 763 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ButtonElement import ButtonElement as ButtonElement
from _Framework.EncoderElement import EncoderElement as EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.SliderElement import SliderElement as SliderElement

def make_encoder(identifier, channel, name):
    return EncoderElement(MIDI_CC_TYPE,
      channel, identifier, (Live.MidiMap.MapMode.absolute), name=name)


def make_slider(identifier, channel, name):
    return SliderElement(MIDI_CC_TYPE, channel, identifier, name=name)


def make_button(identifier, channel, name):
    return ButtonElement(True, MIDI_CC_TYPE, channel, identifier, name=name)

# okay decompiling ./MIDIRemoteScripts/_MPDMkIIBase/ControlElementUtils.pyc
