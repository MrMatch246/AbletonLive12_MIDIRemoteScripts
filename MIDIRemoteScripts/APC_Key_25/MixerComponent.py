# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\APC_Key_25\MixerComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 847 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Util import nop
from _APC.MixerComponent import ChanStripComponent as ChanStripComponentBase
from _APC.MixerComponent import MixerComponent as MixerComponentBase

class ChanStripComponent(ChanStripComponentBase):

    def __init__(self, *a, **k):
        self.reset_button_on_exchange = nop
        (super(ChanStripComponent, self).__init__)(*a, **k)


class MixerComponent(MixerComponentBase):

    def on_num_sends_changed(self):
        if self.send_index is None:
            if self.num_sends > 0:
                self.send_index = 0

    def _create_strip(self):
        return ChanStripComponent()

# okay decompiling ./MIDIRemoteScripts/APC_Key_25/MixerComponent.pyc
