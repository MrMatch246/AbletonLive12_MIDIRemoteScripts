# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Pro\TranslationComponent.py
# Size of source mod 2**32: 1491 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from functools import partial
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent as ControlSurfaceComponent

class TranslationComponent(ControlSurfaceComponent):

    def __init__(self, translated_channel, should_enable=True, should_reset=True, *a, **k):
        self._translated_channel = translated_channel
        self._should_enable = bool(should_enable)
        self._should_reset = should_reset
        (super(TranslationComponent, self).__init__)(*a, **k)

    def __getattr__(self, name):
        if len(name) > 4:
            if name[:4] == "set_":
                return partial(self._set_control_elements, name[4:])
        raise AttributeError(name)

    def _set_control_elements(self, name, control_elements):
        if bool(control_elements):
            buttons = control_elements
            for button in buttons:
                if button:
                    if self._should_reset:
                        button.reset()
                    else:
                        button.reset_state()
                    button.set_enabled(self._should_enable)
                    button.set_channel(self._translated_channel)

# okay decompiling ./MIDIRemoteScripts/Launchpad_Pro/TranslationComponent.pyc
