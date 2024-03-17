# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\SL_MkIII\color_sysex_element.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 401 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import nop
from ableton.v2.control_surface.elements import ColorSysexElement as ColorSysexElementBase

class ColorSysexElement(ColorSysexElementBase):

    class ProxiedInterface(ColorSysexElementBase.ProxiedInterface):
        set_light = nop

# okay decompiling ./MIDIRemoteScripts/SL_MkIII/color_sysex_element.pyc
