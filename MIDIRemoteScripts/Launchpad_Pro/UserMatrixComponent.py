# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Pro\UserMatrixComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 716 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.ControlSurfaceComponent as ControlSurfaceComponent

def _disable_control(control):
    for button in control:
        button.set_enabled(False)


class UserMatrixComponent(ControlSurfaceComponent):

    def __getattr__(self, name):
        if len(name) > 4:
            if name[None[:4]] == "set_":
                return _disable_control
        raise AttributeError(name)

# okay decompiling ./MIDIRemoteScripts/Launchpad_Pro/UserMatrixComponent.pyc
