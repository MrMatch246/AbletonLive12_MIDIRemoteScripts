# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\velocity.py
# Size of source mod 2**32: 611 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name

class VelocityDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(VelocityDeviceDecorator, self).__init__)(*a, **k)
        self._add_switch_option(name="Operation",
          pname="Operation",
          labels=["Vel", "Rel", "Both"])
        self.register_disconnectables(self.options)

# okay decompiling ./MIDIRemoteScripts/Push2/velocity.pyc
