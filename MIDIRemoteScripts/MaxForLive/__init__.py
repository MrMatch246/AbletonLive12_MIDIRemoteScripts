# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MaxForLive\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 325 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import GENERIC_SCRIPT_KEY
from .MaxForLive import MaxForLive

def get_capabilities():
    return {GENERIC_SCRIPT_KEY: True}


def create_instance(c_instance):
    return MaxForLive(c_instance=c_instance)

# okay decompiling ./MIDIRemoteScripts/MaxForLive/__init__.pyc
