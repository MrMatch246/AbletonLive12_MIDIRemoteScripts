# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mkII\session.py
# Size of source mod 2**32: 514 bytes
from __future__ import absolute_import, print_function, unicode_literals
from KeyLab_Essential.session import SceneComponent as SceneComponentBase
from KeyLab_Essential.session import SessionComponent as SessionComponentBase
from .clip_slot import ClipSlotComponent

class SceneComponent(SceneComponentBase):
    clip_slot_component_type = ClipSlotComponent


class SessionComponent(SessionComponentBase):
    scene_component_type = SceneComponent

# okay decompiling ./MIDIRemoteScripts/KeyLab_mkII/session.pyc
