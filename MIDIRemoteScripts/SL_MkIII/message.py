# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\SL_MkIII\message.py
# Size of source mod 2**32: 533 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Component
from .control import TextDisplayControl
NUM_MESSAGE_SEGMENTS = 2

class MessageComponent(Component):
    display = TextDisplayControl(segments=(('', ) * NUM_MESSAGE_SEGMENTS))

    def __call__(self, *messages):
        for index, message in zip(range(NUM_MESSAGE_SEGMENTS), messages):
            self.display[index] = message if message else ""

# okay decompiling ./MIDIRemoteScripts/SL_MkIII/message.pyc
