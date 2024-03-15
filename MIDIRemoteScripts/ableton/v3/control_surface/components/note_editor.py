# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\components\note_editor.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 22487 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt . COME_FROM
_ifstmts_jump ::= c_stmts_opt . ELSE
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt COME_FROM . 
_ifstmts_jump ::= c_stmts_opt come_froms . 
_ifstmts_jumpl ::= _ifstmts_jump . 
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and ::= expr jmp_false . expr
and ::= expr jmp_false . expr COME_FROM
and ::= expr jmp_false . expr jmp_false
and ::= expr jmp_false expr . 
and ::= expr jmp_false expr . COME_FROM
and ::= expr jmp_false expr . jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_FLOOR_DIVIDE . 
build_map_unpack_with_call ::= expr . expr BUILD_MAP_UNPACK_WITH_CALL_2
build_map_unpack_with_call ::= expr expr . BUILD_MAP_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg CALL_METHOD_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg CALL_METHOD_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_5
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compared_chained_middle ROT_TWO POP_TOP _come_froms
compare_chained37 ::= expr . compared_chained_middlea_37
compare_chained37 ::= expr . compared_chained_middlec_37
compare_chained37_false ::= expr . compare_chained_right_false_37
compare_chained37_false ::= expr . compared_chained_middle_false_37
compare_chained37_false ::= expr . compared_chained_middleb_false_37
compare_chained_right_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_false_37 POP_TOP JUMP_BACK COME_FROM
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_right COME_FROM
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compared_chained_middle COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightc_37 POP_TOP JUMP_FORWARD COME_FROM
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 COME_FROM POP_TOP COME_FROM
compared_chained_middleb_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middlec_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 POP_TOP
continues ::= _stmts . lastl_stmt continue
expr ::= LOAD_CONST . 
expr ::= LOAD_DEREF . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= bin_op . 
expr ::= call . 
expr ::= get_iter . 
expr ::= list_comp . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
generator_exp ::= load_closure . load_genexpr LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp ::= expr jmp_false . expr jf_cf expr COME_FROM
if_exp ::= expr jmp_false . expr jump_absolute_else expr
if_exp ::= expr jmp_false expr . jf_cf expr COME_FROM
if_exp ::= expr jmp_false expr . jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
ifelsestmt ::= testexpr . c_stmts come_froms else_suite come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr . c_stmts_opt jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts . come_froms else_suite come_froms
ifelsestmt ::= testexpr c_stmts come_froms . else_suite come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmtr ::= testexpr . return_if_stmts returns
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
jmp_false ::= POP_JUMP_IF_FALSE . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lambda_body ::= load_closure . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_8
list ::= expr . BUILD_LIST_1
list ::= expr . expr expr expr BUILD_LIST_4
list ::= expr expr . expr expr BUILD_LIST_4
list ::= expr expr expr . expr BUILD_LIST_4
list ::= expr expr expr expr . BUILD_LIST_4
list_comp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
list_comp ::= load_closure . LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
list_comp ::= load_closure LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
list_comp ::= load_closure LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
list_comp ::= load_closure LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
list_comp ::= load_closure LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
list_comp ::= load_closure LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 . expr GET_ITER CALL_FUNCTION_1
list_comp ::= load_closure LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr . GET_ITER CALL_FUNCTION_1
list_comp ::= load_closure LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER . CALL_FUNCTION_1
list_comp ::= load_closure LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1 . 
load_closure ::= LOAD_CLOSURE . 
load_closure ::= LOAD_CLOSURE . BUILD_TUPLE_1
load_closure ::= LOAD_CLOSURE . LOAD_CLOSURE BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE BUILD_TUPLE_1 . 
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE . BUILD_TUPLE_2
load_closure ::= LOAD_CLOSURE LOAD_CLOSURE BUILD_TUPLE_2 . 
load_closure ::= load_closure . LOAD_CLOSURE
load_closure ::= load_closure LOAD_CLOSURE . 
load_genexpr ::= BUILD_TUPLE_1 . LOAD_GENEXPR LOAD_STR
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfunc ::= load_closure . LOAD_CODE LOAD_STR MAKE_FUNCTION_8
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return_closure ::= LOAD_CLOSURE . DUP_TOP STORE_NAME RETURN_VALUE RETURN_LAST
return_closure ::= LOAD_CLOSURE . RETURN_VALUE RETURN_LAST
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_DEREF . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testexpr ::= testfalse . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr . expr expr expr expr expr BUILD_TUPLE_6
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr . expr expr expr expr BUILD_TUPLE_6
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr . expr expr expr BUILD_TUPLE_6
tuple ::= expr expr expr expr . expr expr BUILD_TUPLE_6
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 637        86  LOAD_CLOSURE             'self'
                  88  LOAD_CLOSURE             'step_length'
                  90  BUILD_TUPLE_2         2 
