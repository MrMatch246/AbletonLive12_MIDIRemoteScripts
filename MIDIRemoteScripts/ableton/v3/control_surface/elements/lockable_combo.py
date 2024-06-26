# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\elements\lockable_combo.py
# Size of source mod 2**32: 610 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import ComboElement

class LockableComboElement(ComboElement):

    def _modifier_is_valid(self, mod):
        return self.owns_control_element(mod) and (mod.is_pressed) or ((hasattr(mod, "is_locked")) and (mod.is_locked))

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/elements/lockable_combo.pyc
