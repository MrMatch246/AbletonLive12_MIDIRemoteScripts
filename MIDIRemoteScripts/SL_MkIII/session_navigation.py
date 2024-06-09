# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\SL_MkIII\session_navigation.py
# Size of source mod 2**32: 547 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase

class SessionNavigationComponent(SessionNavigationComponentBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._vertical_banking.scroll_up_button.color = "Session.Navigation"
        self._vertical_banking.scroll_down_button.color = "Session.Navigation"

# okay decompiling ./MIDIRemoteScripts/SL_MkIII/session_navigation.pyc
