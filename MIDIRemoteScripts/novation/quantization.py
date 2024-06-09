# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\quantization.py
# Size of source mod 2**32: 1550 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import listens
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ToggleButtonControl
RecordingQuantization = Live.Song.RecordingQuantization

class QuantizationComponent(Component):
    quantization_toggle_button = ToggleButtonControl(untoggled_color="Quantization.Off",
      toggled_color="Quantization.On")

    def __init__(self, *a, **k):
        (super(QuantizationComponent, self).__init__)(*a, **k)
        self._record_quantization = RecordingQuantization.rec_q_sixtenth
        self._QuantizationComponent__on_record_quantization_changed.subject = self.song
        self._QuantizationComponent__on_record_quantization_changed()

    def quantize_clip(self, clip):
        clip.quantize(self._record_quantization, 1.0)

    @quantization_toggle_button.toggled
    def quantization_toggle_button(self, is_toggled, _):
        self.song.midi_recording_quantization = self._record_quantization if is_toggled else RecordingQuantization.rec_q_no_q

    @listens("midi_recording_quantization")
    def __on_record_quantization_changed(self):
        quantization_on = self.song.midi_recording_quantization != RecordingQuantization.rec_q_no_q
        if quantization_on:
            self._record_quantization = self.song.midi_recording_quantization
        self.quantization_toggle_button.is_toggled = quantization_on

# okay decompiling ./MIDIRemoteScripts/novation/quantization.pyc
