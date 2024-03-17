# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Komplete_Kontrol\physical_display_element.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 647 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import str
from itertools import chain
from ableton.v2.control_surface.elements import PhysicalDisplayElement as PhysicalDisplayElementBase

class PhysicalDisplayElement(PhysicalDisplayElementBase):

    def _build_display_message(self, display):
        return chain(*map((lambda x: self._translate_string(str(x).strip())), display._logical_segments))

    def _request_send_message(self):
        self._send_message()

# okay decompiling ./MIDIRemoteScripts/_Komplete_Kontrol/physical_display_element.pyc
