# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\session_ring_selection_linking.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 394 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import SessionRingSelectionLinking as SessionRingSelectionLinkingBase

class SessionRingSelectionLinking(SessionRingSelectionLinkingBase):

    def _current_track(self):
        return self._session_ring.selected_item

# okay decompiling ./MIDIRemoteScripts/Push2/session_ring_selection_linking.pyc
