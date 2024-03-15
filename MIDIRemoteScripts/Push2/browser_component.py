# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\browser_component.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 42821 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
_come_froms ::= _come_froms COME_FROM . 
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
and ::= expr JUMP_IF_FALSE_OR_POP . expr \e_come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP . expr come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr . come_from_opt
and ::= expr JUMP_IF_FALSE_OR_POP expr \e_come_from_opt . 
and ::= expr JUMP_IF_FALSE_OR_POP expr come_from_opt . 
and ::= expr jifop_come_from . expr
and ::= expr jifop_come_from expr . 
and ::= expr jmp_false . expr
and ::= expr jmp_false . expr COME_FROM
and ::= expr jmp_false . expr jmp_false
and ::= expr jmp_false expr . 
and ::= expr jmp_false expr . COME_FROM
and ::= expr jmp_false expr . jmp_false
and ::= expr jmp_false expr jmp_false . 
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false . expr POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr . POP_JUMP_IF_TRUE
and_not ::= expr jmp_false expr POP_JUMP_IF_TRUE . 
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr jmp_true . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr DUP_TOP . designList
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt ::= setup_loop . expr GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop . expr GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER LOAD_CONST YIELD_FROM SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_FALSE POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_BLOCK JUMP_ABSOLUTE END_FINALLY COME_FROM for_block POP_BLOCK COME_FROM_LOOP
async_for_stmt ::= setup_loop expr . GET_AITER SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_for_stmt37 ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_BACK COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop . expr GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER \e__come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
async_forelse_stmt ::= setup_loop expr . GET_AITER _come_froms SETUP_EXCEPT GET_ANEXT LOAD_CONST YIELD_FROM store POP_BLOCK JUMP_FORWARD COME_FROM_EXCEPT DUP_TOP LOAD_GLOBAL COMPARE_OP POP_JUMP_IF_TRUE END_FINALLY COME_FROM for_block COME_FROM POP_TOP POP_TOP POP_TOP POP_EXCEPT POP_TOP POP_BLOCK else_suite COME_FROM_LOOP
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP . LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR . expr inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr . inplace_op ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr inplace_op . ROT_TWO STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO . STORE_ATTR
aug_assign2 ::= expr DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR . 
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
binary_operator ::= BINARY_SUBTRACT . 
build_map_unpack_with_call ::= expr . expr BUILD_MAP_UNPACK_WITH_CALL_2
build_map_unpack_with_call ::= expr expr . BUILD_MAP_UNPACK_WITH_CALL_2
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
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
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg CALL_METHOD_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg CALL_METHOD_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg CALL_METHOD_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_METHOD_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_FUNCTION_4
call ::= expr pos_arg pos_arg pos_arg CALL_FUNCTION_3 . 
call_ex_kw ::= expr . expr build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw ::= expr expr . build_map_unpack_with_call CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
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
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= or . 
expr ::= slice2 . 
expr ::= subscript . 
expr ::= unary_not . 
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
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop . expr get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr . get_for_iter store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter . store for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store . for_block POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block . POP_BLOCK NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . 
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK . NOP COME_FROM_LOOP
for ::= setup_loop expr get_for_iter store for_block POP_BLOCK COME_FROM_LOOP . 
for_block ::= \e_l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts JUMP_BACK . 
for_block ::= l_stmts_opt . COME_FROM_LOOP JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitec _come_froms
forelselaststmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitec COME_FROM_LOOP
forelselaststmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitec COME_FROM_LOOP
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suitel _come_froms
forelselaststmtl ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suitel COME_FROM_LOOP
forelselaststmtl ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suitel COME_FROM_LOOP
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . get_for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter . store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store . for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block . POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr get_for_iter store for_block POP_BLOCK . else_suite _come_froms
forelsestmt ::= setup_loop . expr get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr . get_for_iter store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter . store for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store . for_block POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block . POP_BLOCK else_suite COME_FROM_LOOP
forelsestmt ::= setup_loop expr get_for_iter store for_block POP_BLOCK . else_suite COME_FROM_LOOP
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
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
if_exp_37a ::= and_not . expr JUMP_FORWARD come_froms expr COME_FROM
if_exp_37a ::= and_not expr . JUMP_FORWARD come_froms expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false . expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr . POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr jmp_true expr . jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_ret ::= expr . POP_JUMP_IF_FALSE expr RETURN_END_IF COME_FROM return_expr_or_cond
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
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jump_absolute_else else_suitec
ifelsestmtc ::= testexpr c_stmts_opt JUMP_FORWARD . else_suitec
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
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts . 
iflaststmt ::= testexpr c_stmts . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr c_stmts_opt JUMP_FORWARD . 
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
iflaststmtl ::= testexprl c_stmts . JUMP_BACK
iflaststmtl ::= testexprl c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexprl c_stmts . JUMP_BACK POP_BLOCK
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr _ifstmts_jump . 
ifstmtl ::= testexpr . _ifstmts_jumpl
ifstmtl ::= testexpr _ifstmts_jumpl . 
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
inplace_op ::= INPLACE_ADD . 
inplace_op ::= INPLACE_SUBTRACT . 
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jifop_come_from ::= JUMP_IF_FALSE_OR_POP . come_froms
jifop_come_from ::= JUMP_IF_FALSE_OR_POP come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_jt expr COME_FROM . 
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt1 ::= expr RAISE_VARARGS_1 . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP . return_expr_or_cond COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond . COME_FROM
ret_and ::= expr JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM . 
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_expr ::= expr . 
return_expr ::= ret_and . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_expr_or_cond ::= return_expr . 
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= _stmts return . 
returns ::= return . 
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
slice2 ::= expr . expr BUILD_SLICE_2
slice2 ::= expr expr . BUILD_SLICE_2
slice2 ::= expr expr BUILD_SLICE_2 . 
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= aug_assign2 . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= raise_stmt1 . 
stmt ::= return . 
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
suite_stmts ::= returns . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprl ::= testfalsel . 
testfalse ::= and_not . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse ::= or . jmp_false COME_FROM
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr jmp_true . COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testfalsel ::= expr jmp_true . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . expr expr expr BUILD_TUPLE_4
tuple ::= expr expr . expr expr BUILD_TUPLE_4
tuple ::= expr expr expr . expr BUILD_TUPLE_4
tuple ::= expr expr expr expr . BUILD_TUPLE_4
unary_not ::= expr . UNARY_NOT
unary_not ::= expr UNARY_NOT . 
unary_op ::= expr . unary_operator
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK POP_BLOCK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK \e__come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK _come_froms POP_BLOCK else_suitel COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suite COME_FROM_LOOP
while1elsestmt ::= setup_loop . l_stmts JUMP_BACK else_suitel
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts COME_FROM_LOOP JUMP_BACK POP_BLOCK COME_FROM_LOOP
while1stmt ::= setup_loop . l_stmts POP_BLOCK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whileTruestmt ::= setup_loop \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr \e_l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK
whilestmt ::= setup_loop . testexpr l_stmts_opt JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr l_stmts_opt come_froms JUMP_BACK come_froms POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns POP_BLOCK COME_FROM_LOOP
whilestmt ::= setup_loop . testexpr returns come_froms POP_BLOCK COME_FROM_LOOP
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
   
 L. 623        34  LOAD_FAST                'self'
                  36  LOAD_ATTR                focused_list
                  38  LOAD_ATTR                selected_item
                  40  LOAD_ATTR                is_device
                  42  UNARY_NOT        
                44_0  COME_FROM            32  '32'
