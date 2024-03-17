# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\note_editor.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 494 bytes
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.note_editor_component import NoteEditorComponent

class Push2NoteEditorComponent(NoteEditorComponent):
    __events__ = ('mute_solo_stop_cancel_action_performed', )

    def _on_pad_pressed(self, coordinate):
        super(Push2NoteEditorComponent, self)._on_pad_pressed(coordinate)
        self.notify_mute_solo_stop_cancel_action_performed()

# okay decompiling ./MIDIRemoteScripts/Push2/note_editor.pyc
