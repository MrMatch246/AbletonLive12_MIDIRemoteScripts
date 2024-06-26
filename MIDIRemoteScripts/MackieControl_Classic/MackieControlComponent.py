# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MackieControl_Classic\MackieControlComponent.py
# Size of source mod 2**32: 2500 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
import Live
from .consts import *

class MackieControlComponent(object):

    def __init__(self, main_script):
        self._MackieControlComponent__main_script = main_script

    def destroy(self):
        self._MackieControlComponent__main_script = None

    def main_script(self):
        return self._MackieControlComponent__main_script

    def shift_is_pressed(self):
        return self._MackieControlComponent__main_script.shift_is_pressed()

    def option_is_pressed(self):
        return self._MackieControlComponent__main_script.option_is_pressed()

    def control_is_pressed(self):
        return self._MackieControlComponent__main_script.control_is_pressed()

    def alt_is_pressed(self):
        return self._MackieControlComponent__main_script.alt_is_pressed()

    def song(self):
        return self._MackieControlComponent__main_script.song()

    def script_handle(self):
        return self._MackieControlComponent__main_script.handle()

    def application(self):
        return self._MackieControlComponent__main_script.application()

    def send_midi(self, bytes):
        self._MackieControlComponent__main_script.send_midi(bytes)

    def request_rebuild_midi_map(self):
        self._MackieControlComponent__main_script.request_rebuild_midi_map()

# okay decompiling ./MIDIRemoteScripts/MackieControl_Classic/MackieControlComponent.pyc
