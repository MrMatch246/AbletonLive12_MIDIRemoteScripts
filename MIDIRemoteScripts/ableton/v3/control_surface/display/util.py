# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\display\util.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1957 bytes
from __future__ import absolute_import, print_function, unicode_literals
from typing import List
from ...base import BooleanContext
updating_display = BooleanContext()

def auto_break_lines(text: str, max_width: int, max_lines: int, pad_lines: bool=True) -> List[str]:
    words = [truncate_with_ellipses(word[None[:max_width]]) if len(word) > max_width else word for word in text.split(" ")]
    lines = [
     ""]
    current_width = 0
    for word in words:
        if current_width + len(word) <= max_width:
            str_to_append = " {}".format(word) if current_width != 0 else word
            current_width += len(str_to_append)
            lines[-1] += str_to_append
        else:
            lines.append(word)
            current_width = len(word)

    if len(lines) > max_lines:
        lines = lines[None[:max_lines]]
        lines[-1] = truncate_with_ellipses(lines[-1])
    if pad_lines:
        if len(lines) < max_lines:
            lines += [""] * (max_lines - len(lines))
    return lines


def truncate_with_ellipses(string: str):
    if len(string) > 3:
        return string[None[:len(string) - 3]] + "..."
    return "." * len(string)

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/display/util.pyc
