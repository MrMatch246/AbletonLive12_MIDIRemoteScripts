# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\note_settings_component.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 24089 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM_LOOP . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms . COME_FROM_LOOP
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
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_lambda_body ::= lambda_body . 
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
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_MULTIPLY . 
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
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg CALL_METHOD_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg CALL_METHOD_3
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call ::= expr pos_arg pos_arg CALL_METHOD_2 . 
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_METHOD_3
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
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_loops ::= \e_come_from_loops COME_FROM_LOOP . 
come_from_loops ::= come_from_loops . COME_FROM_LOOP
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
expr ::= LOAD_CODE . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= _lambda_body . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= if_exp . 
expr ::= list . 
expr ::= list_comp . 
expr ::= or . 
expr ::= slice2 . 
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
for_block ::= l_stmts_opt COME_FROM_LOOP . JUMP_BACK
for_block ::= l_stmts_opt COME_FROM_LOOP JUMP_BACK . 
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
for_block ::= l_stmts_opt _come_froms JUMP_BACK . 
for_block ::= l_stmts_opt come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt come_from_loops JUMP_BACK . 
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
function_def ::= mkfunc . store
function_def ::= mkfunc store . 
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
if_exp ::= expr jmp_false expr jf_cf . expr COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr . COME_FROM
if_exp ::= expr jmp_false expr jf_cf expr COME_FROM . 
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
if_exp_not ::= expr jmp_true expr jump_forward_else . expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
if_exp_true ::= expr JUMP_FORWARD . expr COME_FROM
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
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . c_stmts
iflaststmt ::= testexpr . c_stmts JUMP_ABSOLUTE
iflaststmt ::= testexpr . c_stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_0
lambda_body ::= LOAD_LAMBDA . LOAD_STR MAKE_FUNCTION_8
lambda_body ::= LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_0
lambda_body ::= LOAD_LAMBDA LOAD_STR . MAKE_FUNCTION_8
lambda_body ::= LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_0 . 
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr . expr expr BUILD_LIST_3
list ::= expr . expr expr expr BUILD_LIST_4
list ::= expr . expr expr expr expr BUILD_LIST_5
list ::= expr BUILD_LIST_1 . 
list ::= expr expr . BUILD_LIST_2
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr . expr expr BUILD_LIST_4
list ::= expr expr . expr expr expr BUILD_LIST_5
list ::= expr expr expr . BUILD_LIST_3
list ::= expr expr expr . expr BUILD_LIST_4
list ::= expr expr expr . expr expr BUILD_LIST_5
list ::= expr expr expr expr . BUILD_LIST_4
list ::= expr expr expr expr . expr BUILD_LIST_5
list_comp ::= LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
list_comp ::= LOAD_LISTCOMP . LOAD_STR MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
list_comp ::= LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1
list_comp ::= LOAD_LISTCOMP LOAD_STR . MAKE_FUNCTION_8 expr GET_ITER CALL_FUNCTION_1
list_comp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 . expr GET_ITER CALL_FUNCTION_1
list_comp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr . GET_ITER CALL_FUNCTION_1
list_comp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER . CALL_FUNCTION_1
list_comp ::= LOAD_LISTCOMP LOAD_STR MAKE_FUNCTION_0 expr GET_ITER CALL_FUNCTION_1 . 
lstmt ::= stmt . 
mkfunc ::= LOAD_CODE . LOAD_STR MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR . MAKE_FUNCTION_0
mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 . 
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= expr_jt . expr
or ::= expr_jt . expr COME_FROM
or ::= expr_jt expr . 
or ::= expr_jt expr . COME_FROM
or ::= expr_pjit . expr POP_JUMP_IF_FALSE COME_FROM
or ::= expr_pjit expr . POP_JUMP_IF_FALSE COME_FROM
pos_arg ::= expr . 
raise_stmt1 ::= expr . RAISE_VARARGS_1
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
setup_loop ::= SETUP_LOOP . _come_froms
setup_loop ::= SETUP_LOOP \e__come_froms . 
slice2 ::= expr . expr BUILD_SLICE_2
slice2 ::= expr expr . BUILD_SLICE_2
slice2 ::= expr expr BUILD_SLICE_2 . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for . 
stmt ::= function_def . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= store_subscript . 
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
store_subscript ::= expr expr STORE_SUBSCR . 
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testexpr ::= testfalse . 
testexpr_cf ::= testexpr . come_froms
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
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
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
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 731       194  LOAD_FAST                'self'
                 196  LOAD_METHOD              _is_edit_all_notes_active
                 198  CALL_METHOD_0         0  '0 positional arguments'
                 200  POP_JUMP_IF_TRUE    210  'to 210'
                 202  LOAD_FAST                'min_max_values'
                 204  POP_JUMP_IF_TRUE    210  'to 210'
                 206  LOAD_STR                 'Tweak to add note'
                 208  JUMP_FORWARD        212  'to 212'
               210_0  COME_FROM           204  '204'
