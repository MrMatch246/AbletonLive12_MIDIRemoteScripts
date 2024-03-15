# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Pro\Launchpad_Pro.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 48219 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_ifstmts_jump ::= COME_FROM . c_stmts come_froms
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
_ifstmts_jump ::= \e_c_stmts_opt COME_FROM . 
_ifstmts_jump ::= \e_c_stmts_opt come_froms . 
_ifstmts_jump ::= c_stmts_opt . COME_FROM
_ifstmts_jump ::= c_stmts_opt . ELSE
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= c_stmts_opt . come_froms
_ifstmts_jump ::= c_stmts_opt COME_FROM . 
_ifstmts_jump ::= c_stmts_opt come_froms . 
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_BACK
_ifstmts_jumpl ::= COME_FROM . c_stmts JUMP_FORWARD
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
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
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
call ::= expr . pos_arg pos_arg pos_arg CALL_METHOD_3
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_METHOD_5
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg CALL_METHOD_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_METHOD_5
call ::= expr pos_arg CALL_METHOD_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg CALL_METHOD_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_METHOD_5
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_METHOD_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_METHOD_5
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_METHOD_5
call ::= expr pos_arg pos_arg pos_arg pos_arg pos_arg . CALL_METHOD_5
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_kw36 ::= expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_4
call_kw36 ::= expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_5
call_kw36 ::= expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_6
call_kw36 ::= expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_7
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_12
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_30
call_kw36 ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_30 . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
come_froms ::= come_froms COME_FROM . 
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
continues ::= _stmts . lastl_stmt continue
continues ::= lastl_stmt . continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= compare . 
expr ::= or . 
expr ::= subscript . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_pjit_come_from ::= expr POP_JUMP_IF_TRUE . COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
get_iter ::= expr . GET_ITER
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
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
ifelsestmt ::= testexpr c_stmts come_froms else_suite . come_froms
ifelsestmt ::= testexpr c_stmts come_froms else_suite come_froms . 
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jf_cfs else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt . jump_forward_else else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite \e_opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs . else_suite opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite . opt_come_from_except
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite \e_opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jf_cfs else_suite opt_come_from_except . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite \e__come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else . else_suite _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite . _come_froms
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite \e__come_froms . 
ifelsestmt ::= testexpr c_stmts_opt jump_forward_else else_suite _come_froms . 
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs . else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs \e_else_suite_opt opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt . opt_come_from_except
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt \e_opt_come_from_except . 
ifelsestmt ::= testexpr stmts jf_cfs else_suite_opt opt_come_from_except . 
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jump_absolute_else else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtl ::= testexpr . c_stmts_opt cf_jf_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt cf_jump_back else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_cfs else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt jump_forward_else else_suitec
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec
ifelsestmtl ::= testexpr c_stmts_opt . cf_jf_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . cf_jump_back else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_cfs else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . jump_forward_else else_suitec
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else . else_suitec
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else else_suitec . 
ifelsestmtl ::= testexpr_cf . c_stmts_opt jb_else else_suitel
ifelsestmtl ::= testexpr_cf \e_c_stmts_opt . jb_else else_suitel
ifelsestmtl ::= testexpr_cf c_stmts_opt . jb_else else_suitel
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK
iflaststmtl ::= testexprl . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl . c_stmts JUMP_BACK POP_BLOCK
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr . expr expr expr BUILD_LIST_4
list ::= expr . expr expr expr expr expr BUILD_LIST_6
list ::= expr . expr expr expr expr expr expr BUILD_LIST_7
list ::= expr . expr expr expr expr expr expr expr expr expr BUILD_LIST_10
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr . expr expr BUILD_LIST_4
list ::= expr expr . expr expr expr expr BUILD_LIST_6
list ::= expr expr . expr expr expr expr expr BUILD_LIST_7
list ::= expr expr . expr expr expr expr expr expr expr expr BUILD_LIST_10
list ::= expr expr expr . BUILD_LIST_3
list ::= expr expr expr . expr BUILD_LIST_4
list ::= expr expr expr . expr expr expr BUILD_LIST_6
list ::= expr expr expr . expr expr expr expr BUILD_LIST_7
list ::= expr expr expr . expr expr expr expr expr expr expr BUILD_LIST_10
list ::= expr expr expr expr . BUILD_LIST_4
list ::= expr expr expr expr . expr expr BUILD_LIST_6
list ::= expr expr expr expr . expr expr expr BUILD_LIST_7
list ::= expr expr expr expr . expr expr expr expr expr expr BUILD_LIST_10
list ::= expr expr expr expr expr . expr BUILD_LIST_6
list ::= expr expr expr expr expr . expr expr BUILD_LIST_7
list ::= expr expr expr expr expr . expr expr expr expr expr BUILD_LIST_10
list ::= expr expr expr expr expr expr . BUILD_LIST_6
list ::= expr expr expr expr expr expr . expr BUILD_LIST_7
list ::= expr expr expr expr expr expr . expr expr expr expr BUILD_LIST_10
list ::= expr expr expr expr expr expr expr . BUILD_LIST_7
list ::= expr expr expr expr expr expr expr . expr expr expr BUILD_LIST_10
list ::= expr expr expr expr expr expr expr expr . expr expr BUILD_LIST_10
list ::= expr expr expr expr expr expr expr expr expr . expr BUILD_LIST_10
list ::= expr expr expr expr expr expr expr expr expr expr . BUILD_LIST_10
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_jt expr COME_FROM . 
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE . COME_FROM
or ::= expr_pjit expr POP_JUMP_IF_FALSE COME_FROM . 
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
slice2 ::= expr . expr BUILD_SLICE_2
slice2 ::= expr expr . BUILD_SLICE_2
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexpr_cf ::= testexpr come_froms . 
testexprl ::= testfalsel . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse ::= or jmp_false . COME_FROM
testfalse ::= or jmp_false COME_FROM . 
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST with_suffix
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH WITH_CLEANUP_START WITH_CLEANUP_FINISH END_FINALLY
with_as ::= expr . SETUP_WITH store suite_stmts_opt COME_FROM_WITH with_suffix
with_as ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH with_suffix
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.1159        70  LOAD_STR                 'audio_mode'
                  72  LOAD_FAST                'self'
                  74  LOAD_ATTR                _note_modes
                  76  STORE_ATTR               selected_mode
