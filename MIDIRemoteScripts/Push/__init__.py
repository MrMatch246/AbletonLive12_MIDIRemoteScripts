# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push\__init__.py
# Size of source mod 2**32: 1073 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import AUTO_LOAD_KEY, CONTROLLER_ID_KEY, FIRMWARE_KEY, HIDDEN, NOTES_CC, PORTS_KEY, SCRIPT, SYNC, TYPE_KEY, controller_id, inport, outport
from .firmware_handling import get_provided_firmware_version
from .push import Push

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=2536,
                          product_ids=[21],
                          model_name="Ableton Push")), 
     
     PORTS_KEY: [
                 inport(props=[HIDDEN, NOTES_CC, SCRIPT]),
                 inport(props=[]),
                 outport(props=[HIDDEN, NOTES_CC, SYNC, SCRIPT]),
                 outport(props=[])], 
     
     TYPE_KEY: "push", 
     FIRMWARE_KEY: (get_provided_firmware_version()), 
     AUTO_LOAD_KEY: True}


def create_instance(c_instance):
    return Push(c_instance=c_instance)

# okay decompiling ./MIDIRemoteScripts/Push/__init__.pyc
