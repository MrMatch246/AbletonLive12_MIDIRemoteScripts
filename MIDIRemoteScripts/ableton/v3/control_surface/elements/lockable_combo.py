# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\elements\lockable_combo.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 610 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import ComboElement

class LockableComboElement(ComboElement):

    def _modifier_is_valid(self, mod):
        return self.owns_control_element(mod) and (mod.is_pressed or hasattr(mod, "is_locked") and mod.is_locked)

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/elements/lockable_combo.pyc