->                78  JUMP_FORWARD        102  'to 102'
                80_0  COME_FROM            68  '68'
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range, str
from functools import partial
import Live
import _Framework.ButtonMatrixElement as ButtonMatrixElement
import _Framework.ComboElement as ComboElement
from _Framework.ControlSurface import OptimizedControlSurface
from _Framework.Dependency import inject
import _Framework.IdentifiableControlSurface as IdentifiableControlSurface
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
import _Framework.Layer as Layer
from _Framework.ModesComponent import AddLayerMode, LayerMode, ModesComponent, ReenterBehaviour
from _Framework.SubjectSlot import subject_slot
from _Framework.Util import const
from . import consts
from .ActionsComponent import ActionsComponent
from .BackgroundComponent import BackgroundComponent, ModifierBackgroundComponent
from .ClipActionsComponent import ClipActionsComponent
from .Colors import LIVE_COLORS_TO_MIDI_VALUES, RGB_COLOR_TABLE
from .DeviceNavigationComponent import DeviceNavigationComponent
from .DrumGroupComponent import DrumGroupComponent
from .DrumGroupFinderComponent import DrumGroupFinderComponent
from .LedLightingComponent import LedLightingComponent
from .SkinDefault import make_default_skin
from .SpecialDeviceComponent import SpecialDeviceComponent
from .SpecialMidiMap import SpecialMidiMap, make_button, make_multi_button, make_slider
from .SpecialMixerComponent import SpecialMixerComponent
from .SpecialModesComponent import CancelingReenterBehaviour, SpecialModesComponent, SpecialReenterBehaviour
from .SpecialSessionComponent import SessionZoomingManagerComponent
from .SpecialSessionComponent import SpecialSessionComponent as SessionComponent
from .SpecialSessionComponent import SpecialSessionZoomingComponent as SessionZoomingComponent
from .SpecialSessionRecordingComponent import SpecialSessionRecordingComponent
from .TargetTrackComponent import TargetTrackComponent
from .TranslationComponent import TranslationComponent
from .UserMatrixComponent import UserMatrixComponent
NUM_TRACKS = 8
NUM_SCENES = 8

