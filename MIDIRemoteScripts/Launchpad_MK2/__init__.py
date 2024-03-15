# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_MK2\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1724 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, SYNC, controller_id, inport, outport
from .Launchpad_MK2 import Launchpad_MK2

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[
                         105, 
                         106, 
                         107, 
                         108, 
                         109, 
                         110, 
                         111, 
                         112, 
                         113, 
                         114, 
                         115, 
                         116, 
                         117, 
                         118, 
                         119, 
                         120],
                          model_name=[
                         'Launchpad MK2', 
                         'Launchpad MK2 2', 
                         'Launchpad MK2 3', 
                         'Launchpad MK2 4', 
                         'Launchpad MK2 5', 
                         'Launchpad MK2 6', 
                         'Launchpad MK2 7', 
                         'Launchpad MK2 8', 
                         'Launchpad MK2 9', 
                         'Launchpad MK2 10', 
                         'Launchpad MK2 11', 
                         'Launchpad MK2 12', 
                         'Launchpad MK2 13', 
                         'Launchpad MK2 14', 
                         'Launchpad MK2 15', 
                         'Launchpad MK2 16'])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT, REMOTE]),
                 outport(props=[NOTES_CC, SCRIPT, SYNC, REMOTE])]}


def create_instance(c_instance):
    return Launchpad_MK2(c_instance)

# okay decompiling ./MIDIRemoteScripts/Launchpad_MK2/__init__.pyc
