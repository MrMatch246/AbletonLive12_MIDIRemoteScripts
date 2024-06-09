# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Axiom_25_Classic\__init__.py
# Size of source mod 2**32: 1104 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .Axiom import Axiom

def create_instance(c_instance):
    return Axiom(c_instance)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=1891,
                          product_ids=[408],
                          model_name="USB Axiom 25")), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT]),
                 inport(props=[PLAIN_OLD_MIDI]),
                 outport(props=[SCRIPT])]}

# okay decompiling ./MIDIRemoteScripts/Axiom_25_Classic/__init__.pyc
