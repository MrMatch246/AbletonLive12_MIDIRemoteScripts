# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Axiom_AIR_25_49_61\NumericalDisplaySegment.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1504 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.LogicalDisplaySegment as LogicalDisplaySegment

class NumericalDisplaySegment(LogicalDisplaySegment):

    @staticmethod
    def adjust_string(original, length):
        characters_to_retain = {
         '0': 48, 
         '1': 49, 
         '2': 50, 
         '3': 51, 
         '4': 52, 
         '5': 53, 
         '6': 54, 
         '7': 55, 
         '8': 56, 
         '9': 57}
        resulting_string = ""
        for char in original:
            if char in characters_to_retain:
                resulting_string = resulting_string + char

        if len(resulting_string) > length:
            resulting_string = resulting_string[None[:length]]
        if len(resulting_string) < length:
            resulting_string = resulting_string.rjust(length)
        return resulting_string

    def __init__(self, width, update_callback):
        LogicalDisplaySegment.__init__(self, width, update_callback)

    def display_string(self):
        resulting_string = " " * int(self._width)
        if self._data_source != None:
            resulting_string = NumericalDisplaySegment.adjust_string(self._data_source.display_string(), self._width)
        return resulting_string

# okay decompiling ./MIDIRemoteScripts/Axiom_AIR_25_49_61/NumericalDisplaySegment.pyc
