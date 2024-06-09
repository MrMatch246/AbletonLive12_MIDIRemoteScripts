# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\track_frozen_mode.py
# Size of source mod 2**32: 1177 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens
from ableton.v2.control_surface.mode import ModesComponent

class TrackFrozenModesComponent(ModesComponent):

    def __init__(self, default_mode=None, frozen_mode=None, *a, **k):
        (super(TrackFrozenModesComponent, self).__init__)(*a, **k)
        self.add_mode("default", default_mode)
        self.add_mode("frozen", frozen_mode)
        self._on_selected_track_is_frozen_changed.subject = self.song.view
        if self.is_enabled():
            self._update_selected_mode()

    def _update_selected_mode(self):
        self.selected_mode = "frozen" if self.song.view.selected_track.is_frozen else "default"

    @listens("selected_track.is_frozen")
    def _on_selected_track_is_frozen_changed(self):
        self._update_selected_mode()

    def update(self):
        super(TrackFrozenModesComponent, self).update()
        if self.is_enabled():
            self._update_selected_mode()

# okay decompiling ./MIDIRemoteScripts/pushbase/track_frozen_mode.pyc
