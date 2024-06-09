# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Axiom\Pads.py
# Size of source mod 2**32: 2613 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object, range
import Live
from .consts import *

class Pads(object):

    def __init__(self, parent):
        self._Pads__parent = parent

    def build_midi_map(self, script_handle, midi_map_handle):
        for channel in range(4):
            for pad in range(8):
                Live.MidiMap.forward_midi_cc(script_handle, midi_map_handle, channel, AXIOM_PADS[pad])

        for pad in range(8):
            Live.MidiMap.forward_midi_cc(script_handle, midi_map_handle, 15, AXIOM_PADS[pad])

    def receive_midi_cc(self, cc_no, cc_value, channel):
        if list(AXIOM_PADS).count(cc_no) > 0:
            pad_index = list(AXIOM_PADS).index(cc_no)
            index = pad_index + channel * 8
            if cc_value > 0:
                if channel in range(4):
                    if self._Pads__parent.application().view.is_view_visible("Session"):
                        tracks = self._Pads__parent.song().visible_tracks
                        if len(tracks) > index:
                            current_track = tracks[index]
                            clip_index = list(self._Pads__parent.song().scenes).index(self._Pads__parent.song().view.selected_scene)
                            current_track.clip_slots[clip_index].fire()
                elif self._Pads__parent.application().view.is_view_visible("Arranger"):
                    if len(self._Pads__parent.song().cue_points) > index:
                        self._Pads__parent.song().cue_points[index].jump()
                    elif channel == 15:
                        self._Pads__parent.bank_changed(pad_index)

# okay decompiling ./MIDIRemoteScripts/_Axiom/Pads.pyc
