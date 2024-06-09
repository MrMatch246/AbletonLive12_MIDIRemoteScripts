# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\graindelay.py
# Size of source mod 2**32: 561 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator

class GrainDelayDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(GrainDelayDeviceDecorator, self).__init__)(*a, **k)
        self._add_on_off_option(name="Sync", pname="Delay Mode")
        self.register_disconnectables(self.options)

# okay decompiling ./MIDIRemoteScripts/Push2/graindelay.pyc
