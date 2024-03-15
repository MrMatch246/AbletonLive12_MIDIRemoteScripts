# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_APC\RingedEncoderElement.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 3318 bytes
from __future__ import absolute_import, division, print_function, unicode_literals
from past.utils import old_div
import _Framework.ButtonElement as ButtonElement
import _Framework.EncoderElement as EncoderElement
RING_OFF_VALUE = 0
RING_SIN_VALUE = 1
RING_VOL_VALUE = 2
RING_PAN_VALUE = 3

class RingedEncoderElement(EncoderElement):

    def __init__(self, msg_type, channel, identifier, map_mode, *a, **k):
        (super(RingedEncoderElement, self).__init__)(
 msg_type, channel, identifier, map_mode, *a, **k)
        self._ring_mode_button = None
        self.set_needs_takeover(False)

    def set_ring_mode_button(self, button):
        if self._ring_mode_button != None:
            self._ring_mode_button.send_value(RING_OFF_VALUE, force=True)
        self._ring_mode_button = button
        self._update_ring_mode()

    def connect_to(self, parameter):
        if parameter != self._parameter_to_map_to:
            if not self.is_mapped_manually():
                self._ring_mode_button.send_value(RING_OFF_VALUE, force=True)
        super(RingedEncoderElement, self).connect_to(parameter)

    def release_parameter(self):
        super(RingedEncoderElement, self).release_parameter()
        self._update_ring_mode()

    def install_connections(self, install_translation_callback, install_mapping_callback, install_forwarding_callback):
        super(RingedEncoderElement, self).install_connections(install_translation_callback, install_mapping_callback, install_forwarding_callback)
        if not self._is_mapped:
            if self.value_listener_count() == 0:
                self._is_being_forwarded = install_forwarding_callback(self)
        self._update_ring_mode()

    def is_mapped_manually(self):
        return not self._is_mapped and not self._is_being_forwarded

    def _update_ring_mode(self):
        if self._ring_mode_button != None:
            if self.is_mapped_manually():
                self._ring_mode_button.send_value(RING_SIN_VALUE, force=True)
            else:
                if self._parameter_to_map_to != None:
                    param = self._parameter_to_map_to
                    p_range = param.max - param.min
                    value = old_div(param.value - param.min, p_range) * 127
                    self.send_value((int(value)), force=True)
                    if self._parameter_to_map_to.min == -1 * self._parameter_to_map_to.max:
                        self._ring_mode_button.send_value(RING_PAN_VALUE, force=True)
                    elif self._parameter_to_map_to.is_quantized:
                        self._ring_mode_button.send_value(RING_SIN_VALUE, force=True)
                    else:
                        self._ring_mode_button.send_value(RING_VOL_VALUE, force=True)
                else:
                    self._ring_mode_button.send_value(RING_OFF_VALUE, force=True)

# okay decompiling ./MIDIRemoteScripts/_APC/RingedEncoderElement.pyc
