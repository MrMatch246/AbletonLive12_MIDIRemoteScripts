# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Komplete_Kontrol\skin.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 711 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import Skin
from ableton.v2.control_surface.elements import Color

class Colors(object):

    class DefaultButton(object):
        On = Color(127)
        Off = Color(0)
        Disabled = Color(0)

    class Transport(object):
        PlayOn = Color(127)
        PlayOff = Color(0)

    class Automation(object):
        On = Color(127)
        Off = Color(0)

    class Mixer(object):
        MuteOn = Color(0)
        MuteOff = Color(1)
        SoloOn = Color(1)
        SoloOff = Color(0)


skin = Skin(Colors)

# okay decompiling ./MIDIRemoteScripts/_Komplete_Kontrol/skin.pyc
