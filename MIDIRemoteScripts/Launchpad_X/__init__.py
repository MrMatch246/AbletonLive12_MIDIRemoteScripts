# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_X\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 831 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, SYNC, controller_id, inport, outport
from .launchpad_x import Launchpad_X

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[259],
                          model_name=["Launchpad X"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT]),
                 inport(props=[NOTES_CC, REMOTE]),
                 outport(props=[NOTES_CC, SYNC, SCRIPT]),
                 outport(props=[REMOTE])]}


def create_instance(c_instance):
    return Launchpad_X(c_instance=c_instance)

# okay decompiling ./MIDIRemoteScripts/Launchpad_X/__init__.pyc
