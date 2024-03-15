# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK2\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 842 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.Capabilities as caps
from .Launchkey_MK2 import Launchkey_MK2

def get_capabilities():
    return {(caps.CONTROLLER_ID_KEY): (caps.controller_id(vendor_id=4661,
                                 product_ids=[
                                31610, 
                                31866, 32122, 
                                123, 124, 125],
                                 model_name=[
                                "Launchkey MK2 25", "Launchkey MK2 49", "Launchkey MK2 61"])), 
     
     (caps.PORTS_KEY): [
                        caps.inport(props=[]),
                        caps.inport(props=[caps.NOTES_CC, caps.SCRIPT, caps.REMOTE]),
                        caps.outport(props=[]),
                        caps.outport(props=[caps.NOTES_CC, caps.SCRIPT, caps.REMOTE])]}


def create_instance(c_instance):
    return Launchkey_MK2(c_instance)

# okay decompiling ./MIDIRemoteScripts/Launchkey_MK2/__init__.pyc
