# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Arturia\SessionComponent.py
# Size of source mod 2**32: 2022 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Control import EncoderControl
from _Framework.SessionComponent import SessionComponent as SessionComponentBase

class SessionComponent(SessionComponentBase):
    scene_select_encoder = EncoderControl()
    _session_component_ends_initialisation = False

    def __init__(self, *a, **k):
        (super(SessionComponent, self).__init__)(*a, **k)
        self.set_offsets(0, 0)
        self.on_selected_scene_changed()
        self.on_selected_track_changed()

    def set_scene_select_control(self, control):
        self.scene_select_encoder.set_control_element(control)

    @scene_select_encoder.value
    def scene_select_encoder(self, value, encoder):
        selected_scene = self.song().view.selected_scene
        all_scenes = self.song().scenes
        current_index = list(all_scenes).index(selected_scene)
        if value > 0 and selected_scene != all_scenes[-1]:
            self.song().view.selected_scene = all_scenes[current_index + 1]
        elif value < 0:
            if selected_scene != all_scenes[0]:
                self.song().view.selected_scene = all_scenes[current_index - 1]

    def on_selected_scene_changed(self):
        super(SessionComponent, self).on_selected_scene_changed()
        all_scenes = list(self.song().scenes)
        selected_scene = self.song().view.selected_scene
        new_scene_offset = all_scenes.index(selected_scene)
        self.set_offsets(self.track_offset(), new_scene_offset)

    def on_selected_track_changed(self):
        super(SessionComponent, self).on_selected_track_changed()
        tracks = list(self.song().tracks)
        selected_track = self.song().view.selected_track
        if selected_track in tracks:
            track_index = tracks.index(selected_track)
            new_track_offset = track_index - track_index % self.width()
            self.set_offsets(new_track_offset, self.scene_offset())

# okay decompiling ./MIDIRemoteScripts/_Arturia/SessionComponent.pyc
