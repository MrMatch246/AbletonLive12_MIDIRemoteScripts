# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\OpenLabs\SpecialTransportComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 4549 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import Live
from _Framework.ButtonElement import ButtonElement as ButtonElement
from _Framework.EncoderElement import EncoderElement as EncoderElement
from _Framework.InputControlElement import *
from _Framework.TransportComponent import TransportComponent as TransportComponent

class SpecialTransportComponent(TransportComponent):

    def __init__(self):
        TransportComponent.__init__(self)
        self._undo_button = None
        self._redo_button = None
        self._bts_button = None

    def disconnect(self):
        TransportComponent.disconnect(self)
        if self._undo_button != None:
            self._undo_button.remove_value_listener(self._undo_value)
            self._undo_button = None
        if self._redo_button != None:
            self._redo_button.remove_value_listener(self._redo_value)
            self._redo_button = None
        if self._bts_button != None:
            self._bts_button.remove_value_listener(self._bts_value)
            self._bts_button = None

    def set_undo_button(self, undo_button):
        if undo_button != self._undo_button:
            if self._undo_button != None:
                self._undo_button.remove_value_listener(self._undo_value)
            self._undo_button = undo_button
            if self._undo_button != None:
                self._undo_button.add_value_listener(self._undo_value)
            self.update()

    def set_redo_button(self, redo_button):
        if redo_button != self._redo_button:
            if self._redo_button != None:
                self._redo_button.remove_value_listener(self._redo_value)
            self._redo_button = redo_button
            if self._redo_button != None:
                self._redo_button.add_value_listener(self._redo_value)
            self.update()

    def set_bts_button(self, bts_button):
        if bts_button != self._bts_button:
            if self._bts_button != None:
                self._bts_button.remove_value_listener(self._bts_value)
            self._bts_button = bts_button
            if self._bts_button != None:
                self._bts_button.add_value_listener(self._bts_value)
            self.update()

    def _undo_value(self, value):
        if not (self.is_enabled() and value != 0 or self._undo_button.is_momentary()):
            if self.song().can_undo:
                self.song().undo()

    def _redo_value(self, value):
        if not (self.is_enabled() and value != 0 or self._redo_button.is_momentary()):
            if self.song().can_redo:
                self.song().redo()

    def _bts_value(self, value):
        if self.is_enabled():
            if not (value != 0 or self._bts_button.is_momentary()):
                self.song().current_song_time = 0.0

# okay decompiling ./MIDIRemoteScripts/OpenLabs/SpecialTransportComponent.pyc
