# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ATOM\note_pad.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 590 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.controls import PlayableControl

class NotePadMixin:

    def set_matrix(self, matrix):
        super().set_matrix(matrix)
        for button in self.matrix:
            button.set_mode(PlayableControl.Mode.playable_and_listenable)
            button.pressed_color = "NotePad.Pressed"

    def _on_matrix_pressed(self, _):
        pass

    def _on_matrix_released(self, button):
        self._update_button_color(button)

# okay decompiling ./MIDIRemoteScripts/ATOM/note_pad.pyc
