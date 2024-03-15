# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\control_surface.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 33300 bytes

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
_ifstmts_jumpl ::= c_stmts . JUMP_BACK
_stmts ::= _stmts . stmt
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
call ::= expr . pos_arg pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_METHOD_5
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_METHOD_8
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg . pos_arg pos_arg CALL_METHOD_3
call ::= expr pos_arg . pos_arg pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_METHOD_5
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_METHOD_8
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg . pos_arg CALL_METHOD_3
call ::= expr pos_arg pos_arg . pos_arg pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_METHOD_5
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg pos_arg CALL_METHOD_8
call ::= expr pos_arg pos_arg pos_arg . CALL_FUNCTION_3
call ::= expr pos_arg pos_arg pos_arg . CALL_METHOD_3
call ::= expr pos_arg pos_arg pos_arg . pos_arg CALL_METHOD_4
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg CALL_METHOD_5
call ::= expr pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_METHOD_8
call ::= expr pos_arg pos_arg pos_arg pos_arg . CALL_METHOD_4
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg CALL_METHOD_5
call ::= expr pos_arg pos_arg pos_arg pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_METHOD_8
call ::= expr pos_arg pos_arg pos_arg pos_arg CALL_METHOD_4 . 
call_ex ::= expr . starred CALL_FUNCTION_EX
call_ex ::= expr starred . CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr . expr expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr . expr CALL_FUNCTION_EX_KW
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX
call_ex_kw4 ::= expr expr expr . CALL_FUNCTION_EX_KW
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_kw36 ::= expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_10
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
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
continues ::= _stmts . lastl_stmt continue
continues ::= lastl_stmt . continue
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
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
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts JUMP_BACK
iflaststmtl ::= testexpr . c_stmts JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr . c_stmts JUMP_BACK POP_BLOCK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . JUMP_BACK COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts . JUMP_BACK POP_BLOCK
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lambda_body ::= expr . load_closure BUILD_TUPLE_1 LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_9
lastl_stmt ::= iflaststmtl . 
list ::= expr . BUILD_LIST_1
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfunc ::= expr . load_closure LOAD_CODE LOAD_STR MAKE_FUNCTION_9
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
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
slice2 ::= expr . expr BUILD_SLICE_2
slice2 ::= expr expr . BUILD_SLICE_2
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
starred ::= expr . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
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
   
 L. 828        42  LOAD_FAST                'from_identifier'
                  44  LOAD_FAST                'from_channel'
                  46  LOAD_FAST                'to_identifier'
                  48  LOAD_FAST                'to_channel'
                  50  CALL_METHOD_4         4  '4 positional arguments'
                  52  POP_TOP          
                  54  JUMP_FORWARD         56  'to 56'
                56_0  COME_FROM            54  '54'
->              56_1  COME_FROM            34  '34'
from __future__ import absolute_import, print_function, unicode_literals
from builtins import filter, map
from future.utils import iteritems, itervalues
from past.builtins import unicode
import logging, traceback
from collections import OrderedDict
from contextlib import contextmanager
from functools import partial
from itertools import chain
from pickle import dumps, loads
import Live
from ..base import BooleanContext, EventObject, const, find_if, first, in_range, inject, lazy_attribute, liveobj_valid, old_hasattr, task
from . import defaults, midi
from .control_element import OptimizedOwnershipHandler
from .device_bank_registry import DeviceBankRegistry
from .device_provider import DeviceProvider
from .elements import PhysicalDisplayElement
from .input_control_element import MIDI_CC_TYPE, MIDI_NOTE_TYPE, MIDI_PB_TYPE, MIDI_SYSEX_TYPE, InputControlElement, ScriptForwarding
from .message_scheduler import MessageScheduler
from .profile import profile
__all__ = ('SimpleControlSurface', 'ControlSurface')
logger = logging.getLogger(__name__)
CS_LIST_KEY = "control_surfaces"

def publish_control_surface(control_surface):
    get_control_surfaces().append(control_surface)


def get_control_surfaces():
    if isinstance(__builtins__, dict):
        if CS_LIST_KEY not in __builtins__.keys():
            __builtins__[CS_LIST_KEY] = []
        return __builtins__[CS_LIST_KEY]
    if not old_hasattr(__builtins__, CS_LIST_KEY):
        setattr(__builtins__, CS_LIST_KEY, [])
    return getattr(__builtins__, CS_LIST_KEY)


