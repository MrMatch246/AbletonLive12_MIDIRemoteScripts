# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK3\rgb_button.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1017 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import ButtonElement

class RgbButtonElement(ButtonElement):

    def __init__(self, *a, **k):
        self._led_channel = k.pop("led_channel", 0)
        (super(RgbButtonElement, self).__init__)(*a, **k)

    def _do_send_value(self, value, channel=None):
        super(RgbButtonElement, self)._do_send_value(value, channel=(self._led_channel))

# okay decompiling ./MIDIRemoteScripts/Launchkey_MK3/rgb_button.pyc
