# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Komplete_Kontrol_A\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 484 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import SUGGESTED_PORT_NAMES_KEY
from .komplete_kontrol_a import Komplete_Kontrol_A

def get_capabilities():
    return {SUGGESTED_PORT_NAMES_KEY: ["Komplete Kontrol A DAW", "Komplete Kontrol M DAW"]}


def create_instance(c_instance):
    return Komplete_Kontrol_A(c_instance=c_instance)

# okay decompiling ./MIDIRemoteScripts/Komplete_Kontrol_A/__init__.pyc