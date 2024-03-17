# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\APC20\BackgroundComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 595 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase
from _Framework.Util import nop

class BackgroundComponent(BackgroundComponentBase):

    def _clear_control(self, name, control):
        if control:
            control.add_value_listener(nop)
        elif name in self._control_map:
            self._control_map[name].remove_value_listener(nop)
        super(BackgroundComponent, self)._clear_control(name, control)

# okay decompiling ./MIDIRemoteScripts/APC20/BackgroundComponent.pyc
