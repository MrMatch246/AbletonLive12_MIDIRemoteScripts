# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Roland_A_PRO\__init__.py
# Size of source mod 2**32: 805 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from .Roland_A_PRO import Roland_A_PRO

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=1410,
                          product_ids=[271],
                          model_name="A-PRO")), 
     
     PORTS_KEY: [
                 inport(props=[]),
                 inport(props=[NOTES_CC, REMOTE]),
                 inport(props=[NOTES_CC, SCRIPT, REMOTE]),
                 outport(props=[]),
                 outport(props=[SCRIPT])]}


def create_instance(c_instance):
    return Roland_A_PRO(c_instance)

# okay decompiling ./MIDIRemoteScripts/Roland_A_PRO/__init__.pyc
