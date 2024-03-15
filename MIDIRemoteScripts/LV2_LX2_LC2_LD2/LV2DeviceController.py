# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\LV2_LX2_LC2_LD2\LV2DeviceController.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 404 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from .FaderfoxDeviceController import FaderfoxDeviceController

class LV2DeviceController(FaderfoxDeviceController):
    __module__ = __name__

    def __init__(self, parent):
        LV2DeviceController.realinit(self, parent)

    def realinit(self, parent):
        FaderfoxDeviceController.realinit(self, parent)

# okay decompiling ./MIDIRemoteScripts/LV2_LX2_LC2_LD2/LV2DeviceController.pyc
