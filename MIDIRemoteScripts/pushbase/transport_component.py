# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\transport_component.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 458 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import components

class TransportComponent(components.TransportComponent):

    def __init__(self, *a, **k):
        (super(TransportComponent, self).__init__)(*a, **k)
        self._metronome_toggle.view_transform = lambda v:         if v:
"Metronome.On" # Avoid dead code: "Metronome.Off"

# okay decompiling ./MIDIRemoteScripts/pushbase/transport_component.pyc