class SimpleControlSurface(EventObject):
    __events__ = ('received_midi', 'disconnect')
    preferences_key = None
    handle_undo_steps = False

    def __init__(self, c_instance=None, *a, **k):
        (super(SimpleControlSurface, self).__init__)(*a, **k)
        self.canonical_parent = None
        publish_control_surface(self)
        self._c_instance = c_instance
        self._pad_translations = None
        self._components = []
        self._displays = []
        self._controls = []
        self._forwarding_long_identifier_registry = {}
        self._forwarding_registry = {}
        self._is_sending_scheduled_messages = BooleanContext()
        self._remaining_scheduled_messages = []
        self._task_group = task.TaskGroup(auto_kill=False)
        self._in_build_midi_map = BooleanContext()
        self._suppress_requests_counter = 0
        self._rebuild_requests_during_suppression = 0
        self._enabled = True
        self._in_component_guard = BooleanContext()
        self._accumulate_midi_messages = BooleanContext()
        self._midi_message_dict = {}
        self._midi_message_list = []
        self._midi_message_count = 0
        self.mxd_midi_scheduler = MessageScheduler(self._do_send_midi, self._task_group.add(task.TimedCallbackTask()))
        self._ownership_handler = OptimizedOwnershipHandler()
        self._control_surface_injector = inject(element_ownership_handler=(const(self._ownership_handler)),
          parent_task_group=(const(self._task_group)),
          show_message=(const(self.show_message)),
          register_component=(const(self._register_component)),
          register_control=(const(self._register_control)),
          request_rebuild_midi_map=(const(self.request_rebuild_midi_map)),
          set_pad_translations=(const(self.set_pad_translations)),
          send_midi=(const(self._send_midi)),
          song=(const(self.song)),
          set_session_highlight=(const(self._c_instance.set_session_highlight))).everywhere()

    @property
    def components(self):
        return tuple(filter((lambda comp: not comp.is_private), self._components))

    @property
    def root_components(self):
        return tuple(filter((lambda comp: comp.is_root and not comp.is_private), self._components))

    @property
    def controls(self):
        return self._controls

    def _get_tasks(self):
        return self._task_group

    _tasks = property(_get_tasks)

    @property
    def application(self):
        return Live.Application.get_application()

    @property
    def song(self):
        return self._c_instance.song()

    def disconnect(self):
        self._pre_serialize()
        self.notify_disconnect(self)
        self._disconnect_and_unregister_all_components()
        with self.component_guard():
            for control in self._controls:
                control.disconnect()
                control.canonical_parent = None

        self._forwarding_registry = None
        self._controls = None
        self._displays = None
        self._pad_translations = None
        cs_list = get_control_surfaces()
        if self in cs_list:
            cs_list.remove(self)
        self._task_group.clear()
        super(SimpleControlSurface, self).disconnect()

    def can_lock_to_devices(self):
        return False

    def suggest_map_mode(self, cc_no, channel):
        suggested_map_mode = -1
        for control in self._controls:
            if isinstance(control, InputControlElement) and control.message_type() == MIDI_CC_TYPE and control.message_identifier() == cc_no and control.message_channel() == channel:
                suggested_map_mode = control.message_map_mode()
                break

        return suggested_map_mode

    def supports_pad_translation(self):
        return self._pad_translations is not None

    def show_message(self, message):
        self._c_instance.show_message(message)

    def connect_script_instances(self, instanciated_scripts):
        pass

    def request_rebuild_midi_map(self):
        if self._suppress_requests_counter > 0:
            self._rebuild_requests_during_suppression += 1
        else:
            self._c_instance.request_rebuild_midi_map()

    def build_midi_map(self, midi_map_handle):
        with self._in_build_midi_map():
            self._forwarding_registry.clear()
            self._forwarding_long_identifier_registry.clear()
            for control in self._controls:
                if isinstance(control, InputControlElement):
                    control.install_connections(self._translate_message, partial(self._install_mapping, midi_map_handle), partial(self._install_forwarding, midi_map_handle))

            if self._pad_translations is not None:
                self._c_instance.set_pad_translation(self._pad_translations)

    def port_settings_changed(self):
        self.refresh_state()

    def refresh_state(self):
        self.update()

    def update(self):
        with self.component_guard():
            for control in self._controls:
                control.clear_send_cache()

            for component in self._components:
                component.update()

    @profile
    def update_display(self):
        with self.component_guard():
            self.update_display_hook()
            with self._is_sending_scheduled_messages():
                self._task_group.update(defaults.TIMER_DELAY)

    def update_display_hook(self):
        pass

    @profile
    def receive_midi(self, midi_bytes):
        with self.component_guard():
            self._do_receive_midi(midi_bytes)

    @profile
    def receive_midi_chunk(self, midi_chunk):
        with self.component_guard():
            self._do_receive_midi_chunk(midi_chunk)

    @staticmethod
    def _receive_midi_data(recipient, data):
        recipient.receive_value(data)

    def _do_receive_midi(self, midi_bytes):
        (self.notify_received_midi)(*midi_bytes)
        self.mxd_midi_scheduler.handle_message(midi_bytes)
        self.process_midi_bytes(midi_bytes, self._receive_midi_data)

    @staticmethod
    def _merge_midi_data(recipient, data, midi_data):
        if recipient.allow_receiving_chunks:
            _, values = midi_data.setdefault(recipient, (recipient, []))
            values.append(data)
        else:
            midi_data[object()] = (
             recipient, data)

    def _do_receive_midi_chunk(self, midi_chunk):
        midi_data_for_recipient = OrderedDict()
        for midi_bytes in midi_chunk:
            (self.notify_received_midi)(*midi_bytes)
            self.mxd_midi_scheduler.handle_message(midi_bytes)
            self.process_midi_bytes(midi_bytes, partial((self._merge_midi_data), midi_data=midi_data_for_recipient))

        for recipient, data in itervalues(midi_data_for_recipient):
            if recipient.allow_receiving_chunks:
                recipient.receive_chunk(tuple(data))
            else:
                recipient.receive_value(data)

    def process_midi_bytes(self, midi_bytes, midi_processor):
        if midi.is_sysex(midi_bytes):
            result = self.get_registry_entry_for_sysex_midi_message(midi_bytes)
            if result is not None:
                identifier, recipient = result
                midi_processor(recipient, midi_bytes[len(identifier)[:-1]])
            elif self.received_midi_listener_count() == 0:
                logger.warning("Got unknown sysex message: " + midi.pretty_print_bytes(midi_bytes))
        else:
            recipient = self.get_recipient_for_nonsysex_midi_message(midi_bytes)
            if recipient is not None:
                midi_processor(recipient, midi.extract_value(midi_bytes))
            else:
                if self.received_midi_listener_count() == 0:
                    logger.warning("Got unknown message: " + midi.pretty_print_bytes(midi_bytes))

    def get_recipient_for_nonsysex_midi_message(self, midi_bytes):
        forwarding_key = midi_bytes[None[:1 if midi.is_pitchbend(midi_bytes) else 2]]
        if forwarding_key in self._forwarding_registry:
            return self._forwarding_registry[forwarding_key]

    def get_registry_entry_for_sysex_midi_message(self, midi_bytes):
        return find_if((lambda identifier_recipient: midi_bytes[None[:len(identifier_recipient[0])]] == identifier_recipient[0]), iteritems(self._forwarding_long_identifier_registry))

    @contextmanager
    def suppressing_rebuild_requests(self):
        try:
            self._set_suppress_rebuild_requests(True)
            yield
        finally:
            self._set_suppress_rebuild_requests(False)

    def _set_suppress_rebuild_requests(self, suppress_requests):
        if suppress_requests:
            self._suppress_requests_counter += 1
        else:
            self._suppress_requests_counter -= 1
            if self._suppress_requests_counter == 0:
                if self._rebuild_requests_during_suppression > 0:
                    self.request_rebuild_midi_map()
                    self._rebuild_requests_during_suppression = 0

    def set_pad_translations(self, pad_translations):

        def check_translation(translation):
            return True

        self._pad_translations = pad_translations

    def set_enabled(self, enable):
        bool_enable = bool(enable)
        if self._enabled != bool_enable:
            with self.component_guard():
                self._enabled = bool_enable
                root_components = self.root_components
                components = root_components if len(root_components) > 0 else self._components
                for component in components:
                    component._set_enabled_recursive(bool_enable)

    def schedule_message(self, delay_in_ticks, callback, parameter=None):
        if not self._is_sending_scheduled_messages:
            delay_in_ticks -= 1
        else:
            message_reference = [
             None]

            def message(delta):
                if parameter:
                    callback(parameter)
                else:
                    callback()
                self._remaining_scheduled_messages.remove(message_reference)

            message_reference[0] = message
            self._remaining_scheduled_messages.append(message_reference)
            if delay_in_ticks:
                self._task_group.add(task.sequence(task.delay(delay_in_ticks), message))
            else:
                self._task_group.add(message)

    def set_feedback_channels(self, channels):
        self._c_instance.set_feedback_channels(channels)

    def set_controlled_track(self, track):
        self._c_instance.set_controlled_track(track)

    def release_controlled_track(self):
        self._c_instance.release_controlled_track()

    def _register_control(self, control):
        self._controls.append(control)
        control.canonical_parent = self
        if isinstance(control, PhysicalDisplayElement):
            self._displays.append(control)
        if old_hasattr(control, "_is_resource_based"):
            control._is_resource_based = True

    def _register_component(self, component):
        self._components.append(component)
        component.canonical_parent = self

    def _disconnect_and_unregister_all_components(self):
        with self.component_guard():
            for component in self._components:
                component.canonical_parent = None
                component.disconnect()

        self._components = []

    @contextmanager
    def component_guard(self):
        if not self._in_component_guard:
            with self._in_component_guard():
                with self._component_guard():
                    yield
        else:
            yield

    @contextmanager
    def _component_guard(self):
        with self._control_surface_injector:
            with self.suppressing_rebuild_requests():
                with self.accumulating_midi_messages():
                    yield
                    self._ownership_handler.commit_ownership_changes()

    @profile
    def call_listeners(self, listeners):
        with self.component_guard():
            for listener in filter(liveobj_valid, listeners):
                listener()

    @contextmanager
    def accumulating_midi_messages(self):
        with self._accumulate_midi_messages():
            try:
                yield
            finally:
                self._flush_midi_messages()

    def get_control_by_name(self, control_name):
        return find_if((lambda c: c.name == control_name), self._controls)

    def get_component_by_name(self, component_name):
        return find_if((lambda c: c.name == component_name), self.components)

    def _send_midi(self, midi_event_bytes, optimized=True):
        if self._accumulate_midi_messages:
            sysex_status_byte = 240
            entry = (self._midi_message_count, midi_event_bytes)
            if optimized and midi_event_bytes[0] != sysex_status_byte:
                key = (
                 midi_event_bytes[0], midi_event_bytes[1])
                self._midi_message_dict[key] = entry
            else:
                self._midi_message_list.append(entry)
            self._midi_message_count += 1
        else:
            self._do_send_midi(midi_event_bytes)
        return True

    def _flush_midi_messages(self):
        sorted_messages = sorted((chain(self._midi_message_list, itervalues(self._midi_message_dict))),
          key=first)
        for _, message in sorted_messages:
            self._do_send_midi(message)

        self._midi_message_dict.clear()
        self._midi_message_list[None[:None]] = []
        self._midi_message_count = 0

    def _do_send_midi(self, midi_event_bytes):
        try:
            self._c_instance.send_midi(midi_event_bytes)
        except Exception:
            logger.error("Error while sending midi message %s", str(midi_event_bytes))
            traceback.print_exc()
            return False
        else:
            return True

    def _install_mapping(self, midi_map_handle, control, parameter, feedback_delay, feedback_map):
        success = False
        feedback_rule = None
        if control.message_type() == MIDI_NOTE_TYPE:
            feedback_rule = Live.MidiMap.NoteFeedbackRule()
            feedback_rule.note_no = control.message_identifier()
            feedback_rule.vel_map = feedback_map
        else:
            if control.message_type() == MIDI_CC_TYPE:
                feedback_rule = Live.MidiMap.CCFeedbackRule()
                feedback_rule.cc_no = control.message_identifier()
                feedback_rule.cc_value_map = feedback_map
            else:
                if control.message_type() == MIDI_PB_TYPE:
                    feedback_rule = Live.MidiMap.PitchBendFeedbackRule()
                    feedback_rule.value_pair_map = feedback_map
                else:
                    feedback_rule.channel = control.message_channel()
                    feedback_rule.delay_in_ms = feedback_delay
                    feedback_rule.enabled = control.is_feedback_enabled
                    if control.message_type() == MIDI_NOTE_TYPE:
                        success = Live.MidiMap.map_midi_note_with_feedback_map(midi_map_handle, parameter, control.message_channel(), control.message_identifier(), feedback_rule)
                    else:
                        if control.message_type() == MIDI_CC_TYPE:
                            success = Live.MidiMap.map_midi_cc_with_feedback_map(midi_map_handle, parameter, control.message_channel(), control.message_identifier(), control.message_map_mode(), feedback_rule, not control.needs_takeover(), control.mapping_sensitivity)
                        else:
                            if control.message_type() == MIDI_PB_TYPE:
                                success = Live.MidiMap.map_midi_pitchbend_with_feedback_map(midi_map_handle, parameter, control.message_channel(), feedback_rule, not control.needs_takeover())
                if success:
                    Live.MidiMap.send_feedback_for_parameter(midi_map_handle, parameter)
                return success

    def _install_forwarding(self, midi_map_handle, control, forwarding_type=ScriptForwarding.exclusive):
        success = False
        should_consume_event = forwarding_type == ScriptForwarding.exclusive
        if control.message_type() == MIDI_NOTE_TYPE:
            success = Live.MidiMap.forward_midi_note(self._c_instance.handle(), midi_map_handle, control.message_channel(), control.message_identifier(), should_consume_event)
        else:
            if control.message_type() == MIDI_CC_TYPE:
                success = Live.MidiMap.forward_midi_cc(self._c_instance.handle(), midi_map_handle, control.message_channel(), control.message_identifier(), should_consume_event)
            else:
                if control.message_type() == MIDI_PB_TYPE:
                    success = Live.MidiMap.forward_midi_pitchbend(self._c_instance.handle(), midi_map_handle, control.message_channel())
                else:
                    success = True
        if success:
            forwarding_keys = control.identifier_bytes()
            for key in forwarding_keys:
                registry = self._forwarding_registry if control.message_type() != MIDI_SYSEX_TYPE else self._forwarding_long_identifier_registry
                registry[key] = control

        return success

    def _translate_messageParse error at or near `COME_FROM' instruction at offset 56_1

    @lazy_attribute
    def preferences(self):
        if self.preferences_key is None:
            raise RuntimeError("Trying to access preferences without providing a preference_key")
        preferences = self._c_instance.preferences(self.preferences_key)
        pref_dict = {}
        try:
            pref_dict = loads(bytes(preferences))
        except Exception as e:
            try:
                logger.error("Error while loading control surface preferences %s", str(e))
            finally:
                e = None
                del e

        preferences.set_serializer(lambda: dumps(pref_dict))
        return pref_dict

    def _pre_serialize(self):
        if self.preferences_key is not None:
            preferences = self._c_instance.preferences(self.preferences_key)
            dump = dumps(self.preferences)
            preferences.set_serializer(lambda: dump)


class ControlSurface(SimpleControlSurface):
    device_provider_class = DeviceProvider

    def __init__(self, *a, **k):
        (super(ControlSurface, self).__init__)(*a, **k)
        self._device_provider = None
        self._device_bank_registry = None
        if self.device_provider_class:
            self._init_device_provider()
        self._device_support_injector = inject(device_provider=(const(self.device_provider)),
          device_bank_registry=(const(self._device_bank_registry))).everywhere()

    def _init_device_provider(self):
        self._device_provider = self.register_disconnectable(self.device_provider_class(song=(self.song)))
        self._device_bank_registry = self.register_disconnectable(DeviceBankRegistry())
        self._c_instance.update_locks()
        self._device_provider.update_device_selection()

    @property
    def device_provider(self):
        return self._device_provider

    def disconnect(self):
        self._device_provider = None
        self._device_bank_registry = None
        super(ControlSurface, self).disconnect()

    def can_lock_to_devices(self):
        return True

    def lock_to_device(self, device):
        with self.component_guard():
            self._device_provider.lock_to_device(device)

    def unlock_from_device(self, device):
        with self.component_guard():
            self._device_provider.unlock_from_device()

    def restore_bank(self, bank_index):
        device = self._device_provider.device
        if self._device_provider.is_locked_to_device:
            if liveobj_valid(device):
                with self.component_guard():
                    self._device_bank_registry.set_device_bank(device, bank_index)

    def toggle_lock(self):
        self._c_instance.toggle_lock()

    @contextmanager
    def _component_guard(self):
        with super(ControlSurface, self)._component_guard():
            with self._device_support_injector:
                yield
