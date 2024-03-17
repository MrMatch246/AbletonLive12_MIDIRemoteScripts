# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launch_Control\SpecialSessionComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 567 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from future.moves.itertools import zip_longest
from _Framework.SessionComponent import SessionComponent as SessionComponent

class SpecialSessionComponent(SessionComponent):

    def set_clip_launch_buttons(self, buttons):
        for i, button in zip_longest(range(self._num_tracks), buttons or []):
            scene = self.selected_scene()
            slot = scene.clip_slot(i)
            slot.set_launch_button(button)

# okay decompiling ./MIDIRemoteScripts/Launch_Control/SpecialSessionComponent.pyc
