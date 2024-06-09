# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\components\clipboard.py
# Size of source mod 2**32: 5007 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import is_iterable, listenable_property
from .. import Component
from ..controls import ButtonControl
from ..display import Renderable

class ClipboardComponent(Component, Renderable):
    copy_button = ButtonControl(color="Clipboard.Empty",
      on_color="Clipboard.Filled",
      pressed_color="Clipboard.CopyPressed")
    has_content = listenable_property.managed(False)
    is_copying = listenable_property.managed(False)

    def __init__(self, name='Clipboard', *a, **k):
        (super().__init__)(a, name=name, **k)
        self._source_obj = None
        self._did_paste = False
        self._pending_clear = False
        self.register_clipboard()

    def set_copy_button(self, button):
        self.clear()
        self.copy_button.set_control_element(button)

    def copy_or_paste(self, obj):
        if self.has_content:
            self.paste(obj)
        else:
            self.copy(obj)

    def copy(self, obj):
        if not self.any_clipboard_has_content:
            self._source_obj = self._do_copy(obj)
            self.update()

    def paste(self, obj):
        if self._is_source_valid():
            self._did_paste = self._do_paste(obj)
            if self._did_paste:
                self.copy_button.is_pressed or self.clear()
        else:
            self.clear(notify=True)

    def clear(self, notify=False):
        self._source_obj = None
        self._pending_clear = False
        self.update()
        if notify:
            self.notify(self.notifications.Clipboard.clear)

    @copy_button.pressed
    def copy_button(self, _):
        self._pending_clear = self.has_content
        self.is_copying = True

    @copy_button.released
    def copy_button(self, _):
        if self._did_paste or self._pending_clear:
            self.clear(notify=True)
        else:
            self.is_copying = self.has_content

    def update(self):
        super().update()
        self._did_paste = False
        self.has_content = self._is_source_valid()
        self.is_copying = self.has_content
        self.copy_button.is_on = self.has_content

    def _do_copy(self, obj):
        self._source_obj = obj
        return self._source_obj

    def _do_paste(self, obj):
        self._did_paste = obj is not None
        return self._did_paste

    def _is_source_valid(self):
        return self._source_obj is not None


class BufferedClipboardComponent(ClipboardComponent):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._buffer = []

    @property
    def buffer(self):
        return self._buffer

    def clear(self, notify=False):
        self._buffer = []
        super().clear(notify=notify)

    def append_buffer(self, obj):
        self._buffer.append(obj)

    def extend_buffer(self, obj):
        self._buffer.extend(obj)

    def _is_source_valid(self):
        return bool(self._buffer)

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/components/clipboard.pyc
