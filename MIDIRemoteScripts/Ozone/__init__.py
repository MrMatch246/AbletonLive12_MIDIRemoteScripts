# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Ozone\__init__.py
# Size of source mod 2**32: 1602 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Generic.GenericScript import GenericScript as GenericScript
from .config import *

def create_instance(c_instance):
    return GenericScript(c_instance, Live.MidiMap.MapMode.absolute, Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS, TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS, BANK_CONTROLS, CONTROLLER_DESCRIPTIONS)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=1891,
                          product_ids=[8200],
                          model_name="Ozone")), 
     
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[SCRIPT])]}

# okay decompiling ./MIDIRemoteScripts/Ozone/__init__.pyc
