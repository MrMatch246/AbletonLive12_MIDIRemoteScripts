# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Generic\SelectChanStripComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1046 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from _Framework.ChannelStripComponent import ChannelStripComponent as ChannelStripComponent

class SelectChanStripComponent(ChannelStripComponent):

    def __init__(self):
        ChannelStripComponent.__init__(self)

    def _arm_value(self, value):
        if self.is_enabled():
            track_was_armed = False
            if self._track != None:
                if self._track.can_be_armed:
                    track_was_armed = self._track.arm
                ChannelStripComponent._arm_value(self, value)
                if self._track != None:
                    if self._track.can_be_armed:
                        if self._track.arm:
                            if not track_was_armed:
                                if self._track.view.select_instrument():
                                    self.song().view.selected_track = self._track

# okay decompiling ./MIDIRemoteScripts/_Generic/SelectChanStripComponent.pyc
