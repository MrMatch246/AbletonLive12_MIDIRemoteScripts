# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\display\view\util.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 542 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import List, Optional
from ..state import State

def suppress_notifications(state: State, exclude: Optional[List[str]]=None):
    if exclude is None:
        exclude = []
    for notification in getattr(state, "_notifications", set()) - set(exclude):
        setattr(state, notification, None)

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/display/view/util.pyc