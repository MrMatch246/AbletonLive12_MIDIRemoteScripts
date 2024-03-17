# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Pro\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 804 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, SYNC, controller_id, inport, outport
from .Launchpad_Pro import Launchpad_Pro

def create_instance(c_instance):
    return Launchpad_Pro(c_instance)


def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[81],
                          model_name="Launchpad Pro")), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT, REMOTE]),
                 inport(props=[]),
                 outport(props=[NOTES_CC, SYNC, SCRIPT, REMOTE]),
                 outport(props=[])]}

# okay decompiling ./MIDIRemoteScripts/Launchpad_Pro/__init__.pyc
