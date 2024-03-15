# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\APC64\display.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 4913 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
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
ann_assign ::= expr . LOAD_ANNOTATION LOAD_STR STORE_SUBSCR
ann_assign ::= expr LOAD_ANNOTATION . LOAD_STR STORE_SUBSCR
ann_assign ::= expr LOAD_ANNOTATION LOAD_STR . STORE_SUBSCR
ann_assign ::= expr LOAD_ANNOTATION LOAD_STR STORE_SUBSCR . 
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
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
build_class ::= LOAD_BUILD_CLASS . mkfunc expr CALL_FUNCTION_2
build_class ::= LOAD_BUILD_CLASS . mkfunc expr call CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS . mkfunc expr call expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS . mkfunc expr expr CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc . expr CALL_FUNCTION_2
build_class ::= LOAD_BUILD_CLASS mkfunc . expr call CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc . expr call expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc . expr expr CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc expr . CALL_FUNCTION_2
build_class ::= LOAD_BUILD_CLASS mkfunc expr . call CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc expr . call expr CALL_FUNCTION_4
build_class ::= LOAD_BUILD_CLASS mkfunc expr . expr CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc expr expr . CALL_FUNCTION_3
build_class ::= LOAD_BUILD_CLASS mkfunc expr expr CALL_FUNCTION_3 . 
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= expr . POP_TOP
classdef ::= build_class . store
classdef ::= build_class store . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare ::= compare_single . 
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
compare_single ::= expr expr COMPARE_OP . 
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_right COME_FROM
compared_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compared_chained_middle COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middle_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightc_37 POP_TOP JUMP_FORWARD COME_FROM
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compared_chained_middlea_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 COME_FROM POP_TOP COME_FROM
compared_chained_middleb_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_rightb_false_37 POP_TOP _jump COME_FROM
compared_chained_middlec_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained_righta_37 POP_TOP
dict ::= expr . LOAD_CONST BUILD_CONST_KEY_MAP_1
dict ::= expr LOAD_CONST . BUILD_CONST_KEY_MAP_1
expr ::= LOAD_CODE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_NAME . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr ::= subscript . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jitop ::= expr JUMP_IF_TRUE_OR_POP . 
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
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
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_ret ::= expr . POP_JUMP_IF_FALSE expr RETURN_END_IF COME_FROM return_expr_or_cond
if_exp_ret ::= expr POP_JUMP_IF_FALSE . expr RETURN_END_IF COME_FROM return_expr_or_cond
if_exp_ret ::= expr POP_JUMP_IF_FALSE expr . RETURN_END_IF COME_FROM return_expr_or_cond
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
jmp_false ::= POP_JUMP_IF_FALSE . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
list ::= expr . expr expr BUILD_LIST_3
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr expr . BUILD_LIST_3
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= expr_jitop . expr COME_FROM
or ::= expr_jitop expr . COME_FROM
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP . return_expr_or_cond COME_FROM
ret_or ::= expr JUMP_IF_TRUE_OR_POP return_expr_or_cond . COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_or_cond ::= return_expr . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= SETUP_ANNOTATIONS . 
stmt ::= ann_assign . 
stmt ::= assign . 
stmt ::= classdef . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_NAME . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testtrue ::= expr . jmp_true
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr expr . BUILD_TUPLE_3
tuple ::= expr expr expr BUILD_TUPLE_3 . 
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  53         8  LOAD_FAST                'state'
                  10  LOAD_ATTR                encoder_modes
                  12  LOAD_ATTR                selected_mode
                  14  LOAD_CONST               ('fixed_length', 'quantize')
                  16  COMPARE_OP               in
                  18  POP_JUMP_IF_FALSE    30  'to 30'
                  20  LOAD_FAST                'state'
                  22  LOAD_ATTR                elements
                  24  LOAD_ATTR                encoder
                  26  LOAD_ATTR                mapped_object
