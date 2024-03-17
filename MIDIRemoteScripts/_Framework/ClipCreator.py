# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\ClipCreator.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 810 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
import Live
_Q = Live.Song.Quantization

class ClipCreator(object):
    grid_quantization = None
    is_grid_triplet = False
    fixed_length = 8

    def create(self, slot, length=None):
        if length is None:
            length = self.fixed_length
        slot.create_clip(length)
        if self.grid_quantization != None:
            slot.clip.view.grid_quantization = self.grid_quantization
            slot.clip.view.grid_is_triplet = self.is_grid_triplet
        slot.fire(force_legato=True, launch_quantization=(_Q.q_no_q))

# okay decompiling ./MIDIRemoteScripts/_Framework/ClipCreator.pyc
