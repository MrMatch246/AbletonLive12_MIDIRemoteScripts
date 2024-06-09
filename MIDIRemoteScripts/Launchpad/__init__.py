# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad\__init__.py
# Size of source mod 2**32: 665 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import *
from .Launchpad import Launchpad

def create_instance(c_instance):
    return Launchpad(c_instance)


def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[
                         14, 32, 54],
                          model_name=[
                         "Launchpad", "Launchpad S", "Launchpad Mini"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE, SCRIPT]),
                 outport(props=[NOTES_CC, REMOTE, SCRIPT])]}

# okay decompiling ./MIDIRemoteScripts/Launchpad/__init__.pyc