->                28  RETURN_VALUE     
                30_0  COME_FROM            18  '18'
from __future__ import absolute_import, print_function, unicode_literals
from dataclasses import dataclass
from math import floor
from typing import Optional, Tuple
from ableton.v3.control_surface.display import DefaultNotifications, DisplaySpecification, Text, view
from ableton.v3.live import display_name, liveobj_name, parameter_owner, song
from .colors import SimpleColor, make_color_for_liveobj
CONTROL_SURFACE_DISPLAY_PAD_MODES = [
 "session", "session_overview", "drum"]

@dataclass
class Content:
    header_color: SimpleColor
    lines: Optional[Tuple[(str, str, str)]]


class Notifications(DefaultNotifications):
    controlled_range = DefaultNotifications.DefaultText()
    generic = DefaultNotifications.DefaultText()

    class Transport(DefaultNotifications.Transport):
        metronome = DefaultNotifications.DefaultText()
        record_quantize = DefaultNotifications.DefaultText()

    class Track(DefaultNotifications.Track):
        select = "default_lines"

    class Device(DefaultNotifications.Device):
        select = "default_lines"
        bank = "default_lines"
        lock = DefaultNotifications.DefaultText()


def get_active_parameterParse error at or near `RETURN_VALUE' instruction at offset 28


def get_default_lines(state):
    return (
     liveobj_name(state.target_track.target_track),
     liveobj_name(state.device.device) or "-",
     state.device.bank_name or "-")


def format_notification(state, notification_text):
    if notification_text == "default_lines":
        lines = get_default_lines(state)
    else:
        if "ERROR" in notification_text or "INFO" in notification_text:
            lines = [Text(t, max_width=(Text.ContentWidth())) for t in notification_text.split("\n")]
        else:
            text = notification_text.split("\n")
            lines = ("", Text((text[0]), max_width=(Text.ContentWidth())), text[1].title())
    return Content(header_color=(make_color_for_liveobj(state.target_track.target_track)),
      lines=(tuple(lines)))


def create_root_view() -> view.View[Optional[Content]]:

    @view.View
    def main_view(state) -> Optional[Content]:
        active_parameter = get_active_parameter(state)
        return Content(header_color=(make_color_for_liveobj(state.target_track.target_track)),
          lines=((getattr(parameter_owner(active_parameter), "name", ""), Text((display_name(active_parameter)), max_width=(Text.ContentWidth() if display_name(active_parameter) in ('Fixed Length',
                                                                                                            'Quantization') else None)), str(active_parameter)) if active_parameter else ("", "Tempo", "{} BPM".format(floor(song().tempo))) if state.encoder_modes.selected_mode == "tempo" else get_default_lines(state) if state.pad_modes.selected_mode in CONTROL_SURFACE_DISPLAY_PAD_MODES else None))

    return view.CompoundView(view.DisconnectedView(render_condition=(lambda state: not state.identification.is_identified or not state.connected or state.encoder_modes.selected_mode == "swing")), view.NotificationView(format_notification,
      suppressing_signals=(
     (lambda state, _: get_active_parameter(state) is not None or state.elements.tempo_button.is_pressed),),
      render_condition=(lambda state, notification: notification != "default_lines" or state.pad_modes.selected_mode not in CONTROL_SURFACE_DISPLAY_PAD_MODES),
      supports_new_line=True), main_view)


def protocol(elements):

    def display(content):
        if content:
            elements.track_color_element.set_light(content.header_color)
        if content and content.lines:
            elements.display_ownership_command.send_value(1)
            elements.display_line_1.display_message(content.lines[0])
            elements.display_line_2.display_message(content.lines[1])
            elements.display_line_3.display_message(content.lines[2])
        else:
            elements.display_ownership_command.send_value(0)

    return display


display_specification = DisplaySpecification(create_root_view=create_root_view,
  protocol=protocol,
  notifications=Notifications)