->             210_1  COME_FROM           200  '200'
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import filter, map, range, round, str
from past.utils import old_div
import math
from functools import partial
from itertools import chain
import Live
from ableton.v2.base import clamp, find_if, forward_property, listenable_property, listens, listens_group, liveobj_valid, task
from ableton.v2.control_surface import Component, defaults
from ableton.v2.control_surface.control import ButtonControl, ControlManager, EncoderControl, StepEncoderControl, control_list
from ableton.v2.control_surface.elements import DisplayDataSource
from ableton.v2.control_surface.mode import AddLayerMode, Mode, ModesComponent
from .consts import CHAR_ELLIPSIS, GRAPH_VOL

class NoteSettingBase(ControlManager):
    __events__ = ('setting_changed', )
    attribute_index = -1
    encoder = EncoderControl()

    def __init__(self, grid_resolution=None, *a, **k):
        (super(NoteSettingBase, self).__init__)(*a, **k)
        self._min_max_value = None
        self._grid_resolution = grid_resolution

    def encoder_value_to_attribute(self, value):
        raise NotImplementedError

    @property
    def step_length(self):
        if self._grid_resolution:
            return self._grid_resolution.step_length
        return 1.0

    def set_min_max(self, min_max_value):
        self._min_max_value = min_max_value

    @encoder.value
    def encoder(self, value, _):
        self._on_encoder_value_changed(value)

    def _on_encoder_value_changed(self, value):
        self.notify_setting_changed(self.attribute_index, self.encoder_value_to_attribute(value))


class NoteSetting(NoteSettingBase):

    def __init__(self, *a, **k):
        (super(NoteSetting, self).__init__)(*a, **k)
        self.value_source = DisplayDataSource()
        self.label_source = DisplayDataSource()
        self.label_source.set_display_string(self.get_label())

    def get_label(self):
        raise NotImplementedError

    def attribute_min_max_to_string(self, min_value, max_value):
        raise NotImplementedError

    def set_min_max(self, min_max_value):
        self.value_source.set_display_string(self.attribute_min_max_to_string(min_max_value[0], min_max_value[1]) if min_max_value else "-")


RANGE_STRING_FLOAT = "%.1f" + CHAR_ELLIPSIS + "%.1f"
RANGE_STRING_INT = "%d" + CHAR_ELLIPSIS + "%d"
RANGE_STRING_PERCENT = "%d %%" + CHAR_ELLIPSIS + "%d %%"

def step_offset_percentage(step_length, value):
    return int(round(old_div(value - int(old_div(value, step_length)) * step_length, step_length) * 100))


def step_offset_min_max_to_string(step_length, min_value, max_value):
    min_value = step_offset_percentage(step_length, min_value)
    max_value = step_offset_percentage(step_length, max_value)
    if min_value == max_value:
        return "%d%%" % min_value
    return (RANGE_STRING_INT + "%%") % (min_value, max_value)


def convert_value_to_graphic(value, value_range):
    value_bar = GRAPH_VOL
    graph_range = float(len(value_bar))
    value = clamp(int(old_div(value, value_range) * graph_range), 0, len(value_bar) - 1)
    display_string = value_bar[value]
    return display_string


