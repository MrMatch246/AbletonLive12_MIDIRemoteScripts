# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\session_navigation.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 969 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase
from .util import skin_scroll_buttons

class SessionNavigationComponent(SessionNavigationComponentBase):

    def __init__(self, *a, **k):
        (super(SessionNavigationComponent, self).__init__)(*a, **k)
        skin_scroll_buttons(self._vertical_banking, "Session.Navigation", "Session.NavigationPressed")
        skin_scroll_buttons(self._horizontal_banking, "Session.Navigation", "Session.NavigationPressed")
        skin_scroll_buttons(self._vertical_paginator, "Session.Navigation", "Session.NavigationPressed")
        skin_scroll_buttons(self._horizontal_paginator, "Session.Navigation", "Session.NavigationPressed")

# okay decompiling ./MIDIRemoteScripts/novation/session_navigation.pyc
