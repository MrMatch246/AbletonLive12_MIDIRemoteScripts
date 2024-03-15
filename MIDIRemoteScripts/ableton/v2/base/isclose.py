# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\base\isclose.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 2204 bytes
from __future__ import absolute_import, print_function, unicode_literals
import math

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    if a == b:
        return True
    if rel_tol < 0.0 or abs_tol < 0.0:
        raise ValueError("error tolerances must be non-negative")
    if math.isinf(abs(a)) or math.isinf(abs(b)):
        return False
    diff = abs(b - a)
    return diff <= abs(rel_tol * b) or diff <= abs(rel_tol * a) or diff <= abs_tol

# okay decompiling ./MIDIRemoteScripts/ableton/v2/base/isclose.pyc
