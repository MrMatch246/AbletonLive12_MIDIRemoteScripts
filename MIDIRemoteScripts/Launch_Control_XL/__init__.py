# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launch_Control_XL\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 722 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import AUTO_LOAD_KEY, CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, controller_id, inport, outport
from .LaunchControlXL import LaunchControlXL

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[97],
                          model_name="Launch Control XL")), 
     
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[NOTES_CC, SCRIPT])], 
     AUTO_LOAD_KEY: True}


def create_instance(c_instance):
    return LaunchControlXL(c_instance)

# okay decompiling ./MIDIRemoteScripts/Launch_Control_XL/__init__.pyc
