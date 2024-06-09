# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Komplete_Kontrol_S_Mk2\__init__.py
# Size of source mod 2**32: 458 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import SUGGESTED_PORT_NAMES_KEY
from .komplete_kontrol_s_mk2 import Komplete_Kontrol_S_Mk2

def get_capabilities():
    return {SUGGESTED_PORT_NAMES_KEY: ["Komplete Kontrol DAW - 1"]}


def create_instance(c_instance):
    return Komplete_Kontrol_S_Mk2(c_instance=c_instance)

# okay decompiling ./MIDIRemoteScripts/Komplete_Kontrol_S_Mk2/__init__.pyc
