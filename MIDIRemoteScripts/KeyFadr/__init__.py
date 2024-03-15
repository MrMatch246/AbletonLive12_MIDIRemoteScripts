# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyFadr\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 647 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, controller_id, inport, outport
from .KeyFadr import KeyFadr

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=9901,
                          product_ids=[28150],
                          model_name="Reloop KeyFadr")), 
     
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return KeyFadr(c_instance)

# okay decompiling ./MIDIRemoteScripts/KeyFadr/__init__.pyc