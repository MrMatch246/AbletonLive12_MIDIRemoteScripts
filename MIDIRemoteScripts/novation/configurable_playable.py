# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\configurable_playable.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 554 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import PlayableComponent

class ConfigurablePlayableComponent(PlayableComponent):

    def __init__(self, translation_channel, *a, **k):
        self._translation_channel = translation_channel
        (super(ConfigurablePlayableComponent, self).__init__)(*a, **k)

    def _note_translation_for_button(self, button):
        return (
         button.identifier, self._translation_channel)

# okay decompiling ./MIDIRemoteScripts/novation/configurable_playable.pyc
