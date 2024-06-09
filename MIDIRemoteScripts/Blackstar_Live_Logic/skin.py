# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Blackstar_Live_Logic\skin.py
# Size of source mod 2**32: 406 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import Skin
from ableton.v2.control_surface.elements import Color
LED_ON = Color(127)
LED_OFF = Color(0)

class Colors:

    class DefaultButton:
        On = LED_ON
        Off = LED_OFF
        Disabled = LED_OFF


skin = Skin(Colors)

# okay decompiling ./MIDIRemoteScripts/Blackstar_Live_Logic/skin.pyc
