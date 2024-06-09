# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\elements\proxy_element.py
# Size of source mod 2**32: 418 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import Proxy
from ..control_element import ControlElement

class ProxyElement(Proxy, ControlElement):

    def reset(self):
        try:
            super(ProxyElement, self).__getattr__("reset")()
        except AttributeError:
            pass

# okay decompiling ./MIDIRemoteScripts/ableton/v2/control_surface/elements/proxy_element.pyc
