# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_MK2\BackgroundComponent.py
# Size of source mod 2**32: 989 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase

class BackgroundComponent(BackgroundComponentBase):

    def _clear_control(self, name, control):
        if control:
            control.add_value_listener(self._on_value_listener)
        super(BackgroundComponent, self)._clear_control(name, control)

    def _on_value_listener(self, *a, **k):
        pass


class TranslatingBackgroundComponent(BackgroundComponent):

    def __init__(self, translation_channel=0, *a, **k):
        (super(TranslatingBackgroundComponent, self).__init__)(*a, **k)
        self._translation_channel = translation_channel

    def _clear_control(self, name, control):
        if control:
            control.set_channel(self._translation_channel)
        super(TranslatingBackgroundComponent, self)._clear_control(name, control)

# okay decompiling ./MIDIRemoteScripts/Launchpad_MK2/BackgroundComponent.pyc
