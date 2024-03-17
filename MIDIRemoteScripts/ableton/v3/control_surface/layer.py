# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\layer.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 695 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Layer as LayerBaseClass

class Layer(LayerBaseClass):

    def on_received(self, client, *a, **k):
        (super().on_received)(client, *a, **k)
        client.num_layers += 1

    def on_lost(self, client):
        super().on_lost(client)
        client.num_layers -= 1

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/layer.pyc
