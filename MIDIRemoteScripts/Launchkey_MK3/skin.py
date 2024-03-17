# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK3\skin.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 873 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Skin, merge_skins
from novation.colors import Mono, Rgb
from novation.skin import skin as base_skin

class Colors:

    class DefaultButton:
        On = Mono.ON

    class TrackNavigation:
        On = Mono.HALF
        Pressed = Mono.ON

    class Device:
        Navigation = Rgb.PURPLE_HALF
        NavigationPressed = Rgb.PURPLE

    class DrumGroup:
        PadSelected = Rgb.WHITE
        PadSelectedNotSoloed = Rgb.WHITE
        PadMutedSelected = Rgb.WHITE
        PadSoloedSelected = Rgb.WHITE

    class Mode:

        class Device:

            class Bank:
                Selected = Rgb.PURPLE
                Available = Rgb.PURPLE_HALF


skin = merge_skins(base_skin, Skin(Colors)*())

# okay decompiling ./MIDIRemoteScripts/Launchkey_MK3/skin.pyc
