# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\SL_MkIII\session.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1011 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import find_if
from ableton.v2.control_surface.components import SessionComponent as SessionComponentBase

class SessionComponent(SessionComponentBase):

    def _update_stop_clips_led(self, index):
        super()._update_stop_clips_led(index)
        self._update_stop_all_clips_button()

    def _update_stop_all_clips_button(self):
        button = self._stop_all_button
        if button:
            value_to_send = self._stop_clip_disabled_value
            tracks = self.song.tracks
            if find_if((lambda x: x.playing_slot_index >= 0 and x.fired_slot_index != -2), tracks):
                value_to_send = self._stop_clip_value
            else:
                if find_if((lambda x: x.fired_slot_index == -2), tracks):
                    value_to_send = self._stop_clip_triggered_value
            button.set_light(value_to_send)

# okay decompiling ./MIDIRemoteScripts/SL_MkIII/session.pyc