class NoteNudgeSetting(NoteSetting):
    attribute_index = 1

    def get_label(self):
        return "Nudge"

    def encoder_value_to_attribute(self, value):
        return self.step_length * value

    def attribute_min_max_to_string(self, min_value, max_value):
        return step_offset_min_max_to_string(self.step_length, min_value, max_value)


class NoteLengthCoarseSetting(NoteSetting):
    attribute_index = 2
    encoder = StepEncoderControl()

    def get_label(self):
        return "Length -"

    def attribute_min_max_to_string(self, min_value, max_value):
        min_value = old_div(min_value, self.step_length)
        max_value = old_div(max_value, self.step_length)

        def format_string(value):
            num_non_decimal_figures = int(math.log10(value)) if value > 0 else 0
            return "%%.%dg" % (num_non_decimal_figures + 2,)

        if min_value == max_value:
            return (format_string(min_value) + " stp") % min_value
        return (format_string(min_value) + CHAR_ELLIPSIS + format_string(max_value)) % (
         min_value, max_value)

    def encoder_value_to_attribute(self, value):
        return self.step_length * value

    @encoder.value
    def encoder(self, value, _):
        self._on_encoder_value_changed(value)


class NoteLengthFineSetting(NoteSetting):
    attribute_index = 2

    def get_label(self):
        return "Fine"

    def encoder_value_to_attribute(self, value):
        return self.step_length * value

    def attribute_min_max_to_string(self, min_value, max_value):
        value = step_offset_percentage(self.step_length, min_value)
        return convert_value_to_graphic(value, 100.0)


class NoteVelocitySetting(NoteSetting):
    attribute_index = 3

    def get_label(self):
        return "Velocity"

    def encoder_value_to_attribute(self, value):
        return value * 128

    def attribute_min_max_to_string(self, min_value, max_value):
        if int(min_value) == int(max_value):
            return str(int(min_value))
        return RANGE_STRING_INT % (min_value, max_value)


class NoteVelocityDeviationSetting(NoteSetting):
    attribute_index = 4

    def get_label(self):
        return "VelRange"

    def encoder_value_to_attribute(self, value):
        return value * 128

    def attribute_min_max_to_string(self, min_value, max_value):

        def sign_of(x):
            if x > 0:
                return "+"
            return ""

        if int(min_value) == int(max_value):
            return sign_of(min_value) + str(int(min_value))
        return RANGE_STRING_INT % (min_value, max_value)


class NoteProbabilitySetting(NoteSetting):
    attribute_index = 5

    def get_label(self):
        return "Problty"

    def encoder_value_to_attribute(self, value):
        return value * 128

    def attribute_min_max_to_string(self, min_value, max_value):
        min_value_percent = round(min_value * 100)
        max_value_percent = round(max_value * 100)
        if min_value_percent == max_value_percent:
            return "%d %%" % min_value_percent
        return RANGE_STRING_PERCENT % (min_value_percent, max_value_percent)


