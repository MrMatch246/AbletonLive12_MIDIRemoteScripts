# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\components\loop_selector.py
# Size of source mod 2**32: 10733 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import depends, listenable_property, listens
from ...live import action, get_bar_length, is_clip_playing, liveobj_changed, liveobj_valid
from .. import Component
from ..controls import ButtonControl, control_matrix
from ..display import Renderable
from ..skin import LiveObjSkinEntry
from .clipboard import BufferedClipboardComponent

def quantize_page_time(page_time, bar_length):
    return int(page_time / bar_length) * bar_length


class LoopSelectorComponent(Component, Renderable):
    next_page_button = ButtonControl(color="LoopSelector.Navigation",
      pressed_color="LoopSelector.NavigationPressed")
    prev_page_button = ButtonControl(color="LoopSelector.Navigation",
      pressed_color="LoopSelector.NavigationPressed")
    delete_button = ButtonControl(None)
    matrix = control_matrix(ButtonControl)

    @depends(target_track=None, sequencer_clip=None)
    def __init__(self, name='Loop_Selector', target_track=None, sequencer_clip=None, paginator=None, clipboard_component_type=None, *a, **k):
        (super().__init__)(a, name=name, **k)
        self._pressed_matrix_indices = []
        self._target_track = target_track
        self._LoopSelectorComponent__on_target_track_color_changed.subject = target_track
        self._clip = None
        self._last_bar_length = sequencer_clip.bar_length
        self._sequencer_clip = sequencer_clip
        self._LoopSelectorComponent__on_sequencer_clip_changed.subject = sequencer_clip
        self.register_slot(sequencer_clip, self._rectify_page_time, "bar_length")
        self.register_slot(sequencer_clip, self._update_matrix, "length")
        self._paginator = paginator
        self._last_page_length = paginator.page_length
        self.register_slot(paginator, self._rectify_page_time, "page_length")
        self.register_slot(paginator, self.update, "page_time")
        self.register_slot(self.song, self._update_matrix, "session_record")
        self.register_slot(self.song, self._update_matrix, "is_playing")
        clipboard_component_type = clipboard_component_type or NoteRegionClipboardComponent
        self._clipboard = clipboard_component_type(parent=self)
        self.set_clip(self._sequencer_clip.clip)

    @listenable_property
    def clipboard(self):
        return self._clipboard

    @property
    def bar_length(self):
        return get_bar_length(clip=(self._clip))

    def set_matrix(self, matrix):
        self.matrix.set_control_element(matrix)
        self._update_matrix()

    def set_copy_button(self, button):
        self._clipboard.set_copy_button(button)

    def set_clip(self, clip):
        if liveobj_changed(clip, self._clip):
            self._LoopSelectorComponent__on_playing_position_changed.subject = clip
            self._LoopSelectorComponent__on_playing_status_changed.subject = clip
            self._clip = clip
            self._clipboard.set_clip(clip)
            if clip:
                if self._paginator.can_change_page:
                    self._paginator.page_time = clip.loop_start
                self.update()

    @matrix.pressed
    def matrix(self, button):
        bar_length = self.bar_length
        if self.delete_button.is_pressed:
            if action.delete_notes_in_range(self._clip, button.index * bar_length, bar_length):
                self.notify(self.notifications.Notes.delete)
            else:
                self.notify(self.notifications.Notes.error_no_notes_to_delete)
        elif self._clipboard.is_copying:
            self._update_clipboard(button)
        else:
            self._pressed_matrix_indices.append(button.index)
            if len(self._pressed_matrix_indices) > 1:
                action.set_loop_position(self._clip, min(self._pressed_matrix_indices) * bar_length, max(self._pressed_matrix_indices) * bar_length + bar_length)
            self._paginator.page_time = self._pressed_matrix_indices[0] * bar_length

    @matrix.released
    def matrix(self, button):
        if self._clipboard.is_copying:
            self._update_clipboard(button)
        elif button.index in self._pressed_matrix_indices:
            self._pressed_matrix_indices.remove(button.index)

    @matrix.double_clicked
    def matrix(self, button):
        if not self._clipboard.is_copying:
            start = button.index * self.bar_length
            action.set_loop_position(self._clip, start, start + self.bar_length)

    @next_page_button.pressed
    def next_page_button(self, _):
        self._increment_page_time(1)

    @prev_page_button.pressed
    def prev_page_button(self, _):
        self._increment_page_time(-1)

    def _increment_page_time(self, delta):
        self._paginator.page_time = max(0.0, self._paginator.page_length * delta + self._paginator.page_time)

    def _rectify_page_time(self):
        if self._paginator.page_length > self._last_page_length or self.bar_length != self._last_bar_length:
            self._paginator.page_time = quantize_page_time(self._paginator.page_time, self.bar_length)
        self._last_page_length = self._paginator.page_length
        self._last_bar_length = self.bar_length
        self.update()

    def _has_clip(self):
        return liveobj_valid(self._clip)

    def _make_room_for_region(self, region_end):
        if region_end > self._clip.loop_end:
            action.set_loop_end(self._clip, region_end)

    def _update_clipboard(self, button):
        bar_length = self.bar_length
        region_start = button.index * bar_length
        any_button_pressed = any((button.is_pressed for button in self.matrix))
        if self._clipboard.has_content:
            if not any_button_pressed:
                self._make_room_for_region(region_start + self._clipboard.buffer[-1])
                self._clipboard.paste(region_start)
        elif button.is_pressed:
            self._clipboard.extend_buffer((region_start, region_start + bar_length))
        elif not any_button_pressed:
            self._clipboard.copy(self._clipboard.buffer)

    def update(self):
        super().update()
        self._update_matrix()
        self._update_page_buttons()

    def _update_matrix(self):
        has_clip = self._has_clip()
        for button in self.matrix:
            button.enabled = has_clip

        if has_clip:
            bar_length = self.bar_length
            loop_start = self._clip.loop_start
            loop_end = self._clip.loop_end
            playing_page = int(self._clip.playing_position / bar_length)
            editing_page = int(self._paginator.page_time / bar_length)
            for (index, button) in enumerate(self.matrix):
                self._update_matrix_button(button, index == editing_page, is_clip_playing(self._clip) and index == playing_page, loop_start <= button.index * bar_length < loop_end)

    def _update_matrix_button(self, button, selected, playing, inside_loop):
        color = "OutsideLoop"
        if playing:
            color = "PlayheadRecord" if self.song.session_record else "Playhead"
        elif inside_loop:
            color = "InsideLoopSelected" if selected else "InsideLoop"
        elif selected:
            color = "OutsideLoopSelected"
        button.color = LiveObjSkinEntry("LoopSelector.{}".format(color), self._target_track.target_track)

    def _update_page_buttons(self):
        has_clip = self._has_clip()
        self.prev_page_button.enabled = has_clip and self._paginator.page_time > 0.0
        self.next_page_button.enabled = has_clip

    @listens("clip")
    def __on_sequencer_clip_changed(self):
        self.set_clip(self._sequencer_clip.clip)

    @listens("playing_position")
    def __on_playing_position_changed(self):
        self._update_matrix()

    @listens("playing_status")
    def __on_playing_status_changed(self):
        self._update_matrix()

    @listens("target_track.color")
    def __on_target_track_color_changed(self):
        self._update_matrix()


class NoteRegionClipboardComponent(BufferedClipboardComponent):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._clip = None

    def set_clip(self, clip):
        self._clip = clip
        self.clear()

    def extend_buffer(self, obj):
        super().extend_buffer(obj)
        self._buffer = [
         min(self._buffer), max(self._buffer)]
        self.notify(self.notifications.Notes.CopyPaste.copy)

    def _do_paste(self, obj):
        self._clip.duplicate_region(self._buffer[0], self._buffer[1], obj, -1)
        self.notify(self.notifications.Notes.CopyPaste.paste)
        return True

    def _is_source_valid(self):
        return super()._is_source_valid() and liveobj_valid(self._clip)

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/components/loop_selector.pyc
