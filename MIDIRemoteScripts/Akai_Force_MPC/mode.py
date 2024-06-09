# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Akai_Force_MPC\mode.py
# Size of source mod 2**32: 630 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.mode import Mode

class ExtendComboElementMode(Mode):

    def __init__(self, combo_pairs=None, *a, **k):
        (super(ExtendComboElementMode, self).__init__)(*a, **k)
        self._combo_pairs = combo_pairs

    def enter_mode(self):
        for combo, nested in self._combo_pairs:
            combo.register_control_element(nested)

    def leave_mode(self):
        for combo, nested in self._combo_pairs:
            combo.unregister_control_element(nested)

# okay decompiling ./MIDIRemoteScripts/Akai_Force_MPC/mode.pyc
