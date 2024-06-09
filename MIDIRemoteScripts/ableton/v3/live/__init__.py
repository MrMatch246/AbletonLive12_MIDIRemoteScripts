# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\live\__init__.py
# Size of source mod 2**32: 1926 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import is_parameter_bipolar, liveobj_changed, liveobj_valid, move_current_song_time
from .util import all_visible_tracks, any_track_armed, application, deduplicate_parameters, display_name, find_parent_track, flatten_device_chain, get_bar_length, get_parameter_by_name, is_arrangement_view_active, is_clip_new_recording, is_clip_playing, is_device_rack, is_parameter_quantized, is_song_recording, is_track_armed, is_track_recording, liveobj_color_to_midi_rgb_values, liveobj_color_to_value_from_palette, liveobj_name, major_version, normalized_parameter_value, parameter_owner, parameter_value_to_midi_value, playing_clip_slot, prepare_new_clip_slot, scene_index, selected_chain, set_song, song, track_index
__all__ = ('all_visible_tracks', 'any_track_armed', 'application', 'deduplicate_parameters',
           'display_name', 'find_parent_track', 'flatten_device_chain', 'get_bar_length',
           'get_parameter_by_name', 'is_arrangement_view_active', 'is_clip_new_recording',
           'is_clip_playing', 'is_device_rack', 'is_parameter_bipolar', 'is_parameter_quantized',
           'is_song_recording', 'is_track_armed', 'is_track_recording', 'liveobj_changed',
           'liveobj_color_to_midi_rgb_values', 'liveobj_color_to_value_from_palette',
           'liveobj_name', 'liveobj_valid', 'major_version', 'move_current_song_time',
           'normalized_parameter_value', 'parameter_owner', 'parameter_value_to_midi_value',
           'playing_clip_slot', 'prepare_new_clip_slot', 'scene_index', 'selected_chain',
           'set_song', 'song', 'track_index')

# okay decompiling ./MIDIRemoteScripts/ableton/v3/live/__init__.pyc
