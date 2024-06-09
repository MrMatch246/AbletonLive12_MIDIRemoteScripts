# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad\SpecialSessionComponent.py
# Size of source mod 2**32: 1559 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.SessionComponent import SessionComponent as SessionComponent

class SpecialSessionComponent(SessionComponent):

    def _update_stop_clips_led(self, index):
        if self.is_enabled():
            if self._stop_track_clip_buttons != None:
                if index < len(self._stop_track_clip_buttons):
                    button = self._stop_track_clip_buttons[index]
                    tracks_to_use = self.tracks_to_use()
                    track_index = index + self.track_offset()
                    if 0 <= track_index < len(tracks_to_use):
                        track = tracks_to_use[track_index]
                        if track.fired_slot_index == -2:
                            button.send_value(self._stop_clip_triggered_value)
                        elif track.playing_slot_index >= 0:
                            button.send_value(self._stop_clip_value)
                        else:
                            button.turn_off()
                    else:
                        button.send_value(4)

# okay decompiling ./MIDIRemoteScripts/Launchpad/SpecialSessionComponent.pyc
