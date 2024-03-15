# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\session_ring_selection_linking.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 2544 bytes
from __future__ import absolute_import, print_function, unicode_literals
from base.dependency import depends
from base.event import EventObject, listens
from base.util import index_if

class SessionRingSelectionLinking(EventObject):

    @depends(song=None)
    def __init__(self, session_ring=None, selection_changed_notifier=None, song=None, *a, **k):
        (super(SessionRingSelectionLinking, self).__init__)(*a, **k)
        self._session_ring = session_ring
        self._song = song
        self._on_selection_scrolled.subject = selection_changed_notifier

    @listens("selection_scrolled")
    def _on_selection_scrolled(self):
        self._link_session_ring_with_minimal_travel()

    def _link_session_ring_with_minimal_travel(self):
        if self._song.view.selected_track == self._song.master_track:
            return
        track_index = self._current_track_index()
        right_ring_index = self._session_ring.track_offset + self._session_ring.num_tracks - 1
        offset_left = track_index - self._session_ring.track_offset
        offset_right = track_index - right_ring_index
        adjustment = min(0, offset_left) + max(0, offset_right)
        new_track_offset = self._session_ring.track_offset + adjustment
        if new_track_offset != self._session_ring.track_offset:
            self._session_ring.set_offsets(new_track_offset, self._session_ring.scene_offset)

    def _current_track(self):
        return self._song.view.selected_track

    def _current_track_index(self):
        return index_if((lambda t: t == self._current_track()), self._session_ring.tracks_to_use())

# okay decompiling ./MIDIRemoteScripts/ableton/v2/control_surface/session_ring_selection_linking.pyc
