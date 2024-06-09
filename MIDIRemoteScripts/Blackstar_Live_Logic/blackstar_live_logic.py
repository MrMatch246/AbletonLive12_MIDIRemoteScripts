# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Blackstar_Live_Logic\blackstar_live_logic.py
# Size of source mod 2**32: 1883 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens
from ableton.v2.control_surface import Layer, SimpleControlSurface
from ableton.v2.control_surface.midi import is_sysex
from .elements import Elements
from .looper import LooperComponent

class Blackstar_Live_Logic(SimpleControlSurface):

    def __init__(self, *a, **k):
        (super(Blackstar_Live_Logic, self).__init__)(*a, **k)
        with self.component_guard():
            self._elements = Elements()
            self._looper = LooperComponent(name="Looper",
              is_enabled=False,
              layer=Layer(foot_switches=(self._elements.foot_switches),
              time_display=(self._elements.time_display)))

    def disconnect(self):
        super(Blackstar_Live_Logic, self).disconnect()
        self._elements.live_integration_mode_switch.send_value(0)

    def port_settings_changed(self):
        self._elements.live_integration_mode_switch.send_value(1)
        self.schedule_message(1, self._looper.set_enabled, True)
        self.schedule_message(2, self.refresh_state)

    def process_midi_bytes(self, midi_bytes, midi_processor):
        if is_sysex(midi_bytes):
            return
        return super(Blackstar_Live_Logic, self).process_midi_bytes(midi_bytes, midi_processor)

# okay decompiling ./MIDIRemoteScripts/Blackstar_Live_Logic/blackstar_live_logic.pyc
