# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Alesis_V\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 706 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from .Alesis_V import Alesis_V

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=5042,
                          product_ids=[
                         134, 135, 136],
                          model_name=[
                         "V25", "V49", "V61"])), 
     
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[SCRIPT])]}


def create_instance(c_instance):
    return Alesis_V(c_instance)

# okay decompiling ./MIDIRemoteScripts/Alesis_V/__init__.pyc
