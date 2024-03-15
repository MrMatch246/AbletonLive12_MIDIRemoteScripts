# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\saturator.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 624 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator

class SaturatorDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(SaturatorDeviceDecorator, self).__init__)(*a, **k)
        self._add_on_off_option(name="Soft Clip", pname="Soft Clip")
        self._add_on_off_option(name="Color", pname="Color")
        self.register_disconnectables(self.options)

# okay decompiling ./MIDIRemoteScripts/Push2/saturator.pyc
