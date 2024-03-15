# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Keystage\mappings.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 824 bytes
from __future__ import absolute_import, print_function, unicode_literals

def create_mappings(_):
    mappings = {}
    mappings["Transport"] = dict(play_button="play_button",
      stop_button="stop_button",
      loop_button="loop_button",
      tap_tempo_button="tempo_button",
      metronome_button="metronome_button",
      rewind_button="rewind_button",
      fastforward_button="fastforward_button")
    mappings["View_Based_Recording"] = dict(record_button="record_button")
    mappings["Undo_Redo"] = dict(undo_button="undo_button")
    mappings["View_Control"] = dict(prev_track_button="up_button",
      next_track_button="down_button")
    mappings["Device"] = dict(parameter_controls="knobs")
    return mappings

# okay decompiling ./MIDIRemoteScripts/Keystage/mappings.pyc
