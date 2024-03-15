# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_Mini_MK3\skin.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 872 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import Skin, merge_skins
from novation.colors import Mono, Rgb
from novation.skin import skin as base_skin

class Colors(object):

    class Recording(object):
        On = Mono.ON
        Off = Mono.OFF

    class TrackNavigation(object):
        On = Mono.HALF
        Pressed = Mono.ON

    class SceneNavigation(object):
        On = Mono.HALF
        Pressed = Mono.ON

    class DrumGroup(object):
        PadSelected = Rgb.WHITE
        PadSelectedNotSoloed = Rgb.WHITE
        PadMutedSelected = Rgb.WHITE
        PadSoloedSelected = Rgb.WHITE
        Navigation = Rgb.WHITE_HALF
        NavigationPressed = Rgb.WHITE


skin = merge_skins(base_skin, Skin(Colors)*())

# okay decompiling ./MIDIRemoteScripts/Launchkey_Mini_MK3/skin.pyc