class MidiMap(SpecialMidiMap):

    def __init__(self, *a, **k):
        (super(MidiMap, self).__init__)(*a, **k)
        left_button_names = ('Session_Record_Button', 'Double_Loop_Button', 'Duplicate_Button',
                             'Quantize_Button', 'Delete_Button', 'Undo_Button', 'Click_Button',
                             'Shift_Button')
        default_states = {True:"DefaultButton.On", 
         False:"DefaultButton.Off"}
        rec_states = {True:"Recording.On", 
         False:"Recording.Off"}
        shift_states = {True:"Misc.ShiftOn", 
         False:"Misc.Shift"}
        for index, val in enumerate(left_button_names):
            if val in ('Session_Record_Button', 'Undo_Button', 'Click_Button'):
                self.add_button(val,
                  0,
                  ((index + 1) * 10),
                  MIDI_CC_TYPE,
                  default_states=(rec_states if val == "Session_Record_Button" else default_states))
            else:
                self.add_modifier_button(val,
                  0,
                  ((index + 1) * 10),
                  MIDI_CC_TYPE,
                  default_states=(shift_states if val == "Shift_Button" else default_states))

        self.add_button("Record_Arm_Mode_Button",
          0,
          1,
          MIDI_CC_TYPE,
          default_states={True:"Mode.RecordArm.On", 
         False:"Mode.RecordArm.Off"})
        self.add_button("Track_Select_Mode_Button",
          0,
          2,
          MIDI_CC_TYPE,
          default_states={True:"Mode.TrackSelect.On", 
         False:"Mode.TrackSelect.Off"})
        self.add_button("Mute_Mode_Button",
          0,
          3,
          MIDI_CC_TYPE,
          default_states={True:"Mode.Mute.On", 
         False:"Mode.Mute.Off"})
        self.add_button("Solo_Mode_Button",
          0,
          4,
          MIDI_CC_TYPE,
          default_states={True:"Mode.Solo.On", 
         False:"Mode.Solo.Off"})
        self.add_button("Volume_Mode_Button",
          0,
          5,
          MIDI_CC_TYPE,
          default_states={True:"Mode.Volume.On", 
         False:"Mode.Volume.Off"})
        self.add_button("Pan_Mode_Button",
          0,
          6,
          MIDI_CC_TYPE,
          default_states={True:"Mode.Pan.On", 
         False:"Mode.Pan.Off"})
        self.add_button("Sends_Mode_Button",
          0,
          7,
          MIDI_CC_TYPE,
          default_states={True:"Mode.Sends.On", 
         False:"Mode.Sends.Off"})
        self.add_button("Stop_Clip_Mode_Button",
          0,
          8,
          MIDI_CC_TYPE,
          default_states={True:"Mode.StopClip.On", 
         False:"Mode.StopClip.Off"})
        self._arrow_button_names = [
         "Arrow_Up_Button",
         "Arrow_Down_Button",
         "Arrow_Left_Button",
         "Arrow_Right_Button"]
        arrow_button_states = {
         'Pressed': '"DefaultButton.On"', 
         'Enabled': '"DefaultButton.Off"', 
         True: '"DefaultButton.On"', 
         False: '"DefaultButton.Disabled"'}
        for index, val in enumerate(self._arrow_button_names):
            self.add_button(val,
              0, (index + 91), MIDI_CC_TYPE, default_states=arrow_button_states)

        self.add_modifier_button("Session_Mode_Button",
          0,
          95,
          MIDI_CC_TYPE,
          default_states={True:"Mode.Session.On", 
         False:"Mode.Session.Off"},
          element_factory=make_multi_button)
        self.add_button("Note_Mode_Button",
          0, 96, MIDI_CC_TYPE, element_factory=make_multi_button)
        self.add_button("Device_Mode_Button",
          0,
          97,
          MIDI_CC_TYPE,
          default_states={True:"Mode.Device.On", 
         False:"Mode.Device.Off"},
          element_factory=make_multi_button)
        self.add_button("User_Mode_Button",
          0,
          98,
          MIDI_CC_TYPE,
          default_states={True:"Mode.User.On", 
         False:"Mode.User.Off"},
          element_factory=make_multi_button,
          color_slaves=True)
        self.add_matrix("Scene_Launch_Button_Matrix", make_button, 0, [
         [identifier for identifier in range(89, 18, -10)]], MIDI_CC_TYPE)
        self["Scene_Stop_Button_Matrix"] = self["Scene_Launch_Button_Matrix"].submatrix[(
         None[:7], None[:None])]
        self["Scene_Stop_Button_Matrix"].name = "Scene_Stop_Button_Matrix"
        self["Stop_All_Clips_Button"] = self["Scene_Launch_Button_Matrix_Raw"][0][7]
        self.add_matrix("Main_Button_Matrix", make_button, 0, [[identifier for identifier in range(start, start + NUM_TRACKS)] for start in range(81, 10, -10)], MIDI_NOTE_TYPE)
        self["Mixer_Button_Matrix"] = self["Main_Button_Matrix"].submatrix[(None[:None], 7[:None])]
        self["Mixer_Button_Matrix"].name = "Mixer_Button_Matrix"
        matrix_rows_with_session_button_raw = [[self.with_session_button(self["Main_Button_Matrix_Raw"][row][column]) for column in range(8)] for row in range(8)]
        self["Main_Button_Matrix_With_Session_Button"] = ButtonMatrixElement(rows=matrix_rows_with_session_button_raw,
          name="Main_Button_Matrix_With_Session_Button")
        note_buttons_raw = []
        for identifier in range(128):
            if identifier not in self["Main_Button_Matrix_Ids"]:
                button = make_button("Note_Button_" + str(identifier), 0, identifier, MIDI_NOTE_TYPE)
                button.set_enabled(False)
                button.set_channel(consts.CHROM_MAP_CHANNEL)
                note_buttons_raw.append(button)

        self["Note_Button_Matrix"] = ButtonMatrixElement(rows=[
         note_buttons_raw],
          name="Note_Button_Matrix")

        def make_raw_drum_matrix():
            result = []
            for row in range(7, -1, -1):
                button_row = []
                row_offset = 8 + (7 - row) * 4
                for column in range(8):
                    column_offset = 28 if column >= 4 else 0
                    identifier = row * 8 + column + row_offset + column_offset
                    matrix_coords = self["Main_Button_Matrix_Ids"].get(identifier)
                    if matrix_coords:
                        button_row.append(self["Main_Button_Matrix_Raw"][matrix_coords[1]][matrix_coords[0]])
                    else:
                        button_row.append(make_button("Drum_Note_Button_" + str(identifier), 0, identifier, MIDI_NOTE_TYPE))

                result.append(button_row)

            return result

        self["Drum_Button_Matrix"] = ButtonMatrixElement(rows=(make_raw_drum_matrix()),
          name="Drum_Button_Matrix")
        self.add_matrix("Slider_Button_Matrix", make_slider, 0, [
         [identifier for identifier in range(21, 29)]], MIDI_CC_TYPE)
        for index, slider in enumerate(self["Slider_Button_Matrix_Raw"][0]):
            slider.set_index(index)

        self.create_user_mode_controls()

    def create_user_mode_controls(self):
        for channel in consts.USER_MODE_CHANNELS:
            channel_name = channel + 1
            self.add_matrix("User_Button_Matrix_Ch_%d" % (channel_name,), make_button, channel, consts.USER_MATRIX_IDENTIFIERS, MIDI_NOTE_TYPE)
            self.add_matrix("User_Left_Side_Button_Matrix_Ch_%d" % (channel_name,), make_button, channel, [[identifier] for identifier in range(108, 116)], MIDI_NOTE_TYPE)
            self.add_matrix("User_Right_Side_Button_Matrix_Ch_%d" % (channel_name,), make_button, channel, [[identifier] for identifier in range(100, 108)], MIDI_NOTE_TYPE)
            self.add_matrix("User_Bottom_Button_Matrix_Ch_%d" % (channel_name,), make_button, channel, [
             [identifier for identifier in range(116, 124)]], MIDI_NOTE_TYPE)
            self.add_matrix("User_Arrow_Button_Matrix_Ch_%d" % (channel_name,), make_button, channel, [
             [identifier for identifier in range(91, 95)]], MIDI_CC_TYPE)

    def with_shift(self, button_name):
        return ComboElement((self[button_name]),
          modifiers=[
         self["Shift_Button"]],
          name=("Shifted_" + button_name))

    def with_session_button(self, button):
        return ComboElement(button,
          modifiers=[
         self["Session_Mode_Button"]],
          name=(button.name + "_With_Session_Button"))


