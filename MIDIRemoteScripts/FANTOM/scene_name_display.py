# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\FANTOM\scene_name_display.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 705 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .simple_display import SimpleDisplayElement, adjust_string, as_ascii
from .sysex import NAME_LENGTH, NAME_TERMINATOR

class SceneNameDisplayElement(SimpleDisplayElement):

    def display_data(self, data):
        data_to_send = [
         len(data)]
        for scene in data:
            data_to_send.extend(as_ascii(adjust_string(scene.name, NAME_LENGTH).strip()))
            data_to_send.append(NAME_TERMINATOR)

        self._message_to_send = self._message_header + tuple(data_to_send) + self._message_tail
        self._request_send_message()

# okay decompiling ./MIDIRemoteScripts/FANTOM/scene_name_display.pyc