->              44_1  COME_FROM            16  '16'
                  44  CALL_METHOD_1         1  '1 positional argument'
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from past.utils import old_div
from contextlib import contextmanager
from math import ceil
import Live
from ableton.v2.base import BooleanContext, depends, index_if, lazy_attribute, listenable_property, listens, liveobj_changed, liveobj_valid, nop, task
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ButtonControl, StepEncoderControl, ToggleButtonControl, control_list
from pushbase.browser_util import filter_type_for_hotswap_target, get_selection_for_new_device
from pushbase.consts import MessageBoxText
from pushbase.message_box_component import Messenger
from .browser_item import BrowserItem, ProxyBrowserItem
from .browser_list import BrowserList
from .colors import DISPLAY_BUTTON_SHADE_LEVEL, IndexedColor
NAVIGATION_COLORS = dict(color="Browser.Navigation",
  disabled_color="Browser.NavigationDisabled")

class LoadNeighbourOverlayComponent(Component):
    __events__ = ('load_next', 'load_previous')
    load_next_button = ButtonControl(repeat=False, **NAVIGATION_COLORS)
    load_previous_button = ButtonControl(repeat=False, **NAVIGATION_COLORS)

    @load_next_button.pressed
    def button(self, button):
        self.notify_load_next()

    @load_previous_button.pressed
    def button(self, button):
        self.notify_load_previous()

    @listenable_property
    def can_load_next(self):
        return self.load_next_button.enabled

    @can_load_next.setter
    def can_load_next(self, can_load_next):
        self.load_next_button.enabled = can_load_next
        self.notify_can_load_next()

    @listenable_property
    def can_load_previous(self):
        return self.load_previous_button.enabled

    @can_load_previous.setter
    def can_load_previous(self, can_load_previous):
        self.load_previous_button.enabled = can_load_previous
        self.notify_can_load_previous()


class WrappedLoadableBrowserItem(BrowserItem):

    def __init__(self, *a, **k):
        (super(WrappedLoadableBrowserItem, self).__init__)(*a, **k)
        self._browser = Live.Application.get_application().browser

    @property
    def is_selected(self):
        if self._contained_item is None:
            return self._is_selected
        relation = self._browser.relation_to_hotswap_target(self._contained_item)
        return relation == Live.Browser.Relation.equal


class FolderBrowserItem(BrowserItem):

    def __init__(self, wrapped_loadable=None, *a, **k):
        (super(FolderBrowserItem, self).__init__)(*a, **k)
        self._wrapped_loadable = wrapped_loadable

    @property
    def is_selected(self):
        if self._contained_item is None:
            return self._is_selected
        return self._contained_item.is_selected

    @lazy_attribute
    def children(self):
        return [self._wrapped_loadable] + list(self.contained_item.children)


class PluginPresetBrowserItem(BrowserItem):

    def __init__(self, preset_name=None, preset_index=None, vst_device=None, *a, **k):
        (super(PluginPresetBrowserItem, self).__init__)(a, name=preset_name if preset_name else "<Empty Slot %i>" % (preset_index + 1), is_loadable=True, **k)
        self.preset_index = preset_index
        self._vst_device = vst_device

    @property
    def is_selected(self):
        return self._vst_device.selected_preset_index == self.preset_index

    @property
    def uri(self):
        return "pluginpreset%i" % self.preset_index


