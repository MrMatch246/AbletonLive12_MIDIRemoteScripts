# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\components\zoom.py
# Size of source mod 2**32: 3442 bytes
from __future__ import absolute_import, print_function, unicode_literals
from Live.Application import Application as Application
from .. import Component
from . import Scrollable, ScrollComponent
NavDirection = Application.View.NavDirection

class ZoomScroller(ScrollComponent, Scrollable):

    def __init__(self, view_name, vertical=True, zoom_all_tracks=True, *a, **k):
        (super().__init__)(
 self, *a, scroll_skin_name="Zoom.{}".format("Vertical" if vertical else "Horizontal"), **k)
        self._view_name = view_name
        self._is_vertical = vertical
        self._zoom_all_tracks = zoom_all_tracks

    def can_scroll_up(self):
        return True

    def can_scroll_down(self):
        return True

    def scroll_up(self):
        self.application.view.zoom_view(NavDirection.up if self._is_vertical else NavDirection.left, self._view_name, self._zoom_all_tracks)

    def scroll_down(self):
        self.application.view.zoom_view(NavDirection.down if self._is_vertical else NavDirection.right, self._view_name, self._zoom_all_tracks)


class ZoomComponent(Component):

    def __init__(self, name='Zoom', arrangement_only=False, zoom_all_tracks=True, *a, **k):
        (super().__init__)(a, name=name, **k)
        view_name = "Arranger" if arrangement_only else " "
        (self._vertical_zoom, self._horizontal_zoom) = self.add_children(ZoomScroller(view_name, zoom_all_tracks=zoom_all_tracks), ZoomScroller(view_name, vertical=False))

    def set_vertical_zoom_encoder(self, encoder):
        self._vertical_zoom.set_scroll_encoder(encoder)

    def set_vertical_zoom_in_button(self, button):
        self._vertical_zoom.set_scroll_down_button(button)

    def set_vertical_zoom_out_button(self, button):
        self._vertical_zoom.set_scroll_up_button(button)

    def set_horizontal_zoom_encoder(self, encoder):
        self._horizontal_zoom.set_scroll_encoder(encoder)

    def set_horizontal_zoom_in_button(self, button):
        self._horizontal_zoom.set_scroll_down_button(button)

    def set_horizontal_zoom_out_button(self, button):
        self._horizontal_zoom.set_scroll_up_button(button)

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/components/zoom.pyc
