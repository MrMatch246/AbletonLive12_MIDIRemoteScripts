# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Axiom\Encoders.py
# Size of source mod 2**32: 10272 bytes

from __future__ import absolute_import, print_function, unicode_literals
from builtins import object, range, str
import Live
from _Generic.Devices import *
from .consts import *

class Encoders(object):

    def __init__(self, parent, extended):
        self._Encoders__parent = parent
        self._Encoders__bank = 0
        self._Encoders__selected_device = None
        self._Encoders__extended = extended
        self._Encoders__modifier = False
        self._Encoders__device_locked = False
        self._Encoders__show_bank = False

    def disconnect(self):
        if self._Encoders__selected_device != None:
            self._Encoders__selected_device.remove_parameters_listener(self._Encoders__on_device_parameters_changed)
            self._Encoders__selected_device = None

    def build_midi_map(self, script_handle, midi_map_handle):
        tracks = self._Encoders__parent.song().visible_tracks
        feedback_rule = Live.MidiMap.CCFeedbackRule()
        for channel in range(4):
            for encoder in range(8):
                track_index = encoder + channel * 8
                if len(tracks) > track_index:
                    feedback_rule.channel = 0
                    feedback_rule.cc_no = AXIOM_ENCODERS[encoder]
                    feedback_rule.cc_value_map = tuple()
                    feedback_rule.delay_in_ms = -1.0
                    if self._Encoders__extended or self._Encoders__modifier:
                        device_parameter = tracks[track_index].mixer_device.panning
                    else:
                        device_parameter = tracks[track_index].mixer_device.volume
                    avoid_takeover = True
                    Live.MidiMap.map_midi_cc_with_feedback_map(midi_map_handle, device_parameter, channel, AXIOM_ENCODERS[encoder], Live.MidiMap.MapMode.relative_smooth_binary_offset, feedback_rule, not avoid_takeover)
                else:
                    break

        self._Encoders__connect_to_device(midi_map_handle)

    def set_modifier(self, mod_state):
        self._Encoders__modifier = mod_state

    def __connect_to_deviceParse error at or near `COME_FROM' instruction at offset 510_0

    def receive_midi_cc(self, cc_no, cc_value, channel):
        pass

    def lock_to_device(self, device):
        if device:
            self._Encoders__device_locked = True
            self._Encoders__change_appointed_device(device)

    def unlock_from_device(self, device):
        if device:
            if device == self._Encoders__selected_device:
                self._Encoders__device_locked = False
                if not self._Encoders__parent.song().appointed_device == self._Encoders__selected_device:
                    self._Encoders__parent.request_rebuild_midi_map()

    def set_appointed_device(self, device):
        if not self._Encoders__device_locked:
            self._Encoders__change_appointed_device(device)

    def set_bank(self, new_bank):
        result = False
        if self._Encoders__selected_device:
            if number_of_parameter_banks(self._Encoders__selected_device) > new_bank:
                self._Encoders__show_bank = True
                if not self._Encoders__device_locked:
                    self._Encoders__bank = new_bank
                    result = True
                else:
                    self._Encoders__selected_device.store_chosen_bank(self._Encoders__parent.instance_identifier(), new_bank)
        return result

    def restore_bank(self, new_bank):
        self._Encoders__bank = new_bank
        self._Encoders__show_bank = True

    def reset_bank(self):
        self._Encoders__bank = 0

    def __show_bank_select(self, bank_name):
        if self._Encoders__selected_device:
            self._Encoders__parent.show_message(str(self._Encoders__selected_device.name + " Bank: " + bank_name))

    def __change_appointed_device(self, device):
        if not device == self._Encoders__selected_device:
            if self._Encoders__selected_device != None:
                self._Encoders__selected_device.remove_parameters_listener(self._Encoders__on_device_parameters_changed)
            if device != None:
                device.add_parameters_listener(self._Encoders__on_device_parameters_changed)
            self._Encoders__bank = 0
        self._Encoders__show_bank = False
        self._Encoders__selected_device = device
        self._Encoders__parent.request_rebuild_midi_map()

    def __on_device_parameters_changed(self):
        self._Encoders__parent.request_rebuild_midi_map()
