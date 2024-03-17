# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\LV2_LX2_LC2_LD2\LV2_LX2_LC2_LD2.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1149 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from .consts import *
from .FaderfoxDeviceController import FaderfoxDeviceController
from .FaderfoxScript import FaderfoxScript
from .LV2DeviceController import LV2DeviceController
from .LV2MixerController import LV2MixerController
from .LV2TransportController import LV2TransportController

class LV2_LX2_LC2_LD2(FaderfoxScript):
    __module__ = __name__
    __doc__ = "Automap script for LV2 Faderfox controllers"
    __name__ = "LV2_LX2_LC2_LD2 Remote Script"

    def __init__(self, c_instance):
        LV2_LX2_LC2_LD2.realinit(self, c_instance)

    def realinit(self, c_instance):
        self.suffix = "2"
        FaderfoxScript.realinit(self, c_instance)
        self.mixer_controller = LV2MixerController(self)
        self.device_controller = LV2DeviceController(self)
        self.transport_controller = LV2TransportController(self)
        self.components = [
         self.mixer_controller,
         self.device_controller,
         self.transport_controller]

    def suggest_map_mode(self, cc_no, channel):
        return -1

# okay decompiling ./MIDIRemoteScripts/LV2_LX2_LC2_LD2/LV2_LX2_LC2_LD2.pyc
