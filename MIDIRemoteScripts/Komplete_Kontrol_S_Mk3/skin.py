# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Komplete_Kontrol_S_Mk3\skin.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 394 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import BasicColors

class Skin:

    class Transport:
        TapTempo = BasicColors.ON

    class UndoRedo:
        Undo = BasicColors.ON
        Redo = BasicColors.ON

    class ClipActions:
        Quantize = BasicColors.ON

# okay decompiling ./MIDIRemoteScripts/Komplete_Kontrol_S_Mk3/skin.pyc