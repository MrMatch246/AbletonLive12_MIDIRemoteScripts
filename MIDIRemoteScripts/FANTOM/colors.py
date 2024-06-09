# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\FANTOM\colors.py
# Size of source mod 2**32: 1294 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.elements import SimpleColor

class Basic:
    OFF = SimpleColor(0)
    ON = SimpleColor(1)
    DISABLED = SimpleColor(2)


class Rgb:
    YELLOW = SimpleColor(3)
    LIGHT_BLUE = SimpleColor(6)
    RED = SimpleColor(13)
    ORANGE = SimpleColor(14)
    GREEN = SimpleColor(4)
    DARK_BLUE = SimpleColor(63)


STOPPED = SimpleColor(4)
TRIGGERED_PLAY = SimpleColor(7)

class Skin:

    class DefaultButton:
        Disabled = Basic.DISABLED

    class Session:
        SlotRecordButton = SimpleColor(2)
        SlotLacksStop = SimpleColor(5)
        SlotTriggeredPlay = SimpleColor(1)
        SlotTriggeredRecord = SimpleColor(3)
        ClipStopped = STOPPED
        ClipTriggeredPlay = TRIGGERED_PLAY
        ClipTriggeredRecord = SimpleColor(9)
        ClipPlaying = SimpleColor(6)
        ClipRecording = SimpleColor(8)
        Scene = STOPPED
        SceneTriggered = TRIGGERED_PLAY

    class DrumGroup:
        PadFilled = Rgb.YELLOW
        PadSelected = Rgb.LIGHT_BLUE
        PadMuted = Rgb.ORANGE
        PadMutedSelected = Rgb.LIGHT_BLUE
        PadSoloed = Rgb.DARK_BLUE
        PadSoloedSelected = Rgb.LIGHT_BLUE

# okay decompiling ./MIDIRemoteScripts/FANTOM/colors.pyc
