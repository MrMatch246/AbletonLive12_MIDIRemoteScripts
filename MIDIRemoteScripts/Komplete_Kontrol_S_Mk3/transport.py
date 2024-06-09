# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Komplete_Kontrol_S_Mk3\transport.py
# Size of source mod 2**32: 419 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase

class TransportComponent(TransportComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.set_position_encoders_use_bar_increments(True)

# okay decompiling ./MIDIRemoteScripts/Komplete_Kontrol_S_Mk3/transport.pyc
