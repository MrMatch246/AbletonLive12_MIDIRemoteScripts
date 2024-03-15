# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\APC64\recording.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1136 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.base import depends
from ableton.v3.control_surface.components import RecordingMethod
from ableton.v3.live import is_track_armed, prepare_new_clip_slot

class FixedLengthRecordingMethod(RecordingMethod):

    @depends(settings_component=None)
    def __init__(self, settings_component=None, *a, **k):
        (super().__init__)(*a, **k)
        self._fixed_length = settings_component.fixed_length

    def trigger_recording(self):
        if not self.stop_recording():
            for track in self.song.tracks:
                if is_track_armed(track):
                    slot = prepare_new_clip_slot(track)
                if self.can_record_into_clip_slot(slot):
                    if self._fixed_length.enabled:
                        slot.fire(record_length=(self._fixed_length.record_length))
                    else:
                        slot.fire()

# okay decompiling ./MIDIRemoteScripts/APC64/recording.pyc
