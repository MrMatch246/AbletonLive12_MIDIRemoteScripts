# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\elements\button_matrix.py
# Size of source mod 2**32: 1431 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import slicer, to_slice
from ableton.v2.control_surface.elements import ButtonMatrixElement as ButtonMatrixElementBase
from ...base import lazy_attribute, recursive_map
from ..display import Renderable

class ButtonMatrixElement(ButtonMatrixElementBase, Renderable):

    @property
    @slicer(2)
    def submatrix(self, col_slice, row_slice):
        col_slice = to_slice(col_slice)
        row_slice = to_slice(row_slice)
        rows = [row[col_slice] for row in self._orig_buttons[row_slice]]
        return ButtonMatrixElement(rows=rows)

    @lazy_attribute
    def renderable_state(self):
        if not any((isinstance(button, Renderable) for row in self._orig_buttons)):
            return
        matrix = recursive_map((lambda button: button.renderable_state if isinstance(button, Renderable) else None), self._orig_buttons)
        if len(matrix) == 1:
            return matrix[0]
        return matrix

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/elements/button_matrix.pyc
