# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\AIRA_MX_1\NotifyingMixerComponent.py
# Compiled at: 2024-02-20 00:55:13
# Size of source mod 2**32: 1293 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.MixerComponent as MixerComponent
from _Framework.Control import ButtonControl

class NotifyingMixerComponent(MixerComponent):
    send_index_up_button = ButtonControl()
    send_index_down_button = ButtonControl()
    modifier_button = ButtonControl(color=0, pressed_color=127)

    def tracks_to_use(self):
        return tuple(self.song().visible_tracks) + tuple(self.song().return_tracks)

    @send_index_up_button.pressed
    def send_index_up_button(self, button):
        self._adjust_send_index(1)

    @send_index_down_button.pressed
    def send_index_down_button(self, button):
        self._adjust_send_index(-1)

    def _adjust_send_index(self, factor):
        new_index = self.send_index + factor
        if 0 <= new_index < self.num_sends:
            self.send_index = new_index
            self._show_msg_callback("Tone/Filter Controlling Send: %s" % self.song().return_tracks[self.send_index].name)

# okay decompiling ./MIDIRemoteScripts/AIRA_MX_1/NotifyingMixerComponent.pyc