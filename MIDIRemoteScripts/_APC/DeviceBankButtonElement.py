# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_APC\DeviceBankButtonElement.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 797 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ComboElement import ComboElement as ComboElement

class DeviceBankButtonElement(ComboElement):

    def on_nested_control_element_received(self, control):
        super(DeviceBankButtonElement, self).on_nested_control_element_received(control)
        if control == self.wrapped_control:
            self.wrapped_control.set_channel(1)

    def on_nested_control_element_lost(self, control):
        super(DeviceBankButtonElement, self).on_nested_control_element_lost(control)
        if control == self.wrapped_control:
            self.wrapped_control.set_channel(0)

# okay decompiling ./MIDIRemoteScripts/_APC/DeviceBankButtonElement.pyc
