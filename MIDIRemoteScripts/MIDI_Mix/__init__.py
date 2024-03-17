# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MIDI_Mix\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 615 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.Capabilities as caps
from .MIDI_Mix import MIDI_Mix

def get_capabilities():
    return {(caps.CONTROLLER_ID_KEY): (caps.controller_id(vendor_id=2536,
                                 product_ids=[49],
                                 model_name="MIDI Mix")), 
     
     (caps.PORTS_KEY): [
                        caps.inport(props=[caps.NOTES_CC, caps.SCRIPT]),
                        caps.outport(props=[caps.NOTES_CC, caps.SCRIPT])]}


def create_instance(c_instance):
    return MIDI_Mix(c_instance)

# okay decompiling ./MIDIRemoteScripts/MIDI_Mix/__init__.pyc