class Launchpad_Pro(IdentifiableControlSurface, OptimizedControlSurface):
    identity_request = consts.SYSEX_IDENTITY_REQUEST

    def __init__(self, c_instance, *a, **k):
        product_id_bytes = consts.MANUFACTURER_ID + consts.DEVICE_CODE
        (super(Launchpad_Pro, self).__init__)(a, c_instance=c_instance, product_id_bytes=product_id_bytes, **k)
        self._challenge = Live.Application.get_random_int(0, 400000000) & 2139062143
        with self.component_guard():
            self._skin = make_default_skin()
            with inject(skin=(const(self._skin))).everywhere():
                self._midimap = MidiMap()
            self._target_track_component = TargetTrackComponent(name="Target_Track")
            self._create_background()
            self._create_global_component()
            self._last_sent_mode_byte = None
            with inject(layout_setup=(const(self._layout_setup)),
              should_arm=(const(self._should_arm_track)),
              quantization_component=(const(self._actions_component))).everywhere():
                self._create_session()
                self._create_recording()
                self._create_actions()
                self._create_drums()
                self._create_mixer()
                self._create_device()
                self._create_modes()
                self._create_user()
            self._on_session_record_changed.subject = self.song()
        self.set_device_component(self._device)
        self._on_session_record_changed()

    def disconnect(self):
        self._send_midi(consts.TURN_OFF_LEDS)
        self._send_midi(consts.QUIT_MESSAGE)
        super(Launchpad_Pro, self).disconnect()

    def _create_background(self):
        self._modifier_background_component = ModifierBackgroundComponent(name="Background_Component",
          is_enabled=False,
          layer=Layer(shift_button=(self._midimap["Shift_Button"])))
        self._shifted_background = BackgroundComponent(name="No_Op_Shifted_Buttons",
          is_enabled=False,
          layer=Layer(click_bitton=(self._midimap.with_shift("Click_Button")),
          delete_button=(self._midimap.with_shift("Delete_Button")),
          duplicate_button=(self._midimap.with_shift("Duplicate_Button")),
          double_button=(self._midimap.with_shift("Double_Loop_Button")),
          session_record_button=(self._midimap.with_shift("Session_Record_Button"))))

    def _create_global_component(self):
        self._actions_component = ActionsComponent(name="Global_Actions",
          is_enabled=False,
          layer=Layer(undo_button=(self._midimap["Undo_Button"]),
          redo_button=(self._midimap.with_shift("Undo_Button")),
          metronome_button=(self._midimap["Click_Button"]),
          quantization_on_button=(self._midimap.with_shift("Quantize_Button"))))

    def _create_session(self):
        self._session = SessionComponent(NUM_TRACKS,
          NUM_SCENES,
          auto_name=True,
          is_enabled=False,
          enable_skinning=True,
          layer=Layer(track_bank_left_button=(self._midimap["Arrow_Left_Button"]),
          track_bank_right_button=(self._midimap["Arrow_Right_Button"]),
          scene_bank_up_button=(self._midimap["Arrow_Up_Button"]),
          scene_bank_down_button=(self._midimap["Arrow_Down_Button"])))
        self._session.set_enabled(True)
        self._session.set_rgb_mode(LIVE_COLORS_TO_MIDI_VALUES, RGB_COLOR_TABLE)
        for scene_index in range(NUM_SCENES):
            scene = self._session.scene(scene_index)
            scene.layer = Layer(select_button=(self._midimap["Shift_Button"]),
              delete_button=(self._midimap["Delete_Button"]),
              duplicate_button=(self._midimap["Duplicate_Button"]))
            for track_index in range(NUM_TRACKS):
                slot = scene.clip_slot(track_index)
                slot.layer = Layer(select_button=(self._midimap["Shift_Button"]),
                  delete_button=(self._midimap["Delete_Button"]),
                  duplicate_button=(self._midimap["Duplicate_Button"]),
                  double_loop_button=(self._midimap["Double_Loop_Button"]),
                  quantize_button=(self._midimap["Quantize_Button"]))

        self._session_zoom = SessionZoomingComponent((self._session),
          name="Session_Overview", is_enabled=True, enable_skinning=True)

    def _create_recording(self):
        self._session_record = SpecialSessionRecordingComponent((self._target_track_component),
          name="Session_Recording",
          is_enabled=False,
          layer=Layer(record_button=(self._midimap["Session_Record_Button"])))

    def _create_actions(self):
        self._clip_actions_component = ClipActionsComponent((self._target_track_component),
          (self._actions_component),
          name="Clip_Actions",
          is_enabled=False,
          layer=Layer(duplicate_button=(self._midimap["Duplicate_Button"]),
          double_button=(self._midimap["Double_Loop_Button"]),
          quantize_button=(self._midimap["Quantize_Button"])))

    def _create_drums(self):
        self._drum_group_finder = DrumGroupFinderComponent((self._target_track_component),
          name="Drum_Group_Finder",
          is_enabled=False,
          layer=None)
        self._on_drum_group_changed.subject = self._drum_group_finder
        self._drum_group_finder.set_enabled(True)
        self._drum_group = DrumGroupComponent((self._clip_actions_component),
          name="Drum_Group_Control",
          translation_channel=(consts.DR_MAP_CHANNEL))
        self._drum_group.set_enabled(True)

    def _create_mixer(self):
        self._mixer = SpecialMixerComponent(NUM_TRACKS,
          auto_name=True, is_enabled=True, invert_mute_feedback=True)
        self._mixer.name = "Mixer_Control"
        self._session.set_mixer(self._mixer)

    def _create_device(self):
        self._device = SpecialDeviceComponent(name="Device_Control",
          is_enabled=False,
          device_selection_follows_track_selection=True)
        self._device_navigation = DeviceNavigationComponent(name="Device_Navigation")
        self._device_background = BackgroundComponent(name="Device_Background_Component")

    def _setup_drum_group(self):
        self._drum_group.set_drum_group_device(self._drum_group_finder.drum_group)

    def _create_translation(self, comp_name, channel, button_layer, should_enable=True, should_reset=True):
        translation_component = TranslationComponent(name=comp_name,
          translated_channel=channel,
          should_enable=should_enable,
          should_reset=should_reset,
          is_enabled=False,
          layer=button_layer)
        setattr(self, "_" + comp_name.lower(), translation_component)
        return translation_component

    def _create_modes(self):
        self._modes = ModesComponent(name="Launchpad_Modes", is_enabled=False)
        self._session_layer_mode = AddLayerMode(self._session, Layer(scene_launch_buttons=(self._midimap["Scene_Launch_Button_Matrix"]),
          clip_launch_buttons=(self._midimap["Main_Button_Matrix"]),
          delete_button=(self._midimap["Delete_Button"]),
          duplicate_button=(self._midimap["Duplicate_Button"]),
          double_button=(self._midimap["Double_Loop_Button"]),
          quantize_button=(self._midimap["Quantize_Button"])))
        action_button_background = BackgroundComponent(name="No_Op_Buttons")
        self._action_button_background_layer_mode = LayerMode(action_button_background, Layer(delete_button=(self._midimap["Delete_Button"]),
          quantize_button=(self._midimap["Quantize_Button"]),
          duplicate_button=(self._midimap["Duplicate_Button"]),
          double_button=(self._midimap["Double_Loop_Button"])))
        self._clip_delete_layer_mode = AddLayerMode((self._clip_actions_component),
          layer=Layer(delete_button=(self._midimap["Delete_Button"])))
        self._create_session_zooming_modes()
        self._create_session_mode()
        self._create_note_modes()
        self._create_device_mode()
        self._create_user_mode()
        self._create_record_arm_mode()
        self._create_track_select_mode()
        self._create_mute_mode()
        self._create_solo_mode()
        self._create_volume_mode()
        self._create_pan_mode()
        self._create_sends_mode()
        self._create_stop_clips_mode()
        self._modes.layer = Layer(session_mode_button=(self._midimap["Session_Mode_Button"]),
          note_mode_button=(self._midimap["Note_Mode_Button"]),
          device_mode_button=(self._midimap["Device_Mode_Button"]),
          user_mode_button=(self._midimap["User_Mode_Button"]),
          record_arm_mode_button=(self._midimap["Record_Arm_Mode_Button"]),
          track_select_mode_button=(self._midimap["Track_Select_Mode_Button"]),
          mute_mode_button=(self._midimap["Mute_Mode_Button"]),
          solo_mode_button=(self._midimap["Solo_Mode_Button"]),
          volume_mode_button=(self._midimap["Volume_Mode_Button"]),
          pan_mode_button=(self._midimap["Pan_Mode_Button"]),
          sends_mode_button=(self._midimap["Sends_Mode_Button"]),
          stop_clip_mode_button=(self._midimap["Stop_Clip_Mode_Button"]))
        self._modes.selected_mode = "session_mode"
        self._on_layout_changed.subject = self._modes

    def _create_session_zooming_modes(self):
        session_zoom_layer = Layer(button_matrix=(self._midimap["Main_Button_Matrix"]),
          nav_left_button=(self._midimap["Arrow_Left_Button"]),
          nav_right_button=(self._midimap["Arrow_Right_Button"]),
          nav_up_button=(self._midimap["Arrow_Up_Button"]),
          nav_down_button=(self._midimap["Arrow_Down_Button"]))
        session_zooming_layer_mode = LayerMode(self._session_zoom, session_zoom_layer)
        self._session_zooming_manager = SessionZoomingManagerComponent((self._modes),
          is_enabled=False)
        session_zooming_button_layer_mode = LayerMode(self._session_zooming_manager, Layer(session_zooming_button=(self._midimap["Session_Mode_Button"])))
        self._prioritized_session_zooming_button_layer_mode = LayerMode(self._session_zooming_manager, Layer(session_zooming_button=(self._midimap["Session_Mode_Button"]),
          priority=1))
        self._session_zooming_background = BackgroundComponent(name="Session_Zooming_Background")
        session_zooming_background_layer_mode = LayerMode(self._session_zooming_background, Layer(scene_launch_buttons=(self._midimap["Scene_Launch_Button_Matrix"]),
          delete_button=(self._midimap["Delete_Button"]),
          quantize_button=(self._midimap["Quantize_Button"]),
          duplicate_button=(self._midimap["Duplicate_Button"]),
          double_loop_button=(self._midimap["Double_Loop_Button"])))
        self._modes.add_mode("session_zooming_mode", [
         self._session_zooming_manager,
         session_zooming_button_layer_mode,
         session_zooming_layer_mode,
         session_zooming_background_layer_mode])
        self._modes.add_mode("prioritized_session_zooming_mode", [
         partial(self._layout_switch, consts.SESSION_LAYOUT_SYSEX_BYTE),
         self._session_zooming_manager,
         self._prioritized_session_zooming_button_layer_mode,
         session_zooming_layer_mode,
         session_zooming_background_layer_mode,
         self.update])

    def _create_session_mode(self):
        self._modes.add_mode("session_mode",
          [
         partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
         self._session_layer_mode,
         self._session.update_navigation_buttons],
          behaviour=(CancelingReenterBehaviour("session_zooming_mode")))

    def _create_note_modes(self):
        note_mode_matrix_translation = self._create_translation("Note_Mode_Matrix_Translation",
          (consts.CHROM_MAP_CHANNEL),
          Layer(button_matrix=(self._midimap["Main_Button_Matrix"]),
          note_button_matrix=(self._midimap["Note_Button_Matrix"]),
          drum_matrix=(self._midimap["Drum_Button_Matrix"]),
          mixer_button_matrix=(self._midimap["Mixer_Button_Matrix"])),
          should_enable=False)
        note_mode_scene_launch_translation = self._create_translation("Note_Mode_Scene_Launch_Translation", consts.CHROM_MAP_CHANNEL, Layer(scene_launch_buttons=(self._midimap["Scene_Launch_Button_Matrix"])))
        scale_setup_mode_button_lighting = LedLightingComponent(name="LED_Lighting_Component",
          is_enabled=False,
          layer=Layer(button=(self._midimap.with_shift("Note_Mode_Button"))))
        drum_mode_note_matrix_translation = self._create_translation("Drum_Mode_Note_Button_Translation",
          0,
          Layer(note_button_matrix=(self._midimap["Note_Button_Matrix"])),
          should_enable=False,
          should_reset=False)
        drum_group_layer_mode = LayerMode((self._drum_group),
          layer=Layer(scroll_up_button=(self._midimap["Arrow_Left_Button"]),
          scroll_down_button=(self._midimap["Arrow_Right_Button"]),
          scroll_page_up_button=(self._midimap["Arrow_Up_Button"]),
          scroll_page_down_button=(self._midimap["Arrow_Down_Button"]),
          drum_matrix=(self._midimap["Drum_Button_Matrix"]),
          select_button=(self._midimap["Shift_Button"]),
          delete_button=(self._midimap["Delete_Button"])))
        self._note_modes = SpecialModesComponent(name="Note_Modes")
        self._note_modes.add_mode("chromatic_mode", [
         partial(self._layout_setup, consts.NOTE_LAYOUT_SYSEX_BYTE),
         self._clip_delete_layer_mode,
         note_mode_matrix_translation,
         scale_setup_mode_button_lighting])
        self._note_modes.add_mode("drum_mode", [
         partial(self._layout_setup, consts.DRUM_LAYOUT_SYSEX_BYTE),
         self._setup_drum_group,
         drum_group_layer_mode,
         drum_mode_note_matrix_translation])
        self._note_modes.add_mode("audio_mode", [
         partial(self._layout_setup, consts.AUDIO_LAYOUT_SYSEX_BYTE),
         self._clip_delete_layer_mode])
        self._note_modes.set_enabled(False)
        self._modes.add_mode("note_mode",
          [
         note_mode_scene_launch_translation,
         self._note_modes,
         self._select_note_mode,
         self._select_target_track,
         self._clip_actions_component,
         self._show_playing_clip,
         self._set_clip_actions_type],
          behaviour=(ReenterBehaviour(self.toggle_detail_view)))
        self._session_record.set_modes_component(self._modes)
        self._session_record.set_note_mode_name("note_mode")

    def _create_device_mode(self):
        device_mode_scene_launch_translation = self._create_translation("Device_Mode_Scene_Launch_Translation", consts.DEVICE_MAP_CHANNEL, Layer(scene_launch_buttons=(self._midimap["Scene_Launch_Button_Matrix"])))
        device_layer_mode = LayerMode((self._device),
          layer=Layer(parameter_controls=(self._midimap["Slider_Button_Matrix"])))
        device_nav_layer_mode = LayerMode((self._device_navigation),
          layer=Layer(device_nav_left_button=(self._midimap["Arrow_Left_Button"]),
          device_nav_right_button=(self._midimap["Arrow_Right_Button"])))
        device_background_layer_mode = LayerMode((self._device_background),
          layer=Layer(arrow_up_button=(self._midimap["Arrow_Up_Button"]),
          arrow_down_button=(self._midimap["Arrow_Down_Button"])))
        self._modes.add_mode("device_mode",
          [
         partial(self._layout_setup, consts.FADER_LAYOUT_SYSEX_BYTE),
         self._device,
         device_layer_mode,
         device_nav_layer_mode,
         device_background_layer_mode,
         self._clip_actions_component,
         self._clip_delete_layer_mode,
         device_mode_scene_launch_translation,
         self._show_playing_clip,
         self._set_clip_actions_type],
          behaviour=(ReenterBehaviour(self.toggle_detail_view)))

    def _create_user_mode(self):
        self._modes.add_mode("user_mode", [partial(self._layout_setup, consts.USER_LAYOUT_SYSEX_BYTE)])

    def _create_record_arm_mode(self):
        arm_layer_mode = LayerMode((self._mixer),
          layer=Layer(arm_buttons=(self._midimap["Mixer_Button_Matrix"])))
        self._modes.add_mode("record_arm_mode",
          [
         partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
         self._session_layer_mode,
         arm_layer_mode,
         self._session_zooming_manager,
         self._prioritized_session_zooming_button_layer_mode,
         self._session.update_navigation_buttons],
          behaviour=(SpecialReenterBehaviour("session_mode")))

    def _create_track_select_mode(self):
        track_select_layer_mode = LayerMode((self._mixer),
          layer=Layer(track_select_buttons=(self._midimap["Mixer_Button_Matrix"])))
        self._modes.add_mode("track_select_mode",
          [
         partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
         self._session_layer_mode,
         track_select_layer_mode,
         self._session_zooming_manager,
         self._prioritized_session_zooming_button_layer_mode,
         self._session.update_navigation_buttons],
          behaviour=(SpecialReenterBehaviour("session_mode")))

    def _create_mute_mode(self):
        mute_layer_mode = LayerMode((self._mixer),
          layer=Layer(mute_buttons=(self._midimap["Mixer_Button_Matrix"])))
        self._modes.add_mode("mute_mode",
          [
         partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
         self._session_layer_mode,
         mute_layer_mode,
         self._session_zooming_manager,
         self._prioritized_session_zooming_button_layer_mode,
         self._session.update_navigation_buttons],
          behaviour=(SpecialReenterBehaviour("session_mode")))

    def _create_solo_mode(self):
        solo_layer_mode = LayerMode((self._mixer),
          layer=Layer(solo_buttons=(self._midimap["Mixer_Button_Matrix"])))
        self._modes.add_mode("solo_mode",
          [
         partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
         self._session_layer_mode,
         solo_layer_mode,
         self._session_zooming_manager,
         self._prioritized_session_zooming_button_layer_mode,
         self._session.update_navigation_buttons],
          behaviour=(SpecialReenterBehaviour("session_mode")))

    def _create_volume_mode(self):
        volume_mode_scene_launch_translation = self._create_translation("Volume_Mode_Scene_Launch_Translation", consts.VOLUME_MAP_CHANNEL, Layer(scene_launch_buttons=(self._midimap["Scene_Launch_Button_Matrix"])))
        volume_layer_mode = LayerMode((self._mixer),
          layer=Layer(volume_controls=(self._midimap["Slider_Button_Matrix"])))
        self._modes.add_mode("volume_mode",
          [
         partial(self._layout_setup, consts.FADER_LAYOUT_SYSEX_BYTE),
         volume_layer_mode,
         self._action_button_background_layer_mode,
         self._session_zooming_manager,
         self._prioritized_session_zooming_button_layer_mode,
         volume_mode_scene_launch_translation,
         self._session.update_navigation_buttons],
          behaviour=(SpecialReenterBehaviour("session_mode")))

    def _create_pan_mode(self):
        pan_mode_scene_launch_translation = self._create_translation("Pan_Mode_Scene_Launch_Translation", consts.PAN_MAP_CHANNEL, Layer(scene_launch_buttons=(self._midimap["Scene_Launch_Button_Matrix"])))
        pan_layer_mode = LayerMode((self._mixer),
          layer=Layer(pan_controls=(self._midimap["Slider_Button_Matrix"])))
        self._modes.add_mode("pan_mode",
          [
         partial(self._layout_setup, consts.FADER_LAYOUT_SYSEX_BYTE),
         pan_layer_mode,
         self._action_button_background_layer_mode,
         self._session_zooming_manager,
         self._prioritized_session_zooming_button_layer_mode,
         pan_mode_scene_launch_translation,
         self._session.update_navigation_buttons],
          behaviour=(SpecialReenterBehaviour("session_mode")))

    def _create_sends_mode(self):
        send_layer_mode = LayerMode((self._mixer),
          layer=Layer(send_controls=(self._midimap["Slider_Button_Matrix"]),
          send_select_buttons=(self._midimap["Scene_Launch_Button_Matrix"])))
        self._modes.add_mode("sends_mode",
          [
         partial(self._layout_setup, consts.FADER_LAYOUT_SYSEX_BYTE),
         send_layer_mode,
         self._action_button_background_layer_mode,
         self._session_zooming_manager,
         self._prioritized_session_zooming_button_layer_mode,
         self._session.update_navigation_buttons],
          behaviour=(SpecialReenterBehaviour("session_mode")))

    def _create_stop_clips_mode(self):
        stop_layer_mode = AddLayerMode(self._session, Layer(stop_track_clip_buttons=(self._midimap["Mixer_Button_Matrix"]),
          stop_scene_clip_buttons=(self._midimap["Scene_Stop_Button_Matrix"]),
          stop_all_clips_button=(self._midimap["Stop_All_Clips_Button"])))
        self._modes.add_mode("stop_clip_mode",
          [
         partial(self._layout_setup, consts.SESSION_LAYOUT_SYSEX_BYTE),
         self._session_layer_mode,
         stop_layer_mode,
         self._session_zooming_manager,
         self._prioritized_session_zooming_button_layer_mode,
         self._session.update_navigation_buttons],
          behaviour=(SpecialReenterBehaviour("session_mode")))

    def toggle_detail_view(self):
        view = self.application().view
        if view.is_view_visible("Detail"):
            if view.is_view_visible("Detail/DeviceChain"):
                view.show_view("Detail/Clip")
            else:
                view.show_view("Detail/DeviceChain")

    def _create_user(self):
        self._user_matrix_component = UserMatrixComponent(name="User_Matrix_Component",
          is_enabled=False,
          layer=Layer(user_button_matrix_ch_6=(self._midimap["User_Button_Matrix_Ch_6"]),
          user_button_matrix_ch_7=(self._midimap["User_Button_Matrix_Ch_7"]),
          user_button_matrix_ch_8=(self._midimap["User_Button_Matrix_Ch_8"]),
          user_button_matrix_ch_14=(self._midimap["User_Button_Matrix_Ch_14"]),
          user_button_matrix_ch_15=(self._midimap["User_Button_Matrix_Ch_15"]),
          user_button_matrix_ch_16=(self._midimap["User_Button_Matrix_Ch_16"]),
          user_left_side_button_matrix_ch_6=(self._midimap["User_Left_Side_Button_Matrix_Ch_6"]),
          user_left_side_button_matrix_ch_7=(self._midimap["User_Left_Side_Button_Matrix_Ch_7"]),
          user_left_side_button_matrix_ch_8=(self._midimap["User_Left_Side_Button_Matrix_Ch_8"]),
          user_left_side_button_matrix_ch_14=(self._midimap["User_Left_Side_Button_Matrix_Ch_14"]),
          user_left_side_button_matrix_ch_15=(self._midimap["User_Left_Side_Button_Matrix_Ch_15"]),
          user_left_side_button_matrix_ch_16=(self._midimap["User_Left_Side_Button_Matrix_Ch_16"]),
          user_right_side_button_matrix_ch_6=(self._midimap["User_Right_Side_Button_Matrix_Ch_6"]),
          user_right_side_button_matrix_ch_7=(self._midimap["User_Right_Side_Button_Matrix_Ch_7"]),
          user_right_side_button_matrix_ch_8=(self._midimap["User_Right_Side_Button_Matrix_Ch_8"]),
          user_right_side_button_matrix_ch_14=(self._midimap["User_Right_Side_Button_Matrix_Ch_14"]),
          user_right_side_button_matrix_ch_15=(self._midimap["User_Right_Side_Button_Matrix_Ch_15"]),
          user_right_side_button_matrix_ch_16=(self._midimap["User_Right_Side_Button_Matrix_Ch_16"]),
          user_bottom_button_matrix_ch_6=(self._midimap["User_Bottom_Button_Matrix_Ch_6"]),
          user_bottom_button_matrix_ch_7=(self._midimap["User_Bottom_Button_Matrix_Ch_7"]),
          user_bottom_button_matrix_ch_8=(self._midimap["User_Bottom_Button_Matrix_Ch_8"]),
          user_bottom_button_matrix_ch_14=(self._midimap["User_Bottom_Button_Matrix_Ch_14"]),
          user_bottom_button_matrix_ch_15=(self._midimap["User_Bottom_Button_Matrix_Ch_15"]),
          user_bottom_button_matrix_ch_16=(self._midimap["User_Bottom_Button_Matrix_Ch_16"]),
          user_arrow_button_matrix_ch_6=(self._midimap["User_Arrow_Button_Matrix_Ch_6"]),
          user_arrow_button_matrix_ch_7=(self._midimap["User_Arrow_Button_Matrix_Ch_7"]),
          user_arrow_button_matrix_ch_8=(self._midimap["User_Arrow_Button_Matrix_Ch_8"]),
          user_arrow_button_matrix_ch_14=(self._midimap["User_Arrow_Button_Matrix_Ch_14"]),
          user_arrow_button_matrix_ch_15=(self._midimap["User_Arrow_Button_Matrix_Ch_15"]),
          user_arrow_button_matrix_ch_16=(self._midimap["User_Arrow_Button_Matrix_Ch_16"])))
        self._user_matrix_component.set_enabled(True)

    @subject_slot("drum_group")
    def _on_drum_group_changed(self):
        if self._note_modes.selected_mode == "drum_mode":
            self._drum_group.set_drum_group_device(self._drum_group_finder.drum_group)
        elif self._modes.selected_mode == "note_mode":
            self._select_note_mode()
        else:
            self.release_controlled_track()
        self._update_note_mode_button(self._drum_group_finder.drum_group is not None)

    def _select_note_modeParse error at or near `JUMP_FORWARD' instruction at offset 78

    def _select_target_track(self):
        track = self._target_track_component.target_track
        if track != self.song().view.selected_track:
            self.song().view.selected_track = track

    def _update_note_mode_button(self, focused_track_is_drum_track):
        button = self._midimap["Note_Mode_Button"]
        if focused_track_is_drum_track:
            button.default_states = {True:"Mode.Drum.On", 
             False:"Mode.Drum.Off"}
        else:
            button.default_states = {True:"Mode.Chromatic.On", 
             False:"Mode.Chromatic.Off"}
        button.reset_state()
        self._modes.update()

    def _show_playing_clip(self):
        track = None
        if self._use_sel_track():
            track = self.song().view.selected_track
        else:
            track = self._target_track_component.target_track
        if track in self.song().tracks:
            slot_index = track.fired_slot_index
            if slot_index < 0:
                slot_index = track.playing_slot_index
            if slot_index >= 0:
                clip_slot = track.clip_slots[slot_index]
                self.song().view.highlighted_clip_slot = clip_slot

    def _set_clip_actions_type(self):
        self._clip_actions_component.use_selected_track(self._use_sel_track())
        self._clip_actions_component.update()

    def _use_sel_track(self):
        return self._modes.selected_mode == "device_mode"

    def _should_arm_track(self):
        return self._modes.selected_mode == "record_arm_mode"

    @subject_slot("selected_mode")
    def _on_layout_changed(self, mode):
        if mode == "note_mode":
            self.set_controlled_track(self._target_track_component.target_track)
        else:
            self.release_controlled_track()
        self._session_record.set_enabled(mode != "user_mode")

    @subject_slot("session_record")
    def _on_session_record_changed(self):
        status = self.song().session_record
        feedback_color = int(self._skin["Instrument.FeedbackRecord"] if status else self._skin["Instrument.Feedback"])
        self._c_instance.set_feedback_velocity(feedback_color)

    def _clear_send_cache(self):
        with self.component_guard():
            for control in self.controls:
                control.clear_send_cache()

    def _update_hardware(self):
        self._clear_send_cache()
        self.update()

    def _update_global_components(self):
        self._actions_component.update()
        self._session_record.update()
        self._modifier_background_component.update()

    def _layout_setup(self, mode):
        self._layout_switch(mode)
        self._clear_send_cache()
        self._update_global_components()

    def _layout_switch(self, mode):
        prefix = consts.SYSEX_STANDARD_PREFIX + consts.SYSEX_PARAM_BYTE_LAYOUT
        suffix = consts.SYSEX_STANDARD_SUFFIX
        self._send_midi(prefix + mode + suffix)
        self._last_sent_mode_byte = mode

    def port_settings_changed(self):
        self.set_highlighting_session_component(None)
        super(Launchpad_Pro, self).port_settings_changed()

    def on_identified(self):
        self._send_challenge()

    def _send_challenge(self):
        challenge_bytes = []
        for index in range(4):
            challenge_bytes.append(self._challenge >> 8 * index & 127)

        challenge = consts.CHALLENGE_PREFIX + tuple(challenge_bytes) + (247, )
        self._send_midi(challenge)

    def _on_handshake_successful(self):
        self._do_send_midi(consts.LIVE_MODE_SWITCH_REQUEST)
        with self.component_guard():
            self._modes.set_enabled(True)
            self._actions_component.set_enabled(True)
            self._session_record.set_enabled(True)
            self._modifier_background_component.set_enabled(True)
            self._shifted_background.set_enabled(True)
            self.release_controlled_track()
            self.set_feedback_channels(consts.FEEDBACK_CHANNELS)
        if self._last_sent_mode_byte is not None:
            self._layout_setup(self._last_sent_mode_byte)
        self.set_highlighting_session_component(self._session)
        self.update()

    def _is_challenge_response(self, midi_bytes):
        return len(midi_bytes) == 10 and midi_bytes[None[:7]] == consts.SYSEX_STANDARD_PREFIX + consts.SYSEX_CHALLENGE_RESPONSE_BYTE

    def _is_response_valid(self, midi_bytes):
        response = int(midi_bytes[7])
        response += int(midi_bytes[8] << 8)
        return response == Live.Application.encrypt_challenge2(self._challenge)

    def handle_sysex(self, midi_bytes):
        if len(midi_bytes) < 7:
            pass
        elif self._is_challenge_response(midi_bytes) and self._is_response_valid(midi_bytes):
            self._on_handshake_successful()
        else:
            if midi_bytes[6] == consts.SYSEX_STATUS_BYTE_LAYOUT and midi_bytes[7] == consts.NOTE_LAYOUT_SYSEX_BYTE[0]:
                self._update_hardware()
            else:
                if midi_bytes[6] in (
                 consts.SYSEX_STATUS_BYTE_MODE,
                 consts.SYSEX_STATUS_BYTE_LAYOUT):
                    pass
                else:
                    super(Launchpad_Pro, self).handle_sysex(midi_bytes)
