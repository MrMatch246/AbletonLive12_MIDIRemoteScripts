# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_MK2\ControlElementUtils.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1903 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ButtonElement import ButtonElement as ButtonElement
from _Framework.ComboElement import ComboElement as ComboElement
from _Framework.ComboElement import MultiElement as MultiElementBase
from _Framework.Dependency import depends
from _Framework.InputControlElement import MIDI_NOTE_TYPE
from _Framework.Resource import PrioritizedResource

@depends(skin=None)
def make_button(identifier, channel, name, msg_type=MIDI_NOTE_TYPE, skin=None, is_modifier=False):
    return ButtonElement(True,
      msg_type,
      channel,
      identifier,
      skin=skin,
      name=name,
      resource_type=(PrioritizedResource if is_modifier else None))


def with_modifier(modifier, button):
    return ComboElement(button, modifiers=[modifier])


class MultiElement(MultiElementBase):

    def __init__(self, *a, **k):
        (super(MultiElement, self).__init__)(*a, **k)
        self._is_pressed = False

    def is_pressed(self):
        return self._is_pressed

    def on_nested_control_element_value(self, value, control):
        self._is_pressed = bool(value)
        super(MultiElement, self).on_nested_control_element_value(value, control)


class FilteringMultiElement(MultiElement):

    def __init__(self, controls, feedback_channels=None, **k):
        (super(MultiElement, self).__init__)(*controls, **k)
        self._feedback_channels = feedback_channels

    def send_value(self, value):
        for control in self.owned_control_elements():
            if control.message_channel() in self._feedback_channels:
                control.send_value(value)

    def set_light(self, value):
        for control in self.owned_control_elements():
            if control.message_channel() in self._feedback_channels:
                control.set_light(value)

# okay decompiling ./MIDIRemoteScripts/Launchpad_MK2/ControlElementUtils.pyc
