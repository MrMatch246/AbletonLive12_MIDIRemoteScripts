# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyFadr\KeyFadr.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 424 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from KeyPad import KeyPad

class KeyFadr(KeyPad):
    _encoder_range = list(range(80, 72, -1))
    _product_model_id = 102

    def __init__(self, *a, **k):
        (super(KeyFadr, self).__init__)(*a, **k)

# okay decompiling ./MIDIRemoteScripts/KeyFadr/KeyFadr.pyc
