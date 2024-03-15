# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\VCM600\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 949 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.Capabilities as caps
from .VCM600 import VCM600

def get_capabilities():
    return {(caps.CONTROLLER_ID_KEY): (caps.controller_id(vendor_id=6817,
                                 product_ids=[64],
                                 model_name=["VCM-600"])), 
     
     (caps.PORTS_KEY): [
                        caps.inport(props=[caps.SCRIPT]),
                        caps.outport(props=[caps.SCRIPT])]}


def create_instance(c_instance):
    return VCM600(c_instance)

# okay decompiling ./MIDIRemoteScripts/VCM600/__init__.pyc
