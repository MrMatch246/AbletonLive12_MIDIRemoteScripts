# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\novation\simple_device_navigation.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1342 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ButtonControl
NavDirection = Live.Application.Application.View.NavDirection

class SimpleDeviceNavigationComponent(Component):
    next_button = ButtonControl(color="Device.Navigation",
      pressed_color="Device.NavigationPressed")
    prev_button = ButtonControl(color="Device.Navigation",
      pressed_color="Device.NavigationPressed")

    @next_button.pressed
    def next_button(self, value):
        self._scroll_device_chain(NavDirection.right)

    @prev_button.pressed
    def prev_button(self, value):
        self._scroll_device_chain(NavDirection.left)

    def _scroll_device_chain(self, direction):
        view = self.application.view
        if view.is_view_visible("Detail"):
            if not view.is_view_visible("Detail/DeviceChain"):
                view.show_view("Detail")
                view.show_view("Detail/DeviceChain")
        else:
            view.scroll_view(direction, "Detail/DeviceChain", False)

# okay decompiling ./MIDIRemoteScripts/novation/simple_device_navigation.pyc