class NoteSettingsComponentBase(Component):
    __events__ = ('setting_changed', 'full_velocity')
    full_velocity_button = ButtonControl()

    def __init__(self, grid_resolution=None, *a, **k):
        (super(NoteSettingsComponentBase, self).__init__)(*a, **k)
        self._settings = []
        self._encoders = []
        self._create_settings(grid_resolution)

    def _create_settings(self, grid_resolution):
        self._add_setting(NoteNudgeSetting(grid_resolution=grid_resolution))
        self._add_setting(NoteLengthCoarseSetting(grid_resolution=grid_resolution))
        self._add_setting(NoteLengthFineSetting(grid_resolution=grid_resolution))
        self._add_setting(NoteVelocitySetting(grid_resolution=grid_resolution))
        if self.show_velocity_ranges_and_probabilities:
            self._add_setting(NoteVelocityDeviationSetting(grid_resolution=grid_resolution))
            self._add_setting(NoteProbabilitySetting(grid_resolution=grid_resolution))

    def _add_setting(self, setting):
        self._settings.append(setting)
        self._update_encoders()
        self.register_disconnectable(setting)
        self.register_slot(setting, self.notify_setting_changed, "setting_changed")

    @property
    def number_of_settings(self):
        return len(self._settings)

    @property
    def settings(self):
        return self._settings

    @property
    def show_velocity_ranges_and_probabilities(self):
        return Live.Application.UnavailableFeature.note_velocity_ranges_and_probabilities not in Live.Application.get_application().unavailable_features

    def set_info_message(self, message):
        pass

    def set_encoder_controls(self, encoders):
        self._encoders = encoders or []
        self._update_encoders()

    def set_min_max(self, index, min_max_value):
        setting_for_index = [i for i in self._settings if i.attribute_index == index]
        for setting in setting_for_index:
            setting.set_min_max(min_max_value)

    @full_velocity_button.pressed
    def full_velocity_button(self, button):
        if self.is_enabled():
            self.notify_full_velocity()

    def _update_encoders(self):
        if self.is_enabled() and self._encoders:
            for index, setting in enumerate(self._settings):
                setting.encoder.set_control_element(self._encoders[index])

        else:
            list(map((lambda setting: setting.encoder.set_control_element(None)), self._settings))

    def update(self):
        super(NoteSettingsComponentBase, self).update()
        self._update_encoders()


class NoteSettingsComponent(NoteSettingsComponentBase):

    def __init__(self, *a, **k):
        (super(NoteSettingsComponent, self).__init__)(*a, **k)
        self._top_data_sources = [DisplayDataSource() for _ in range(8)]
        self._bottom_data_sources = [DisplayDataSource() for _ in range(8)]
        self._info_data_source = DisplayDataSource()
        self._create_display_sources()

    def _create_display_sources(self):
        self._top_data_sources = [s.label_source for s in self._settings] + [DisplayDataSource() for _ in range(8 - len(self._settings))]
        self._bottom_data_sources = [s.value_source for s in self._settings] + [DisplayDataSource() for _ in range(8 - len(self._settings))]

    def set_top_display_line(self, display):
        if self.is_enabled():
            if display:
                display.set_data_sources(self._top_data_sources)

    def set_bottom_display_line(self, display):
        if self.is_enabled():
            if display:
                display.set_data_sources(self._bottom_data_sources)

    def set_info_display_line(self, display):
        if self.is_enabled():
            if display:
                display.set_data_sources([self._info_data_source])

    def set_clear_display_line(self, display):
        if self.is_enabled():
            if display:
                display.reset()

    def set_info_message(self, message):
        self._info_data_source.set_display_string(message.rjust(62))


class DetailViewRestorerMode(Mode):

    def __init__(self, application=None, *a, **k):
        (super(DetailViewRestorerMode, self).__init__)(*a, **k)
        self._app = application
        self._view_to_restore = None

    def enter_mode(self):
        clip_view_visible = self._app.view.is_view_visible("Detail/Clip", False)
        device_chain_visible = self._app.view.is_view_visible("Detail/DeviceChain", False)
        if clip_view_visible != device_chain_visible:
            self._view_to_restore = "Detail/Clip" if clip_view_visible else "Detail/DeviceChain"

    def leave_mode(self):
        try:
            if self._view_to_restore:
                self._app.view.show_view(self._view_to_restore)
                self._view_to_restore = None
        except RuntimeError:
            pass


def show_clip_view(application):
    try:
        view = application.view
        if view.is_view_visible("Detail/DeviceChain", False):
            if not view.is_view_visible("Detail/Clip", False):
                application.view.show_view("Detail/Clip")
    except RuntimeError:
        pass


class ModeSelector(Component):
    select_buttons = control_list(ButtonControl, color="DefaultButton.Disabled")
    state_buttons = control_list(ButtonControl, color="DefaultButton.Disabled")


