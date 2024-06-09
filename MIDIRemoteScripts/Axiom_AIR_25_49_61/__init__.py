# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Axiom_AIR_25_49_61\__init__.py
# Size of source mod 2**32: 808 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, controller_id, inport, outport
from .Axiom_AIR_25_49_61 import Axiom_AIR_25_49_61

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=1891,
                          product_ids=[8243],
                          model_name="Axiom AIR 49")), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC]),
                 inport(props=[SCRIPT]),
                 inport(props=[NOTES_CC]),
                 outport(props=[NOTES_CC]),
                 outport(props=[SCRIPT])]}


def create_instance(c_instance):
    return Axiom_AIR_25_49_61(c_instance)

# okay decompiling ./MIDIRemoteScripts/Axiom_AIR_25_49_61/__init__.pyc
