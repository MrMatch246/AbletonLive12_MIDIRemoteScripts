# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\iRig_Keys_IO\scroll.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 710 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import nop
from ableton.v2.control_surface.components import ScrollComponent as ScrollComponentBase
from ableton.v2.control_surface.control import EncoderControl

class ScrollComponent(ScrollComponentBase):
    scroll_encoder = EncoderControl()

    @scroll_encoder.value
    def scroll_encoder(self, value, _):
        scroll_step = nop
        if value > 0 and self.can_scroll_down():
            scroll_step = self._do_scroll_down
        elif value < 0:
            if self.can_scroll_up():
                scroll_step = self._do_scroll_up
        scroll_step()

# okay decompiling ./MIDIRemoteScripts/iRig_Keys_IO/scroll.pyc
