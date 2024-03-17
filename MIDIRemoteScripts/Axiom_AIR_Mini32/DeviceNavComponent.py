# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Axiom_AIR_Mini32\DeviceNavComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 2465 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent as ControlSurfaceComponent

class DeviceNavComponent(ControlSurfaceComponent):

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

    def _nav_value(self, value, sender):
        if self.is_enabled():
            if not sender.is_momentary() or value != 0:
                app_view = self.application().view
                if not (app_view.is_view_visible("Detail") and app_view.is_view_visible("Detail/DeviceChain")):
                    app_view.show_view("Detail")
                    app_view.show_view("Detail/DeviceChain")
                else:
                    directions = Live.Application.Application.View.NavDirection
                    direction = directions.right if sender == self._right_button else directions.left
                    modifier_pressed = True
                    app_view.scroll_view(direction, "Detail/DeviceChain", not modifier_pressed)

# okay decompiling ./MIDIRemoteScripts/Axiom_AIR_Mini32/DeviceNavComponent.pyc
