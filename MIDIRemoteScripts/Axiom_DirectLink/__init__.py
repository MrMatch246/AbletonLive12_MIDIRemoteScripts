# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Axiom_DirectLink\__init__.py
# Size of source mod 2**32: 1196 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .Axiom_DirectLink import Axiom_DirectLink

def create_instance(c_instance):
    return Axiom_DirectLink(c_instance)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=1891,
                          product_ids=[8237],
                          model_name="Axiom 49")), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 inport(props=[NOTES_CC]),
                 outport(props=[]),
                 outport(props=[SCRIPT])]}

# okay decompiling ./MIDIRemoteScripts/Axiom_DirectLink/__init__.pyc
