# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\RemoteSL_Classic\RemoteSLComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1723 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from .consts import *

class RemoteSLComponent(object):

    def __init__(self, remote_sl_parent):
        self._RemoteSLComponent__parent = remote_sl_parent
        self._RemoteSLComponent__support_mkII = False

    def application(self):
        return self._RemoteSLComponent__parent.application()

    def song(self):
        return self._RemoteSLComponent__parent.song()

    def send_midi(self, midi_event_bytes):
        self._RemoteSLComponent__parent.send_midi(midi_event_bytes)

    def request_rebuild_midi_map(self):
        self._RemoteSLComponent__parent.request_rebuild_midi_map()

    def disconnect(self):
        pass

    def build_midi_map(self, script_handle, midi_map_handle):
        pass

    def refresh_state(self):
        pass

    def update_display(self):
        pass

    def cc_status_byte(self):
        return CC_STATUS + SL_MIDI_CHANNEL

    def support_mkII(self):
        return self._RemoteSLComponent__support_mkII

    def set_support_mkII(self, support_mkII):
        self._RemoteSLComponent__support_mkII = support_mkII

# okay decompiling ./MIDIRemoteScripts/RemoteSL_Classic/RemoteSLComponent.pyc