->                92  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                  94  LOAD_STR                 'NoteEditorComponent._visible_steps.<locals>.<dictcomp>'
                  96  MAKE_FUNCTION_8          'closure'
from __future__ import absolute_import, print_function, unicode_literals
from math import inf
from Live.Clip import MidiNoteSpecification
from ...base import EventObject, clamp, depends, in_range, listenable_property, listens
from ...live import liveobj_changed, liveobj_valid
from .. import Component
from ..controls import ButtonControl, control_matrix
from ..skin import LiveObjSkinEntry
PROPERTY_RANGE_KEYS = ('pitch', 'start_time', 'duration', 'velocity')
RELATIVE_OFFSET = 0.24
DEFAULT_HEIGHT = 4
DEFAULT_WIDTH = 4
DEFAULT_VELOCITY = 100
DEFAULT_START_NOTE = 36
DEFAULT_STEP_TRANSLATION_CHANNEL = 1

def get_notes(clip, pitches, time, length, all_pitches=False):
    if len(pitches) > 1 or all_pitches:
        return clip.get_notes_extended(from_time=time,
          from_pitch=0,
          time_span=length,
          pitch_span=128)
    return clip.get_notes_extended(from_time=time,
      from_pitch=(pitches[0]),
      time_span=length,
      pitch_span=1)


def remove_notes(clip, pitches, time, length, all_pitches=False):
    if len(pitches) > 1 or all_pitches:
        clip.remove_notes_extended(from_time=time,
          from_pitch=0,
          time_span=length,
          pitch_span=128)
    else:
        clip.remove_notes_extended(from_time=time,
          from_pitch=(pitches[0]),
          time_span=length,
          pitch_span=1)


def property_ranges_for_notes(notes, start_time, property_ranges):
    for note in notes:
        note_values = [
         note.pitch, note.start_time, note.duration, note.velocity]
        note_values[1] -= start_time
        for key, value in zip(PROPERTY_RANGE_KEYS, note_values):
            if not property_ranges:
                property_ranges = {key: (inf, -inf) for key in PROPERTY_RANGE_KEYS}
            min_value, max_value = property_ranges[key]
            property_ranges[key] = (min(value, min_value), max(value, max_value))

    return property_ranges


class PitchProvider(EventObject):
    pitches = listenable_property.managed([DEFAULT_START_NOTE])
    is_polyphonic = listenable_property.managed(False)


class TimeStep:

    def __init__(self, start, length, *a, **k):
        (super().__init__)(*a, **k)
        self.start = start
        self.length = length

    @property
    def offset(self):
        return self.length * RELATIVE_OFFSET

    def left_boundary(self):
        return max(0, self.start - self.length * 0.2)

    def right_boundary(self):
        return max(0, self.start + self.length * 0.7)

    def filter_notes(self, notes):
        return list(filter(self.includes_note, notes))

    def clamp(self, time):
        return clamp(time, self.left_boundary(), self.right_boundary())

    def includes_note(self, note):
        return self.includes_time(note.start_time)

    def includes_time(self, time):
        return in_range(time - self.start + self.offset, 0, self.length)

    def connected_time_ranges(self):
        return [
         (
          self.start - self.offset, self.length)]


class StepButtonControl(ButtonControl):

    class State(ButtonControl.State):
        x = property((lambda self: self.coordinate[1]))
        y = property((lambda self: self.coordinate[0]))
        is_active = False


