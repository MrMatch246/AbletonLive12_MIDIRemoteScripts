# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Axiom_DirectLink\DetailViewCntrlComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 3822 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ButtonElement import ButtonElement as ButtonElement
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent as ControlSurfaceComponent

class DetailViewCntrlComponent(ControlSurfaceComponent):

    def __init__(self):
        ControlSurfaceComponent.__init__(self)
        self._left_button = None
        self._right_button = None

    def disconnect(self):
        if self._left_button != None:
            self._left_button.remove_value_listener(self._nav_value)
            self._left_button = None
        if self._right_button != None:
            self._right_button.remove_value_listener(self._nav_value)
            self._right_button = None

    def set_device_nav_buttons(self, left_button, right_button):
        identify_sender = True
        if self._left_button != None:
            self._left_button.remove_value_listener(self._nav_value)
        self._left_button = left_button
        if self._left_button != None:
            self._left_button.add_value_listener(self._nav_value, identify_sender)
        if self._right_button != None:
            self._right_button.remove_value_listener(self._nav_value)
        self._right_button = right_button
        if self._right_button != None:
            self._right_button.add_value_listener(self._nav_value, identify_sender)
        self.update()

    def on_enabled_changed(self):
        self.update()

    def update(self):
        super(DetailViewCntrlComponent, self).update()
        if self.is_enabled():
            if self._left_button != None:
                self._left_button.turn_off()
            if self._right_button != None:
                self._right_button.turn_off()

    def _nav_value(self, value, sender):
        if self.is_enabled():
            if not sender.is_momentary() or value != 0:
                modifier_pressed = True
                if not (self.application().view.is_view_visible("Detail") and self.application().view.is_view_visible("Detail/DeviceChain")):
                    self.application().view.show_view("Detail")
                    self.application().view.show_view("Detail/DeviceChain")
                else:
                    direction = Live.Application.Application.View.NavDirection.left
                    if sender == self._right_button:
                        direction = Live.Application.Application.View.NavDirection.right
                    self.application().view.scroll_view(direction, "Detail/DeviceChain", not modifier_pressed)

# okay decompiling ./MIDIRemoteScripts/Axiom_DirectLink/DetailViewCntrlComponent.pyc
