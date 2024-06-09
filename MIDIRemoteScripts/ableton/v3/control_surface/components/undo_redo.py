# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\components\undo_redo.py
# Size of source mod 2**32: 1331 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import cast
from .. import Component
from ..controls import ButtonControl
from ..display import Renderable

class UndoRedoComponent(Component, Renderable):
    undo_button = ButtonControl(color="UndoRedo.Undo",
      pressed_color="UndoRedo.UndoPressed")
    redo_button = ButtonControl(color="UndoRedo.Redo",
      pressed_color="UndoRedo.RedoPressed")

    def __init__(self, name='Undo_Redo', *a, **k):
        (super().__init__)(a, name=name, **k)

    @undo_button.pressed
    def undo_button(self, _):
        if self.song.can_undo:
            self.notify(self.notifications.UndoRedo.undo, cast(str, self.song.undo()))
        else:
            self.notify(self.notifications.UndoRedo.error_undo_no_action)

    @redo_button.pressed
    def redo_button(self, _):
        if self.song.can_redo:
            self.notify(self.notifications.UndoRedo.redo, cast(str, self.song.redo()))
        else:
            self.notify(self.notifications.UndoRedo.error_redo_no_action)

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/components/undo_redo.pyc
