# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\SL_MkIII\caching_control_element.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 628 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import depends
from ableton.v2.control_surface import ControlElement
from .sysex import SET_PROPERTY_MSG_HEADER

class CachingControlElement(ControlElement):

    @depends(message_cache=None)
    def __init__(self, message_cache=None, *a, **k):
        (super().__init__)(*a, **k)
        self._message_cache = message_cache

    def send_midi(self, message, **_):
        self._message_cache(message[len(SET_PROPERTY_MSG_HEADER)[:-1]])

    def reset(self):
        pass

# okay decompiling ./MIDIRemoteScripts/SL_MkIII/caching_control_element.pyc
