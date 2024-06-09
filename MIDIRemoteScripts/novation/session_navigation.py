# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\session_navigation.py
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
