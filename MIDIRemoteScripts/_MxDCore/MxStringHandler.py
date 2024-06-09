# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_MxDCore\MxStringHandler.py
# Size of source mod 2**32: 4933 bytes
from __future__ import absolute_import, print_function, unicode_literals
import logging
from ableton.v2.base import old_hasattr
logger = logging.getLogger(__name__)
STATE_NEUTRAL = "neutral"
STATE_QUOTED_STR = "quoted"
STATE_UNQUOTED_STR = "unquoted"
STATE_PENDING_NR = "number"
STATE_PENDING_FLOAT = "float"
QUOTE_ENTITY = "&quot;"
QUOTE_SIMPLE = '"'

class MxStringHandler:

    @staticmethod
    def prepare_incoming(string):
        return string.replace(QUOTE_ENTITY, QUOTE_SIMPLE)

    @staticmethod
    def prepare_outgoing(string):
        result = string.replace(QUOTE_SIMPLE, QUOTE_ENTITY)
        if result.find(" ") >= 0:
            result = QUOTE_SIMPLE + result + QUOTE_SIMPLE
        return result

    @staticmethod
    def parse(string, id_callback):
        return MxStringHandler(id_callback).parse_string(string)

    def __init__(self, id_callback):
        self._input_string = ""
        self._current_parse_index = None
        self._state = STATE_NEUTRAL
        self._sub_string = ""
        self._id_callback = id_callback

    def parse_string(self, string):
        self._input_string = string
        self._arguments = []
        self._sub_string = ""
        self._state = STATE_NEUTRAL
        self._current_parse_index = 0
        while self._current_parse_index < len(string):
            char = self._input_string[self._current_parse_index]
            handle_selector = "_" + str(self._state) + "_handle_char"
            if old_hasattr(self, handle_selector):
                getattr(self, handle_selector)(char, self._current_parse_index)
                self._current_parse_index += 1
            else:
                logger.info("Unknown state " + str(self._state))

        finalize_selector = "_finalize_" + str(self._state)
        if len(self._sub_string) > 0:
            if old_hasattr(self, finalize_selector):
                getattr(self, finalize_selector)()
            return self._arguments

    def _neutral_handle_char(self, char, index):
        if char == '"':
            self._state = STATE_QUOTED_STR
        elif char != " ":
            self._sub_string += char
            if str(char).isdigit():
                self._state = STATE_PENDING_NR
            else:
                self._state = STATE_UNQUOTED_STR

    def _number_handle_char(self, char, index):
        if char == " ":
            if len(self._sub_string) > 0:
                self._finalize_number()
            else:
                self._state = STATE_NEUTRAL
        else:
            if char == ".":
                self._state = STATE_PENDING_FLOAT
            elif not str(char).isdigit():
                self._state = STATE_UNQUOTED_STR
            self._sub_string += char

    def _float_handle_char(self, char, index):
        if char == " ":
            self._add_argument(float(self._sub_string))
        else:
            if char in ('.', 'e', 'E'):
                if char in self._sub_string:
                    self._state = STATE_UNQUOTED_STR
            elif not str(char).isdigit():
                self._state = STATE_UNQUOTED_STR
            self._sub_string += char

    def _unquoted_handle_char(self, char, index):
        if char == " ":
            self._add_argument(self._sub_string)
        elif str(char).isdigit():
            if self._sub_string == "-":
                self._state = STATE_PENDING_NR
            elif self._sub_string in ('.', '-.'):
                self._state = STATE_PENDING_FLOAT
            self._sub_string += char

    def _quoted_handle_char(self, char, index):
        close_quote_index = self._input_string.find('"', index + 1)
        if close_quote_index == -1:
            raise RuntimeError("no match for quote at index %d found" % index)
        self._add_argument(self._input_string[index:close_quote_index])
        self._current_parse_index = close_quote_index

    def _finalize_unquoted(self):
        self._add_argument(self._sub_string)

    def _finalize_float(self):
        self._add_argument(float(self._sub_string))

    def _finalize_number(self):
        argument = int(self._sub_string)
        if len(self._arguments) > 0:
            if self._arguments[-1] == "id":
                self._arguments.pop()
                try:
                    argument = self._id_callback(argument)
                except KeyError:
                    raise RuntimeError("Invalid id")

        self._add_argument(argument)

    def _add_argument(self, argument):
        if isinstance(argument, str):
            argument = MxStringHandler.prepare_incoming(argument)
        self._arguments.append(argument)
        self._sub_string = ""
        self._state = STATE_NEUTRAL

# okay decompiling ./MIDIRemoteScripts/_MxDCore/MxStringHandler.pyc
