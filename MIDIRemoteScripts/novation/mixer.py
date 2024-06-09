# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\mixer.py
# Size of source mod 2**32: 2309 bytes
from __future__ import absolute_import, print_function, unicode_literals
from future.moves.itertools import zip_longest
from functools import partial
from ableton.v2.control_surface.components import MixerComponent as MixerComponentBase

class MixerComponent(MixerComponentBase):

    def __getattr__(self, name):
        if name.startswith("set_"):
            if name.endswith("controls") or name.endswith("displays"):
                if not getattr(self, name[4:], None):
                    return partial(self._set_controls_on_all_channel_strips, name[4:-1])
                raise AttributeError

    def _set_controls_on_all_channel_strips(self, attr_name, controls):
        for (strip, control) in zip_longest(self._channel_strips, controls or []):
            getattr(strip, attr_name).set_control_element(control)

    def set_static_color_value(self, value):
        for strip in self._channel_strips:
            strip.set_static_color_value(value)

    def set_send_a_controls(self, controls):
        self._set_send_controls(controls, 0)

    def set_send_b_controls(self, controls):
        self._set_send_controls(controls, 1)

    def _set_send_controls(self, controls, send_index):
        if controls:
            for (index, control) in enumerate(controls):
                if control:
                    self.channel_strip(index).set_send_controls((None, ) * send_index + (control,))

        else:
            for strip in self._channel_strips:
                strip.set_send_controls(None)

# okay decompiling ./MIDIRemoteScripts/novation/mixer.pyc