class NoteEditorComponent(Component):
    __events__ = ('clip_notes', )
    matrix = control_matrix(StepButtonControl)

    @depends(target_track=None,
      sequencer_clip=None,
      full_velocity=None,
      grid_resolution=None)
    def __init__(self, name="Note_Editor", translation_channel=DEFAULT_STEP_TRANSLATION_CHANNEL, full_velocity=None, target_track=None, sequencer_clip=None, grid_resolution=None, *a, **k):
        (super().__init__)(a, name=name, **k)
        self._full_velocity = full_velocity
        self._translation_channel = translation_channel
        self._page_time = 0.0
        self._pitches = [
         DEFAULT_START_NOTE]
        self._pitch_provider = PitchProvider()
        self._clip_notes = []
        self._clip = None
        self._sequencer_clip = sequencer_clip
        self._active_steps = []
        self._grid_resolution = grid_resolution
        self._NoteEditorComponent__on_resolution_changed.subject = self._grid_resolution
        self._nudge_offset = 0
        self._duration_offset = 0
        self._velocity_offset = 0
        self._pitch_offset = 0
        self._triplet_factor = 1.0
        self._is_triplet = False
        self._update_from_grid()
        self._target_track = target_track
        self._NoteEditorComponent__on_target_track_color_changed.subject = target_track
        self._NoteEditorComponent__on_sequencer_clip_changed.subject = sequencer_clip
        self._NoteEditorComponent__on_sequencer_clip_changed()

    @property
    def width(self):
        if self.matrix.width:
            return self.matrix.width
        return DEFAULT_WIDTH

    @property
    def height(self):
        if self.matrix.height:
            return self.matrix.height
        return DEFAULT_HEIGHT

    @property
    def step_count(self):
        return self.width * self.height

    @property
    def step_length(self):
        return self._grid_resolution.step_length

    @property
    def can_change_page(self):
        return not self._active_steps

    @property
    def page_time(self):
        return self._page_time

    @page_time.setter
    def page_time(self, time):
        if time != self._page_time:
            self._page_time = time
            self.page_time_changed()
            self._NoteEditorComponent__on_clip_notes_changed()

    @listenable_property
    def page_length(self):
        return self.step_count * self.step_length * self._triplet_factor

    @listenable_property
    def active_steps(self):
        return list(map(self._get_step_time_range, self._active_steps))

    @listenable_property
    def pitch_provider(self):
        return self._pitch_provider

    @pitch_provider.setter
    def pitch_provider(self, provider):
        self._pitch_provider = provider
        self._NoteEditorComponent__on_provider_polyphony_changed.subject = provider
        self._NoteEditorComponent__on_provided_pitches_changed.subject = provider
        self._NoteEditorComponent__on_provided_pitches_changed(provider.pitches if provider else [])
        self.notify_pitch_provider()

    def set_clip(self, clip):
        if liveobj_changed(clip, self._clip):
            self._clip = clip
            if self.can_change_page:
                self.page_time = 0.0
            self._NoteEditorComponent__on_clip_notes_changed.subject = clip
            self._NoteEditorComponent__on_clip_notes_changed()

    def set_pitches(self, pitches):
        if pitches != self._pitches:
            self._pitches = pitches
            enabled = self._can_edit()
            for button in self.matrix:
                button.enabled = enabled

            if enabled:
                self._NoteEditorComponent__on_clip_notes_changed()

    def set_pitch_offset(self, value):
        self._modify_note_property("_pitch_offset", value)

    def set_duration_offset(self, value):
        self._modify_note_property("_duration_offset", value)

    def set_velocity_offset(self, value):
        self._modify_note_property("_velocity_offset", value)

    def set_nudge_offset(self, value):
        self._modify_note_property("_nudge_offset", value)

    def set_matrix(self, matrix):
        self.matrix.set_control_element(matrix)
        for button in self.matrix:
            button.channel = self._translation_channel

        self._update_editor_matrix()

    def is_pitch_active(self, pitch):
        if self._has_clip():
            for step in self.active_steps:
                if get_notes(self._clip, (pitch,), step[0], step[1]):
                    return True

        return False

    def toggle_pitch_for_all_active_steps(self, pitch):
        for step in self._active_steps:
            time, _, pitches = self._get_notes_info_from_step(step)
            if pitch not in pitches:
                self._add_new_note_in_step(pitch, time)
            else:
                time_step = self._time_step(self._get_step_start_time(step))
                for time, length in time_step.connected_time_ranges():
                    remove_notes(self._clip, (pitch,), time, length)

    def can_nudge_by_offset(self, offset):
        for step in self.active_steps:
            notes = self._time_step(step[0]).filter_notes(self._clip_notes)
            time_step = self._time_step(step[0])
            for note in notes:
                new_start_time = time_step.clamp(note.start_time + offset)
                if new_start_time != note.start_time and in_range(new_start_time, time_step.left_boundary(), time_step.right_boundary()):
                    return True

        return False

    def get_note_property_ranges(self):
        property_ranges = {}
        if self._active_steps:
            for step in self._active_steps:
                start_time = self._get_step_start_time(step)
                property_ranges = property_ranges_for_notes(self._time_step(start_time).filter_notes(self._clip_notes), start_time, property_ranges)

        return property_ranges

    def page_time_changed(self):
        pass

    def _time_step(self, time):
        return TimeStep(time, self.step_length)

    def _can_edit(self):
        return len(self._pitches) != 0

    def _has_clip(self):
        return liveobj_valid(self._clip)

    def _can_press_or_release_step(self, step):
        width = self.width * self._triplet_factor if self._is_triplet else self.width
        return self._can_edit() and step.x < width and step.y < self.height

    def _get_step_start_time(self, step):
        step_time = step.x + step.y * self.width * self._triplet_factor
        return self._page_time + step_time * self.step_length

    def _get_step_time_range(self, step):
        time = self._get_step_start_time(step)
        return (time, time + self.step_length)

    def _get_notes_info_from_step(self, step):
        time = self._get_step_start_time(step)
        notes = self._time_step(time).filter_notes(self._clip_notes)
        pitches = [note.pitch for note in notes]
        return (time, notes, pitches)

    def _get_clip_notes_time_range(self):
        return (
         self._page_time - self._time_step(0).offset, self.page_length)

    @matrix.pressed
    def matrix(self, pad):
        self._on_pad_pressed(pad)

    def _on_pad_pressed(self, pad):
        if self.is_enabled():
            if not self._has_clip():
                self.set_clip(self._sequencer_clip.create_clip())
                self._update_from_grid()
            if self._can_press_or_release_step(pad):
                pad.is_active = True
                self._refresh_active_steps()

    @matrix.released_immediately
    def matrix(self, pad):
        self._on_pad_released(pad, can_add_or_remove=True)

    @matrix.released_delayed
    def matrix(self, pad):
        self._on_pad_released(pad)

    def _on_pad_released(self, pad, **k):
        if self.is_enabled():
            if self._can_press_or_release_step(pad):
                (self._on_release_step)(pad, **k)

    def _on_release_step(self, step, can_add_or_remove=False):
        if step.is_active:
            if can_add_or_remove:
                self._delete_notes_in_step(step)
                for pitch in self._pitches:
                    self._add_note_in_step(step, pitch)

        step.is_active = False
        self._refresh_active_steps()

    def _refresh_active_steps(self):
        active_steps = [s for s in self.matrix if s.is_active]
        if active_steps != self._active_steps:
            self._active_steps = active_steps
            self.notify_active_steps()

    def _release_active_steps(self):
        for step in self.matrix:
            self._on_release_step(step)

    def _add_note_in_step(self, step, pitch):
        if self._has_clip():
            time, notes, _ = self._get_notes_info_from_step(step)
            if not notes:
                self._add_new_note_in_step(pitch, time)

    def _add_new_note_in_step(self, pitch, time):
        velocity = 127 if self._full_velocity.enabled else DEFAULT_VELOCITY
        note = MidiNoteSpecification(pitch=pitch,
          start_time=time,
          duration=(self.step_length),
          velocity=velocity,
          mute=False)
        self._clip.add_new_notes((note,))
        self._clip.deselect_all_notes()

    def _delete_notes_in_step(self, step):
        if self._has_clip():
            if self._can_edit():
                time_step = self._time_step(self._get_step_start_time(step))
                for time, length in time_step.connected_time_ranges():
                    remove_notes(self._clip, self._pitches, time, length, self._pitch_provider.is_polyphonic)

    def _modify_note_property(self, note_property, value):
        if self.is_enabled():
            setattr(self, note_property, getattr(self, note_property) + value)
            if self._active_steps:
                if self._has_clip():
                    if self._can_edit():
                        self._modify_step_notes(self._active_steps)
                        self._clip.apply_note_modifications(self._clip_notes)
                        self._update_editor_matrix()
                        self.notify_active_steps()
            self._reset_modifications()

    def _reset_modifications(self):
        self._pitch_offset = 0
        self._velocity_offset = 0
        self._duration_offset = 0
        self._nudge_offset = 0

    def _modify_step_notes(self, steps):
        notes = self._clip_notes
        for step in steps:
            time_step = self._time_step(self._get_step_start_time(step))
            for note in notes:
                self._modify_note(time_step, self._duration_offset, self._nudge_offset, note)

    def _modify_note(self, time_step, duration_offset, nudge_offset, note):
        if time_step.includes_time(note.start_time):
            note.start_time = time_step.clamp(note.start_time + nudge_offset)
            note.duration = max(time_step.length * 0.1, note.duration + duration_offset)
            note.velocity = clamp(note.velocity + self._velocity_offset, 1, 127)
            note.pitch = clamp(note.pitch + self._pitch_offset, 0, 127)

    def _update_from_grid(self):
        quantization, self._is_triplet = self._grid_resolution.clip_grid
        self._triplet_factor = 1.0 if not self._is_triplet else 0.75
        if self._has_clip():
            self._clip.view.grid_quantization = quantization
            self._clip.view.grid_is_triplet = self._is_triplet

    def update(self):
        super().update()
        self._update_editor_matrix()

    def _update_editor_matrix(self):
        if self.is_enabled():
            visible_steps = self._visible_steps()
            for index, button in enumerate(self.matrix):
                button.color = LiveObjSkinEntry(self._get_color_for_step(index, visible_steps), self._target_track.target_track)

    def _get_color_for_step(self, index, visible_steps):
        color = "NoteEditor.StepDisabled"
        if self._has_clip():
            if index in visible_steps:
                notes = visible_steps[index].filter_notes(self._clip_notes)
                color = "NoteEditor.StepEmpty"
                if len(notes) > 0:
                    if any((n.mute for n in notes)):
                        color = "NoteEditor.StepMuted"
            else:
                color = "NoteEditor.StepFilled"
        elif index in visible_steps:
            color = "NoteEditor.NoClip"
        return self._get_alternate_color_for_step(index, visible_steps) or color

    def _get_alternate_color_for_step(self, index, visible_steps):
        pass

    def _visible_stepsParse error at or near `LOAD_DICTCOMP' instruction at offset 92

    @listens("notes")
    def __on_clip_notes_changed(self):
        self._clip_notes = []
        if self._has_clip():
            if self._can_edit():
                start, length = self._get_clip_notes_time_range()
                self._clip_notes = get_notes(self._clip, self._pitches, start, length, self._pitch_provider.is_polyphonic)
        self._update_editor_matrix()
        self.notify_clip_notes()

    @listens("clip")
    def __on_sequencer_clip_changed(self):
        self.set_clip(self._sequencer_clip.clip)

    @listens("target_track.color")
    def __on_target_track_color_changed(self):
        self._update_editor_matrix()

    @listens("pitches")
    def __on_provided_pitches_changed(self, pitches):
        self.set_pitches(pitches)

    @listens("is_polyphonic")
    def __on_provider_polyphony_changed(self, _):
        self._NoteEditorComponent__on_clip_notes_changed()

    @listens("index")
    def __on_resolution_changed(self, *_):
        self._release_active_steps()
        self._update_from_grid()
        self.notify_page_length()
        self._NoteEditorComponent__on_clip_notes_changed()
