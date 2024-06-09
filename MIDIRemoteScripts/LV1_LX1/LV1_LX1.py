# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\LV1_LX1\LV1_LX1.py
# Size of source mod 2**32: 1184 bytes
from __future__ import absolute_import, print_function, unicode_literals
from LV2_LX2_LC2_LD2.FaderfoxComponent import FaderfoxComponent as FaderfoxComponent
from LV2_LX2_LC2_LD2.FaderfoxDeviceController import FaderfoxDeviceController as FaderfoxDeviceController
from LV2_LX2_LC2_LD2.FaderfoxMixerController import FaderfoxMixerController as FaderfoxMixerController
from LV2_LX2_LC2_LD2.FaderfoxScript import FaderfoxScript as FaderfoxScript
from LV2_LX2_LC2_LD2.FaderfoxTransportController import FaderfoxTransportController as FaderfoxTransportController

class LV1_LX1(FaderfoxScript):
    __module__ = __name__
    __doc__ = "Automap script for LV1 Faderfox controllers"
    __name__ = "LV1_LX1 Remote Script"

    def __init__(self, c_instance):
        LV1_LX1.realinit(self, c_instance)

    def realinit(self, c_instance):
        self.suffix = "1"
        FaderfoxScript.realinit(self, c_instance)
        self.is_lv1 = True
        self.log("lv1 lx1")
        self.mixer_controller = FaderfoxMixerController(self)
        self.device_controller = FaderfoxDeviceController(self)
        self.transport_controller = FaderfoxTransportController(self)
        self.components = [
         self.mixer_controller,
         self.device_controller,
         self.transport_controller]

# okay decompiling ./MIDIRemoteScripts/LV1_LX1/LV1_LX1.pyc
