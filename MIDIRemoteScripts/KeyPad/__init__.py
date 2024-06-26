# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyPad\__init__.py
# Size of source mod 2**32: 643 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, controller_id, inport, outport
from .KeyPad import KeyPad

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=9901,
                          product_ids=[28149],
                          model_name="Reloop KeyPad")), 
     
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return KeyPad(c_instance)

# okay decompiling ./MIDIRemoteScripts/KeyPad/__init__.pyc