class NoteEditorSettingsComponent(ModesComponent):
    initial_encoders = control_list(EncoderControl)
    encoders = control_list(EncoderControl)

    def __init__(self, note_settings_component_class=None, automation_component_class=None, grid_resolution=None, initial_encoder_layer=None, encoder_layer=None, *a, **k):
        (super(NoteEditorSettingsComponent, self).__init__)(*a, **k)
        self.settings = note_settings_component_class(grid_resolution=grid_resolution,
          parent=self,
          is_enabled=False)
        self.automation = automation_component_class(parent=self, is_enabled=False)
        self._mode_selector = ModeSelector(parent=self, is_enabled=False)
        self._visible_detail_view = "Detail/DeviceChain"
        self._show_settings_task = self._tasks.add(task.sequence(task.wait(defaults.MOMENTARY_DELAY), task.run(self._show_settings))).kill()
        self._update_infos_task = self._tasks.add(task.run(self._update_note_infos)).kill()
        self._settings_modes = ModesComponent(parent=self)
        self._settings_modes.set_enabled(False)
        self._settings_modes.add_mode("automation", [
         self.automation,
         self._mode_selector,
         partial(self._set_envelope_view_visible, True),
         partial(show_clip_view, self.application)])
        self._settings_modes.add_mode("note_settings", [
         self.settings,
         self._update_note_infos,
         self._mode_selector,
         partial(self._set_envelope_view_visible, False),
         partial(show_clip_view, self.application)])
        self._settings_modes.selected_mode = "note_settings"
        self._NoteEditorSettingsComponent__on_selected_setting_mode_changed.subject = self._settings_modes
        self.add_mode("disabled", [])
        self.add_mode("about_to_show", [
         AddLayerMode(self, initial_encoder_layer),
         (
          self._show_settings_task.restart, self._show_settings_task.kill)])
        self.add_mode("enabled", [
         DetailViewRestorerMode(self.application),
         AddLayerMode(self, encoder_layer),
         self._settings_modes])
        self.selected_mode = "disabled"
        self._editors = []
        self._on_detail_clip_changed.subject = self.song.view
        self._on_selected_track_changed.subject = self.song.view
        self._NoteEditorSettingsComponent__on_full_velocity_changed.subject = self.settings
        self._NoteEditorSettingsComponent__on_setting_changed.subject = self.settings

    automation_layer = forward_property("automation")("layer")
    mode_selector_layer = forward_property("_mode_selector")("layer")
    selected_setting = forward_property("_settings_modes")("selected_mode")

    @property
    def step_settings(self):
        return self._settings_modes

    @property
    def editors(self):
        return self._editors

    @listenable_property
    def is_touched(self):
        return any(map((lambda e: e and e.is_touched), filter((lambda e: self._can_notify_is_touched(e)), self.encoders)))

    def _is_step_held(self):
        return len(self._active_note_regions()) > 0

    def add_editor(self, editor):
        self._editors.append(editor)
        self._on_active_note_regions_changed.add_subject(editor)
        self._on_notes_changed.replace_subjects(self._editors)
        self._NoteEditorSettingsComponent__on_modify_all_notes_changed.add_subject(editor)

    def set_encoders(self, encoders):
        self.encoders.set_control_element(encoders)
        self.settings.set_encoder_controls(encoders)
        self.automation.set_parameter_controls(encoders)

    @property
    def parameter_provider(self):
        self.automation.parameter_provider

    @parameter_provider.setter
    def parameter_provider(self, value):
        self.automation.parameter_provider = value

    @listens("selected_mode")
    def __on_selected_setting_mode_changed(self, mode):
        if mode == "automation":
            self.automation.selected_time = self._active_note_regions()

    def update_view_state_based_on_selected_setting(self, setting):
        if not self.selected_mode == "enabled" or self.is_touched or setting is None:
            self._set_settings_view_enabled(False)
        else:
            if self._is_step_held():
                if not (self.selected_setting == "automation" and self.automation.can_automate_parameters):
                    if self.selected_setting == "note_settings":
                        self._show_settings()

    @listens("full_velocity")
    def __on_full_velocity_changed(self):
        for editor in self._editors:
            editor.set_full_velocity()

    @listens("setting_changed")
    def __on_setting_changed(self, index, value):
        for editor in self._editors:
            self._modify_note_property_offset(editor, index, value)

    def _modify_note_property_offset(self, editor, index, value):
        if index == 1:
            editor.set_nudge_offset(value)
        else:
            if index == 2:
                editor.set_length_offset(value)
            else:
                if index == 3:
                    editor.set_velocity_offset(value)
                else:
                    if index == 4:
                        editor.set_velocity_deviation_offset(value)
                    else:
                        if index == 5:
                            editor.set_probability_offset(value)

    def _set_envelope_view_visible(self, visible):
        clip = self.song.view.detail_clip
        if liveobj_valid(clip):
            if visible:
                clip.view.show_envelope()
            else:
                clip.view.hide_envelope()

    def _set_settings_view_enabled(self, should_show_view):
        really_show_view = should_show_view and self.automation.can_automate_parameters if self.selected_setting == "automation" else should_show_view
        if really_show_view:
            if self.selected_mode == "disabled":
                self.selected_mode = "about_to_show"
        else:
            self._hide_settings()

    def _active_note_regions(self):
        all_active_regions = list(map((lambda e: e.active_note_regions), self._editors))
        return list(set(chain.from_iterable(all_active_regions)))

    @listens_group("active_note_regions")
    def _on_active_note_regions_changed(self, _):
        if self.is_enabled():
            all_steps = self._active_note_regions()
            self.automation.selected_time = all_steps
            self._update_note_infos()
            self._set_settings_view_enabled(len(all_steps) > 0 and self.selected_setting != None or self.is_touched)

    @listens_group("modify_all_notes")
    def __on_modify_all_notes_changed(self, editor):
        self.selected_mode = "about_to_show" if editor.modify_all_notes_enabled else "disabled"

    @listens_group("notes_changed")
    def _on_notes_changed(self, editor):
        self._update_infos_task.restart()

    @listens("detail_clip")
    def _on_detail_clip_changed(self):
        self.automation.clip = self.song.view.detail_clip if self.is_enabled() else None

    @listens("selected_track")
    def _on_selected_track_changed(self):
        self.selected_mode = "disabled"

    @initial_encoders.touched
    def initial_encoders(self, encoder):
        if self.selected_mode == "about_to_show":
            self._show_settings()

    @initial_encoders.value
    def initial_encoders(self, encoder, value):
        if self.selected_mode == "about_to_show":
            self._show_settings()

    @encoders.touched
    def encoders(self, encoder):
        if self._can_notify_is_touched(encoder):
            self.notify_is_touched()

    @encoders.released
    def encoders(self, encoder):
        if not self.is_touched:
            if not self._is_step_held():
                if not self._is_edit_all_notes_active():
                    self._hide_settings()
        if self._can_notify_is_touched(encoder):
            self.notify_is_touched()

    @encoders.value
    def encoders(self, encoder, value):
        self._notify_modification()

    def _can_notify_is_touched(self, encoder):
        if self.is_enabled():
            return self._settings_modes.selected_mode != "note_settings" or encoder.index < self.settings.number_of_settings
        return False

    def _is_edit_all_notes_active(self):
        return find_if((lambda e: e.modify_all_notes_enabled), self._editors) != None

    def _notify_modification(self):
        for editor in self._editors:
            editor.notify_modification()

    def _update_note_infosParse error at or near `COME_FROM' instruction at offset 210_1

    def _show_settings(self):
        if self.selected_mode != "enabled":
            self.selected_mode = "enabled"
            self._notify_modification()

    def _hide_settings(self):
        self.selected_mode = "disabled"

    def on_enabled_changed(self):
        super(NoteEditorSettingsComponent, self).on_enabled_changed()
        if not self.is_enabled():
            self.selected_mode = "disabled"

    def update(self):
        super(NoteEditorSettingsComponent, self).update()
        if self.is_enabled():
            self._on_detail_clip_changed()
