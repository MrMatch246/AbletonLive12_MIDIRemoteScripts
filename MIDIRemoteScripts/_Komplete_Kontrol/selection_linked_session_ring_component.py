# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Komplete_Kontrol\selection_linked_session_ring_component.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 833 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens
from ableton.v2.control_surface.components import SessionRingComponent

class SelectionLinkedSessionRingComponent(SessionRingComponent):

    def __init__(self, *a, **k):
        (super(SelectionLinkedSessionRingComponent, self).__init__)(*a, **k)
        self._SelectionLinkedSessionRingComponent__on_selected_track_changed.subject = self.song.view
        self._SelectionLinkedSessionRingComponent__on_selected_track_changed()

    @listens("selected_track")
    def __on_selected_track_changed(self):
        selected_track = self.song.view.selected_track
        if selected_track not in self.controlled_tracks():
            all_tracks = list(self.tracks_to_use())
            self.track_offset = all_tracks.index(selected_track)

# okay decompiling ./MIDIRemoteScripts/_Komplete_Kontrol/selection_linked_session_ring_component.pyc
