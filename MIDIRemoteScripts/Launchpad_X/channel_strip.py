# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_X\channel_strip.py
# Size of source mod 2**32: 1106 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import next
from ableton.v2.base import liveobj_valid
from novation.channel_strip import ChannelStripComponent as ChannelStripComponentBase

class ChannelStripComponent(ChannelStripComponentBase):

    def update(self):
        super(ChannelStripComponent, self).update()
        self._update_static_color_control()

    def _update_static_color_control(self):
        valid_track = liveobj_valid(self._track)
        color_value = self._static_color_value if valid_track else 0
        if valid_track:
            if self._send_controls:
                send_index = next((i for (i, x) in enumerate(self._send_controls)), None)
                if send_index is not None:
                    if send_index >= len(self._track.mixer_device.sends):
                        color_value = 0
        self.static_color_control.value = color_value

# okay decompiling ./MIDIRemoteScripts/Launchpad_X/channel_strip.pyc
