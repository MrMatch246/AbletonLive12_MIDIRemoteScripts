# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\MomentaryModeObserver.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1807 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from . import Defaults

class MomentaryModeObserver(object):

    def __init__(self):
        object.__init__(self)
        self._controls = None
        self._mode_callback = None
        self._reset()

    def disconnect(self):
        self._reset()

    def set_mode_details(self, base_mode, controls, mode_callback=None):
        self._reset()
        if controls != None:
            self._controls = controls
            for control in self._controls:
                control.add_value_listener(self._control_changed)

        self._base_mode = base_mode
        self._mode_callback = mode_callback

    def is_mode_momentary(self):
        return self._controls_changed or self._timer_count >= Defaults.MOMENTARY_DELAY_TICKS

    def on_timer(self):
        self._timer_count += 1

    def _control_changed(self, value):
        if self._mode_callback == None or self._mode_callback() == self._base_mode:
            self._controls_changed = True

    def _release_controls(self):
        if self._controls != None:
            for control in self._controls:
                control.remove_value_listener(self._control_changed)

            self._controls = None

    def _reset(self):
        self._base_mode = -1
        self._controls_changed = False
        self._mode_callback = None
        self._timer_count = 0
        self._release_controls()

# okay decompiling ./MIDIRemoteScripts/_Framework/MomentaryModeObserver.pyc
