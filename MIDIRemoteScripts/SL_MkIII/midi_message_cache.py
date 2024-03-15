# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\SL_MkIII\midi_message_cache.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 725 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .sysex import NUM_SET_PROPERTY_HEADER_BYTES

class MidiMessageCache:

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._messages = []

    def __call__(self, message):
        self._messages = list(filter((lambda m: m[None[:NUM_SET_PROPERTY_HEADER_BYTES]] != message[None[:NUM_SET_PROPERTY_HEADER_BYTES]]), self._messages))
        self._messages.append(message)

    @property
    def messages(self):
        return self._messages

    def clear(self):
        self._messages = []

# okay decompiling ./MIDIRemoteScripts/SL_MkIII/midi_message_cache.pyc