class PluginBrowserItem(BrowserItem):

    def __init__(self, vst_device=None, *a, **k):
        (super(PluginBrowserItem, self).__init__)(a, is_loadable=False, is_selected=True, **k)
        self._vst_device = vst_device

    @property
    def children(self):
        return [PluginPresetBrowserItem(preset_name=preset, preset_index=i, vst_device=(self._vst_device)) for i, preset in enumerate(self._vst_device.presets)]


class CannotFocusListError(Exception):
    pass


class BrowserComponent(Component, Messenger):
    __events__ = ('loaded', 'close')
    NUM_ITEMS_PER_COLUMN = 6
    NUM_VISIBLE_BROWSER_LISTS = 7
    NUM_COLUMNS_IN_EXPANDED_LIST = 3
    EXPAND_LIST_TIME = 1.5
    REVEAL_PREVIEW_LIST_TIME = 0.2
    MIN_TIME = 0.6
    MAX_TIME = 1.4
    MIN_TIME_TEXT_LENGTH = 30
    MAX_TIME_TEXT_LENGTH = 70
    up_button = ButtonControl(repeat=True)
    down_button = ButtonControl(repeat=True)
    right_button = ButtonControl(repeat=True, **NAVIGATION_COLORS)
    left_button = ButtonControl(repeat=True, **NAVIGATION_COLORS)
    back_button = ButtonControl(**NAVIGATION_COLORS)
    open_button = ButtonControl(**NAVIGATION_COLORS)
    load_button = ButtonControl(**NAVIGATION_COLORS)
    close_button = ButtonControl()
    prehear_button = ToggleButtonControl(toggled_color="Browser.Option",
      untoggled_color="Browser.OptionDisabled")
    scroll_encoders = control_list(StepEncoderControl,
      num_steps=10, control_count=NUM_VISIBLE_BROWSER_LISTS)
    scroll_focused_encoder = StepEncoderControl(num_steps=10)
    scrolling = listenable_property.managed(False)
    horizontal_navigation = listenable_property.managed(False)
    list_offset = listenable_property.managed(0)
    can_enter = listenable_property.managed(False)
    can_exit = listenable_property.managed(False)
    context_color_index = listenable_property.managed(-1)
    context_text = listenable_property.managed("")

    @depends(commit_model_changes=None, selection=None)
    def __init__(self, preferences=dict(), commit_model_changes=None, selection=None, main_modes_ref=None, *a, **k):
        (super(BrowserComponent, self).__init__)(*a, **k)
        self._lists = []
        self._browser = Live.Application.get_application().browser
        self._current_hotswap_target = self._browser.hotswap_target
        self._updating_root_items = BooleanContext()
        self._focused_list_index = 0
        self._commit_model_changes = commit_model_changes
        self._preferences = preferences
        self._expanded = False
        self._unexpand_with_scroll_encoder = False
        self._delay_preview_list = BooleanContext()
        self._selection = selection
        self._main_modes_ref = main_modes_ref if main_modes_ref is not None else nop
        self._load_neighbour_overlay = LoadNeighbourOverlayComponent(parent=self,
          is_enabled=False)
        self._content_filter_type = None
        self._content_hotswap_target = None
        self._preview_list_task = self._tasks.add(task.sequence(task.wait(self.REVEAL_PREVIEW_LIST_TIME), task.run(self._replace_preview_list_by_task))).kill()
        self._update_root_items()
        self._update_navigation_buttons()
        self._update_context()
        self.prehear_button.is_toggled = preferences.setdefault("browser_prehear", True)
        self._on_selected_track_color_index_changed.subject = self.song.view
        self._on_selected_track_name_changed.subject = self.song.view
        self._on_detail_clip_name_changed.subject = self.song.view
        self._on_hotswap_target_changed.subject = self._browser
        self._on_load_next.subject = self._load_neighbour_overlay
        self._on_load_previous.subject = self._load_neighbour_overlay
        self._on_focused_item_changed.subject = self
        self.register_slot(self, self.notify_focused_item, "focused_list_index")

        def auto_unexpand():
            self.expanded = False
            self._update_list_offset()

        self._unexpand_task = self._tasks.add(task.sequence(task.wait(self.EXPAND_LIST_TIME), task.run(auto_unexpand))).kill()

    @up_button.pressed
    def up_button(self, button):
        with self._delay_preview_list():
            self.focused_list.select_index_with_offset(-1)
        self._update_auto_expand()
        self._update_scrolling()
        self._update_horizontal_navigation()

    @up_button.released
    def up_button(self, button):
        self._finish_preview_list_task()
        self._update_scrolling()

    @down_button.pressed
    def down_button(self, button):
        with self._delay_preview_list():
            self.focused_list.select_index_with_offset(1)
        self._update_auto_expand()
        self._update_scrolling()
        self._update_horizontal_navigation()

    @down_button.released
    def down_button(self, button):
        self._finish_preview_list_task()
        self._update_scrolling()

    @right_button.pressed
    def right_button(self, button):
        if self._expanded and self._can_auto_expand() and self._focused_list_index > 0:
            self.focused_list.select_index_with_offset(self.NUM_ITEMS_PER_COLUMN)
            self._update_scrolling()
            self.horizontal_navigation = True
        else:
            if not self._enter_selected_item():
                self._update_auto_expand()

    @right_button.released
    def right_button(self, button):
        self._update_scrolling()

    @left_button.pressed
    def left_button(self, button):
        if self._expanded and self._focused_list_index > 0 and self.focused_list.selected_index >= self.NUM_ITEMS_PER_COLUMN:
            self.focused_list.select_index_with_offset(-self.NUM_ITEMS_PER_COLUMN)
            self._update_scrolling()
            self.horizontal_navigation = True
        else:
            self._exit_selected_item()

    @left_button.released
    def left_button(self, button):
        self._update_scrolling()

    @open_button.pressed
    def open_button(self, button):
        self._enter_selected_item()

    @back_button.pressed
    def back_button(self, button):
        self._exit_selected_item()

    @scroll_encoders.touched
    def scroll_encoders(self, encoder):
        list_index = self._get_list_index_for_encoder(encoder)
        if list_index is not None:
            try:
                if self._focus_list_with_index(list_index, crop=False):
                    self._unexpand_with_scroll_encoder = True
                    self._prehear_selected_item()
                if self.focused_list.selected_item.is_loadable:
                    if encoder.index == self.scroll_encoders.control_count - 1:
                        self._update_list_offset()
                self._on_encoder_touched()
            except CannotFocusListError:
                pass

    @scroll_encoders.released
    def scroll_encoders(self, encoders):
        self._on_encoder_released()

    @scroll_encoders.value
    def scroll_encoders(self, value, encoder):
        list_index = self._get_list_index_for_encoder(encoder)
        if list_index is not None:
            try:
                if self._focus_list_with_index(list_index):
                    self._unexpand_with_scroll_encoder = True
                self._on_encoder_value(value)
            except CannotFocusListError:
                pass

    @scroll_focused_encoder.value
    def scroll_focused_encoder(self, value, encoder):
        self._on_encoder_value(value)

    @scroll_focused_encoder.touched
    def scroll_focused_encoder(self, encoder):
        self._on_encoder_touched()

    @scroll_focused_encoder.released
    def scroll_focused_encoder(self, encoder):
        self._on_encoder_released()

    def _on_encoder_value(self, value):
        with self._delay_preview_list():
            self.focused_list.select_index_with_offset(value)
        first_visible_list_focused = self.focused_list_index == self.list_offset
        if self.expanded and first_visible_list_focused:
            self.expanded = False
            self._unexpand_with_scroll_encoder = True
        else:
            if not first_visible_list_focused:
                if not self.expanded:
                    if self._can_auto_expand():
                        self._update_auto_expand()
                        self._unexpand_with_scroll_encoder = True
        self._update_scrolling()
        self._update_horizontal_navigation()

    def _on_encoder_touched(self):
        self._unexpand_task.kill()
        self._update_scrolling()
        self._update_horizontal_navigation()

    def _on_encoder_released(self):
        any_encoder_touched = any(map((lambda e: e.is_touched), self.scroll_encoders)) or self.scroll_focused_encoder.is_touched
        if not any_encoder_touched:
            if self._unexpand_with_scroll_encoder:
                self._unexpand_task.restart()
        self._update_scrolling()

    def _get_list_index_for_encoder(self, encoder):
        if self.expanded:
            if encoder.index == 0:
                return self.list_offset
        else:
            return self.list_offset + 1
            index = self.list_offset + encoder.index
            if self.focused_list_index + 1 == index:
                if self.should_widen_focused_item:
                    index = self.focused_list_index
            if 0 <= index < len(self._lists):
                return index
        return

    @load_button.pressed
    def load_button(self, button):
        self._load_selected_item()

    @prehear_button.toggled
    def prehear_button(self, toggled, button):
        if toggled:
            self._prehear_selected_item()
        else:
            self._browser.stop_preview()
        self._preferences["browser_prehear"] = toggled
        self.notify_prehear_enabled()

    @close_button.pressed
    def close_button(self, button):
        self.notify_close()

    @listenable_property
    def lists(self):
        return self._lists

    @listenable_property
    def focused_list_index(self):
        return self._focused_list_index

    @listenable_property
    def prehear_enabled(self):
        return self.prehear_button.is_toggled

    @property
    def focused_list(self):
        return self._lists[self._focused_list_index]

    @listenable_property
    def focused_item(self):
        return self.focused_list.selected_item

    @listenable_property
    def expanded(self):
        return self._expanded

    @property
    def load_neighbour_overlay(self):
        return self._load_neighbour_overlay

    @listenable_property
    def should_widen_focused_item(self):
        return self.focused_item.is_loadable and not self.focused_item.is_device

    @property
    def context_display_type(self):
        return "custom_button"

    def disconnect(self):
        super(BrowserComponent, self).disconnect()
        self._lists = []
        self._commit_model_changes = None

    @expanded.setter
    def expanded(self, expanded):
        if self._expanded != expanded:
            self._expanded = expanded
            self._unexpand_with_scroll_encoder = False
            self._update_navigation_buttons()
            if len(self._lists) > self._focused_list_index + 1:
                self._lists[self._focused_list_index + 1].limit = self.num_preview_items
            self.notify_expanded()

    @listens("selected_track.color_index")
    def _on_selected_track_color_index_changed(self):
        if self.is_enabled():
            self._update_context()
            self._update_navigation_buttons()

    @listens("selected_track.name")
    def _on_selected_track_name_changed(self):
        if self.is_enabled():
            self._update_context()

    @listens("detail_clip.name")
    def _on_detail_clip_name_changed(self):
        if self.is_enabled():
            self._update_context()

    @listens("hotswap_target")
    def _on_hotswap_target_changed(self):
        if self.is_enabled():
            if not self._switched_to_empty_pad():
                self._update_root_items()
                self._update_context()
                self._update_list_offset()
                self._update_load_neighbour_overlay_visibility()
            else:
                self._load_neighbour_overlay.set_enabled(False)
        self._current_hotswap_target = self._browser.hotswap_target

    @listens("focused_item")
    def _on_focused_item_changed(self):
        self.notify_should_widen_focused_item()

    @property
    def browse_for_audio_clip(self):
        main_modes = self._main_modes_ref()
        if main_modes is None:
            return False
        has_midi_support = self.song.view.selected_track.has_midi_input
        return not has_midi_support and "clip" in main_modes.active_modes

    def _switched_to_empty_pad(self):
        hotswap_target = self._browser.hotswap_target
        is_browsing_drumpad = isinstance(hotswap_target, Live.DrumPad.DrumPad)
        was_browsing_pad = isinstance(self._current_hotswap_target, Live.DrumPad.DrumPad)
        return is_browsing_drumpad and was_browsing_pad and len(hotswap_target.chains) == 0

    def _focus_list_with_index(self, index, crop=True):
        if self._focused_list_index != index:
            if self._finish_preview_list_task():
                if index >= len(self._lists):
                    raise CannotFocusListError()
            self._on_focused_selection_changed.subject = None
            if self._focused_list_index > index:
                if crop:
                    for l in self._lists[self._focused_list_index[:None]]:
                        l.selected_index = -1

            self._focused_list_index = index
            self.focused_list.limit = -1
            if self.focused_list.selected_index == -1:
                self.focused_list.selected_index = 0
            self.notify_focused_list_index()
            self._on_focused_selection_changed.subject = self.focused_list
            if crop:
                self._crop_browser_lists(self._focused_list_index + 2)
            if self._focused_list_index == len(self._lists) - 1:
                self._replace_preview_list()
            self._load_neighbour_overlay.set_enabled(False)
            self._update_navigation_buttons()
            return True
        return False

    @listens("selected_index")
    def _on_focused_selection_changed(self):
        if self._delay_preview_list:
            self.focused_item.is_loadable or self._preview_list_task.restart()
        else:
            self._replace_preview_list()
        self._update_navigation_buttons()
        self._prehear_selected_item()
        self._load_neighbour_overlay.set_enabled(False)
        self.notify_focused_item()

    def _get_actual_item(self, item):
        contained_item = getattr(item, "contained_item", None)
        if contained_item is not None:
            return contained_item
        return item

    def _previous_can_be_loaded(self):
        return self.focused_list.selected_index > 0 and self.focused_list.items[self.focused_list.selected_index - 1].is_loadable

    def _next_can_be_loaded(self):
        items = self.focused_list.items
        return self.focused_list.selected_index < len(items) - 1 and items[self.focused_list.selected_index + 1].is_loadable

    @listens("load_next")
    def _on_load_next(self):
        self.focused_list.selected_index += 1
        self._load_selected_item()

    @listens("load_previous")
    def _on_load_previous(self):
        self.focused_list.selected_index -= 1
        self._load_selected_item()

    def _update_load_neighbour_overlay_visibilityParse error at or near `COME_FROM' instruction at offset 44_1

    def _load_selected_item(self):
        focused_list = self.focused_list
        self._update_load_neighbour_overlay_visibility()
        self._update_navigation_buttons()
        item = self._get_actual_item(focused_list.selected_item)
        self._load_item(item)
        self.notify_loaded()

    def _show_load_notification(self, item):
        notification_text = self._make_notification_text(item)
        text_length = len(notification_text)
        notification_time = self.MIN_TIME
        if text_length > self.MIN_TIME_TEXT_LENGTH:
            if text_length > self.MAX_TIME_TEXT_LENGTH:
                notification_time = self.MAX_TIME
            else:
                notification_time = self.MIN_TIME + (self.MAX_TIME - self.MIN_TIME) * old_div(float(text_length - self.MIN_TIME_TEXT_LENGTH), self.MAX_TIME_TEXT_LENGTH - self.MIN_TIME_TEXT_LENGTH)
        self.show_notification(notification_text, notification_time=notification_time)
        self._commit_model_changes()

    def _make_notification_text(self, browser_item):
        return "Loading %s" % browser_item.name

    def _load_item(self, item):
        self._show_load_notification(item)
        if liveobj_valid(self._browser.hotswap_target):
            if isinstance(item, PluginPresetBrowserItem):
                self._browser.hotswap_target.selected_preset_index = item.preset_index
            else:
                self._browser.load_item(item)
                self._content_hotswap_target = self._browser.hotswap_target
        else:
            with self._insert_right_of_selected():
                self._browser.load_item(item)

    @contextmanager
    def _insert_right_of_selected(self):
        DeviceInsertMode = Live.Track.DeviceInsertMode
        device_to_select = get_selection_for_new_device(self._selection)
        if device_to_select:
            self._selection.selected_object = device_to_select
        selected_track_view = self.song.view.selected_track.view
        selected_track_view.device_insert_mode = DeviceInsertMode.selected_right
        yield
        selected_track_view.device_insert_mode = DeviceInsertMode.default

    def _prehear_selected_item(self):
        if self.prehear_button.is_toggled:
            if not self._updating_root_items:
                self._browser.stop_preview()
                item = self._get_actual_item(self.focused_list.selected_item)
                if item:
                    if item.is_loadable:
                        if isinstance(item, Live.Browser.BrowserItem):
                            self._browser.preview_item(item)

    def _stop_prehear(self):
        if self.prehear_button.is_toggled:
            if not self._updating_root_items:
                self._browser.stop_preview()

    def _update_navigation_buttons(self):
        focused_list = self.focused_list
        self.up_button.enabled = focused_list.selected_index > 0
        self.down_button.enabled = focused_list.selected_index < len(focused_list.items) - 1
        selected_item_loadable = self.focused_list.selected_item.is_loadable
        can_exit = self._focused_list_index > 0
        assume_can_enter = self._preview_list_task.is_running and not selected_item_loadable
        can_enter = self._focused_list_index < len(self._lists) - 1 or assume_can_enter
        self.back_button.enabled = can_exit
        self.open_button.enabled = can_enter
        self.load_button.enabled = selected_item_loadable
        self._load_neighbour_overlay.can_load_previous = self._previous_can_be_loaded()
        self._load_neighbour_overlay.can_load_next = self._next_can_be_loaded()
        context_button_color = IndexedColor.from_live_index(self.context_color_index, DISPLAY_BUTTON_SHADE_LEVEL) if self.context_color_index > -1 else "Browser.Navigation"
        self.load_button.color = context_button_color
        self.close_button.color = context_button_color
        self._load_neighbour_overlay.load_next_button.color = context_button_color
        self._load_neighbour_overlay.load_previous_button.color = context_button_color
        if not self._expanded:
            self.left_button.enabled = self.back_button.enabled
            self.right_button.enabled = can_enter or self._can_auto_expand()
        else:
            num_columns = int(ceil(old_div(float(len(self.focused_list.items)), self.NUM_ITEMS_PER_COLUMN)))
            last_column_start_index = (num_columns - 1) * self.NUM_ITEMS_PER_COLUMN
            self.left_button.enabled = self._focused_list_index > 0
            self.right_button.enabled = can_enter or self.focused_list.selected_index < last_column_start_index
        self.can_enter = can_enter
        self.can_exit = can_exit

    def _update_scrolling(self):
        self.scrolling = self.up_button.is_pressed or self.down_button.is_pressed or self.scroll_focused_encoder.is_touched or any(map((lambda e: e.is_touched), self.scroll_encoders)) or self.right_button.is_pressed and self._expanded or self.left_button.is_pressed and self._expanded

    def _update_horizontal_navigation(self):
        self.horizontal_navigation = self.right_button.is_pressed or self.left_button.is_pressed

    def _update_context(self):
        selected_track = self.song.view.selected_track
        clip = self.song.view.detail_clip
        if self.browse_for_audio_clip and clip:
            self.context_text = clip.name
        else:
            if liveobj_valid(self._browser.hotswap_target):
                self.context_text = self._browser.hotswap_target.name
            else:
                self.context_text = selected_track.name
        selected_track_color_index = selected_track.color_index
        self.context_color_index = selected_track_color_index if selected_track_color_index is not None else -1

    def _enter_selected_item(self):
        item_entered = False
        self._finish_preview_list_task()
        new_index = self._focused_list_index + 1
        if 0 <= new_index < len(self._lists):
            self._focus_list_with_index(new_index)
            self._unexpand_task.kill()
            self._update_list_offset()
            self._update_auto_expand()
            self._prehear_selected_item()
            item_entered = True
        return item_entered

    def _exit_selected_item(self):
        item_exited = False
        try:
            self._focus_list_with_index(self._focused_list_index - 1)
            self._update_list_offset()
            self._update_auto_expand()
            self._stop_prehear()
            item_exited = True
        except CannotFocusListError:
            pass

        return item_exited

    def _can_auto_expand(self):
        return len(self.focused_list.items) > self.NUM_ITEMS_PER_COLUMN * 2 and self.focused_list.selected_item.is_loadable and getattr(self.focused_list.selected_item, "contained_item", None) == None

    def _update_auto_expand(self):
        self.expanded = self._can_auto_expand()
        self._update_list_offset()

    def _update_list_offset(self):
        if self.expanded:
            self.list_offset = max(0, self.focused_list_index - 1)
        else:
            offset = len(self._lists)
            if self.focused_list.selected_item.is_loadable:
                offset += 1
            self.list_offset = max(0, offset - self.NUM_VISIBLE_BROWSER_LISTS)

    def _replace_preview_list_by_task(self):
        self._replace_preview_list()
        self._update_navigation_buttons()

    def _finish_preview_list_task(self):
        if self._preview_list_task.is_running:
            self._replace_preview_list_by_task()
            return True
        return False

    def _replace_preview_list(self):
        self._preview_list_task.kill()
        self._crop_browser_lists(self._focused_list_index + 1)
        selected_item = self.focused_list.selected_item
        children_iterator = selected_item.iter_children
        if len(children_iterator) > 0:
            enable_wrapping = getattr(selected_item, "enable_wrapping", True) and self.focused_list.items_wrapped
            self._append_browser_list(children_iterator=children_iterator,
              limit=(self.num_preview_items),
              enable_wrapping=enable_wrapping)

    def _append_browser_list(self, children_iterator, limit=-1, enable_wrapping=True):
        l = BrowserList(item_iterator=children_iterator,
          item_wrapper=(self._wrap_item if enable_wrapping else nop),
          limit=limit)
        l.items_wrapped = enable_wrapping
        self._lists.append(l)
        self.register_disconnectable(l)
        self.notify_lists()

    def _crop_browser_lists(self, length):
        num_items_to_crop = len(self._lists) - length
        for _ in range(num_items_to_crop):
            l = self._lists.pop()
            self.unregister_disconnectable(l)

        if num_items_to_crop > 0:
            self.notify_lists()

    def _make_root_browser_items(self):
        filter_type = self._browser.filter_type
        hotswap_target = self._browser.hotswap_target
        if liveobj_valid(hotswap_target):
            filter_type = filter_type_for_hotswap_target(hotswap_target,
              default=filter_type)
        return make_root_browser_items(self._browser, filter_type)

    def _content_cache_is_valid(self):
        return self._content_filter_type == self._browser.filter_type and not liveobj_changed(self._content_hotswap_target, self._browser.hotswap_target)

    def _invalidate_content_cache(self):
        self._content_hotswap_target = None
        self._content_filter_type = None

    def _update_content_cache(self):
        self._content_filter_type = self._browser.filter_type
        self._content_hotswap_target = self._browser.hotswap_target

    def _update_root_items(self):
        if not self._content_cache_is_valid():
            self._update_content_cache()
            with self._updating_root_items():
                self._on_focused_selection_changed.subject = None
                self._crop_browser_lists(0)
                self._append_browser_list(children_iterator=(self._make_root_browser_items()))
                self._focused_list_index = 0
                self.focused_list.selected_index = 0
                self._select_hotswap_target()
                self._on_focused_selection_changed.subject = self.focused_list
                self._on_focused_selection_changed()

    def _select_hotswap_target(self, list_index=0):
        if list_index < len(self._lists):
            l = self._lists[list_index]
            l.access_all = True
            children = l.items
            i = index_if((lambda i: i.is_selected), children)
            if i < len(children):
                self._focused_list_index = list_index
                l.selected_index = i
                self._replace_preview_list()
                self._select_hotswap_target(list_index + 1)

    @property
    def num_preview_items(self):
        if self._expanded:
            return self.NUM_ITEMS_PER_COLUMN * self.NUM_COLUMNS_IN_EXPANDED_LIST
        return 6

    def update(self):
        super(BrowserComponent, self).update()
        self._invalidate_content_cache()
        if self.is_enabled():
            self._update_root_items()
            self._update_context()
            self._update_list_offset()
            self._update_load_neighbour_overlay_visibility()
            self._update_navigation_buttons()
            self.expanded = False
            self._update_list_offset()
        else:
            self._stop_prehear()
            self.list_offset = 0

    def _wrap_item(self, item):
        if item.is_device:
            return self._wrap_device_item(item)
        if self._is_hotswap_target_plugin(item):
            return self._wrap_hotswapped_plugin_item(item)
        return item

    def _wrap_device_item(self, item):
        wrapped_loadable = WrappedLoadableBrowserItem(name=(item.name),
          is_loadable=True,
          contained_item=item)
        return FolderBrowserItem(name=(item.name),
          is_loadable=True,
          is_device=True,
          contained_item=item,
          wrapped_loadable=wrapped_loadable,
          icon="browser_arrowcontent.svg")

    def _is_hotswap_target_plugin(self, item):
        return isinstance(self._browser.hotswap_target, Live.PluginDevice.PluginDevice) and isinstance(item, Live.Browser.BrowserItem) and self._browser.relation_to_hotswap_target(item) == Live.Browser.Relation.equal

    def _wrap_hotswapped_plugin_item(self, item):
        return PluginBrowserItem(name=(item.name), vst_device=(self._browser.hotswap_target))


class TrackBrowserItem(BrowserItem):
    filter_type = Live.Browser.FilterType.hotswap_off

    def create_track(self, song):
        raise NotImplementedError


class MidiTrackBrowserItem(TrackBrowserItem):
    filter_type = Live.Browser.FilterType.midi_track_devices

    def __init__(self, *a, **k):
        (super(MidiTrackBrowserItem, self).__init__)(a, name="MIDI track", **k)

    def create_track(self, song):
        song.create_midi_track()


class AudioTrackBrowserItem(TrackBrowserItem):
    filter_type = Live.Browser.FilterType.audio_effect_hotswap

    def __init__(self, *a, **k):
        (super(AudioTrackBrowserItem, self).__init__)(a, name="Audio track", **k)

    def create_track(self, song):
        song.create_audio_track()


class ReturnTrackBrowserItem(TrackBrowserItem):
    filter_type = Live.Browser.FilterType.audio_effect_hotswap

    def __init__(self, *a, **k):
        (super(ReturnTrackBrowserItem, self).__init__)(a, name="Return track", **k)

    def create_track(self, song):
        song.create_return_track()


class DefaultTrackBrowserItem(BrowserItem):

    def __init__(self, *a, **k):
        (super(DefaultTrackBrowserItem, self).__init__)(a, name="Default track", is_loadable=True, **k)


class NewTrackBrowserComponent(BrowserComponent):

    def __init__(self, *a, **k):
        self._content = []
        self._track_type_items = [
         MidiTrackBrowserItem(children=(self._content)),
         AudioTrackBrowserItem(children=(self._content)),
         ReturnTrackBrowserItem(children=(self._content))]
        (super(NewTrackBrowserComponent, self).__init__)(*a, **k)
        if self.is_enabled():
            self._update_filter_type()

    def _make_root_browser_items(self):
        self._update_root_content()
        return self._track_type_items

    def disconnect(self):
        super(NewTrackBrowserComponent, self).disconnect()
        self._content = []

    @property
    def browse_for_audio_clip(self):
        return False

    @property
    def context_display_type(self):
        return "cancel_button"

    def _update_root_content(self):
        real_root_items = super(NewTrackBrowserComponent, self)._make_root_browser_items()
        self._content[None[:None]] = [DefaultTrackBrowserItem()] + real_root_items

    def _update_root_items(self):
        self._set_filter_type(self._track_type_items[0].filter_type)
        super(NewTrackBrowserComponent, self)._update_root_items()
        self._on_root_list_selection_changed.subject = self._lists[0]

    def _update_filter_type(self):
        self._set_filter_type(self._selected_track_item().filter_type)

    def _set_filter_type(self, filter_type):
        if self._browser.filter_type != filter_type:
            self._browser.filter_type = filter_type
            self._update_root_content()

    def _update_context(self):
        pass

    def _load_item(self, item):
        try:
            self._selected_track_item().create_track(self.song)
            if isinstance(item, DefaultTrackBrowserItem):
                self._show_load_notification(item)
            else:
                super(NewTrackBrowserComponent, self)._load_item(item)
        except Live.Base.LimitationError:
            self.show_notification(MessageBoxText.TRACK_LIMIT_REACHED)
        except RuntimeError:
            self.show_notification(MessageBoxText.MAX_RETURN_TRACKS_REACHED)

    def _make_notification_text(self, browser_item):
        if isinstance(browser_item, DefaultTrackBrowserItem):
            return "Default track created"
        new_track_position = self._selected_track_index() + 1
        return "%s loaded in track %i" % (browser_item.name, new_track_position)

    def _selected_track_index(self):
        song = self.song
        selected_track = self._selection.selected_track
        if selected_track in song.tracks:
            return list(song.tracks).index(selected_track)
        return -1

    def _selected_track_item(self):
        return self._lists[0].selected_item

    @listens("selected_index")
    def _on_root_list_selection_changed(self):
        self._update_filter_type()
        self._replace_preview_list()


def wrap_item(item, icon, **k):
    return ProxyBrowserItem(proxied_object=item, icon=icon, **k)


def wrap_items(items, icon, enable_wrapping=True):
    for i, place in enumerate(items):
        items[i] = wrap_item(place, icon, enable_wrapping=enable_wrapping)

    return items


class UserFilesBrowserItem(BrowserItem):

    def __init__(self, browser, *a, **k):
        (super(UserFilesBrowserItem, self).__init__)(*a, **k)
        self._browser = browser

    @property
    def is_selected(self):
        return any(map((lambda c: c.is_selected), self.children))

    @lazy_attribute
    def children(self):
        res = [
         wrap_item(self._browser.user_library, "browser_userlibrary.svg")] + wrap_items(list(self._browser.user_folders), "browser_folder.svg")
        self._browser = None
        return res


class CollectionsBrowserItem(BrowserItem):

    def __init__(self, browser, *a, **k):
        (super(CollectionsBrowserItem, self).__init__)(*a, **k)
        self._browser = browser

    @property
    def is_selected(self):
        return any(map((lambda c: c.is_selected), self.children))

    @lazy_attribute
    def children(self):
        color_labels = wrap_items((list(self._browser.colors)),
          "browser_collection_icon.svg",
          enable_wrapping=False)
        self._browser = None
        return color_labels


def make_root_browser_items(browser, filter_type):
    collections = CollectionsBrowserItem(browser,
      name="Collections", icon="browser_collections.svg")
    sounds = wrap_item(browser.sounds, "browser_sounds.svg")
    drums = wrap_item((browser.drums), "browser_drums.svg", enable_wrapping=False)
    instruments = wrap_item(browser.instruments, "browser_instruments.svg")
    audio_effects = wrap_item(browser.audio_effects, "browser_audioeffect.svg")
    midi_effects = wrap_item(browser.midi_effects, "browser_midieffect.svg")
    packs = wrap_item(browser.packs, "browser_packs.svg")
    current_project = wrap_item(browser.current_project, "browser_currentproject.svg")
    if filter_type == Live.Browser.FilterType.samples:
        categories = [
         packs, current_project]
    else:
        common_items = [
         wrap_item(browser.max_for_live, "browser_max.svg"),
         wrap_item(browser.plugins, "browser_plugins.svg"),
         packs,
         current_project]
        if filter_type == Live.Browser.FilterType.audio_effect_hotswap:
            categories = [
             audio_effects] + common_items
        else:
            if filter_type == Live.Browser.FilterType.midi_effect_hotswap:
                categories = [
                 midi_effects] + common_items
            else:
                if filter_type == Live.Browser.FilterType.instrument_hotswap:
                    categories = [
                     sounds, drums, instruments] + common_items
                else:
                    categories = [
                     sounds, 
                     drums, 
                     instruments, 
                     audio_effects, 
                     midi_effects] + common_items
    user_files = UserFilesBrowserItem(browser,
      name="User Files", icon="browser_userfiles.svg")
    return [
     collections, user_files] + categories
