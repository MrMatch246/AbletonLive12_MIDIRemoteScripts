# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MackieControl_Classic\ChannelStripController.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 51750 bytes

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
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg CALL_METHOD_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg CALL_METHOD_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_stmt ::= expr . POP_TOP
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
continues ::= _stmts lastl_stmt . continue
continues ::= lastl_stmt . continue
else_suite ::= suite_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= subscript . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
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
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
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
ifelsestmt ::= testexpr c_stmts come_froms else_suite . come_froms
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
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= return . 
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
stmt ::= return . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
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
testexpr_cf ::= testexpr . come_froms
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr BUILD_TUPLE_2 . 
tuple ::= expr expr expr . BUILD_TUPLE_3
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 519        76  LOAD_CONST               (None, None)
                  78  RETURN_VALUE     
                  80  JUMP_FORWARD         82  'to 82'
->              82_0  COME_FROM            80  '80'

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= \e__come_froms COME_FROM_LOOP . 
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
_ifstmts_jumpl ::= c_stmts JUMP_BACK . 
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
and ::= expr jmp_false expr jmp_false . 
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
binary_operator ::= BINARY_ADD . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg CALL_METHOD_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg CALL_METHOD_2
call ::= expr . pos_arg pos_arg pos_arg CALL_FUNCTION_3
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg CALL_METHOD_2
call ::= expr pos_arg . pos_arg pos_arg CALL_FUNCTION_3
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_METHOD_2
call ::= expr pos_arg pos_arg . pos_arg CALL_FUNCTION_3
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_stmt ::= expr . POP_TOP
cf_jf_else ::= come_froms . JUMP_FORWARD ELSE
cf_jump_back ::= COME_FROM . JUMP_BACK
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
come_from_loops ::= \e_come_from_loops COME_FROM_LOOP . 
come_from_loops ::= come_from_loops . COME_FROM_LOOP
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
else_suite ::= suite_stmts . 
else_suite_opt ::= else_suite . 
else_suitec ::= c_stmts . 
else_suitec ::= returns . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= subscript . 
expr ::= tuple . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
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
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
for_block ::= l_stmts_opt _come_froms . JUMP_BACK
for_block ::= l_stmts_opt come_from_loops . JUMP_BACK
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
get_for_iter ::= GET_ITER _come_froms . FOR_ITER
get_for_iter ::= GET_ITER _come_froms FOR_ITER . 
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
if_exp_37b ::= expr jmp_false expr POP_JUMP_IF_FALSE . jump_forward_else expr
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
ifelsestmtl ::= testexpr c_stmts_opt jump_forward_else else_suitec . 
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
iflaststmtl ::= testexpr c_stmts JUMP_BACK . 
iflaststmtl ::= testexpr c_stmts JUMP_BACK . COME_FROM_LOOP
iflaststmtl ::= testexpr c_stmts JUMP_BACK . POP_BLOCK
iflaststmtl ::= testexpr c_stmts JUMP_BACK POP_BLOCK . 
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
jb_cfs ::= \e_come_from_opt . JUMP_BACK come_froms
jb_cfs ::= \e_come_from_opt JUMP_BACK . come_froms
jb_cfs ::= come_from_opt . JUMP_BACK come_froms
jb_else ::= JUMP_BACK . COME_FROM
jb_else ::= JUMP_BACK . ELSE
jf_cfs ::= JUMP_FORWARD . _come_froms
jf_cfs ::= JUMP_FORWARD \e__come_froms . 
jf_cfs ::= JUMP_FORWARD _come_froms . 
jmp_false ::= POP_JUMP_IF_FALSE . 
jump_absolute_else ::= come_froms . _jump COME_FROM
jump_forward_else ::= JUMP_FORWARD . 
jump_forward_else ::= JUMP_FORWARD . COME_FROM
jump_forward_else ::= JUMP_FORWARD . ELSE
jump_forward_else ::= JUMP_FORWARD COME_FROM . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lastl_stmt . 
l_stmts ::= lastl_stmt . come_froms l_stmts
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_1
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
opt_come_from_except ::= _come_froms . 
or ::= and . jitop_come_from_expr COME_FROM
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr RETURN_VALUE . 
return ::= return_expr RETURN_VALUE . COME_FROM
return ::= return_expr RETURN_VALUE COME_FROM . 
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
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
sstmt ::= return . RETURN_LAST
sstmt ::= return RETURN_LAST . 
sstmt ::= sstmt . RETURN_LAST
sstmt ::= sstmt RETURN_LAST . 
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= for . 
stmt ::= ifelsestmt . 
stmt ::= ifstmt . 
stmt ::= ifstmtl . 
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
testexpr_cf ::= testexpr . come_froms
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr jmp_false . COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr BUILD_TUPLE_2 . 
tuple ::= expr expr expr . BUILD_TUPLE_3
unary_not ::= expr . UNARY_NOT
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
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L. 657       102  LOAD_FAST                't'
                 104  LOAD_ATTR                available_output_routing_channels
                 106  LOAD_FAST                'target_string'
                 108  CALL_FUNCTION_2       2  '2 positional arguments'
                 110  LOAD_FAST                't'
                 112  STORE_ATTR               output_routing_channel
                 114  JUMP_FORWARD        116  'to 116'
               116_0  COME_FROM           114  '114'
               116_1  COME_FROM            98  '98'
               116_2  COME_FROM            88  '88'
               116_3  COME_FROM            62  '62'
->             116_4  COME_FROM            36  '36'
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import chr, range
from past.utils import old_div
from itertools import chain
from _Generic.Devices import *
from .MackieControlComponent import *
flatten_target = lambda routing_target: routing_target.display_name

def flatten_target_list(target_list):
    target_names = []
    for target in target_list:
        name = flatten_target(target)
        if name not in target_names:
            target_names.append(name)

    return list(target_names)


def target_by_name(target_list, name):
    matches = [t for t in target_list if t.display_name == name]
    if matches:
        return matches[0]


class ChannelStripController(MackieControlComponent):

    def __init__(self, main_script, channel_strips, master_strip, main_display_controller):
        MackieControlComponent.__init__(self, main_script)
        self._ChannelStripController__left_extensions = []
        self._ChannelStripController__right_extensions = []
        self._ChannelStripController__own_channel_strips = channel_strips
        self._ChannelStripController__master_strip = master_strip
        self._ChannelStripController__channel_strips = channel_strips
        self._ChannelStripController__main_display_controller = main_display_controller
        self._ChannelStripController__meters_enabled = False
        self._ChannelStripController__assignment_mode = CSM_VOLPAN
        self._ChannelStripController__sub_mode_in_io_mode = CSM_IO_FIRST_MODE
        self._ChannelStripController__plugin_mode = PCM_DEVICES
        self._ChannelStripController__plugin_mode_offsets = [0 for x in range(PCM_NUMMODES)]
        self._ChannelStripController__chosen_plugin = None
        self._ChannelStripController__ordered_plugin_parameters = []
        self._ChannelStripController__displayed_plugins = []
        self._ChannelStripController__last_attached_selected_track = None
        self._ChannelStripController__send_mode_offset = 0
        self._ChannelStripController__flip = False
        self._ChannelStripController__view_returns = False
        self._ChannelStripController__bank_cha_offset = 0
        self._ChannelStripController__bank_cha_offset_returns = 0
        self._ChannelStripController__within_track_added_or_deleted = False
        self.song().add_visible_tracks_listener(self._ChannelStripController__on_tracks_added_or_deleted)
        self.song().view.add_selected_track_listener(self._ChannelStripController__on_selected_track_changed)
        for t in chain(self.song().visible_tracks, self.song().return_tracks):
            if not t.solo_has_listener(self._ChannelStripController__update_rude_solo_led):
                t.add_solo_listener(self._ChannelStripController__update_rude_solo_led)
            if not t.has_audio_output_has_listener(self._ChannelStripController__on_any_tracks_output_type_changed):
                t.add_has_audio_output_listener(self._ChannelStripController__on_any_tracks_output_type_changed)

        self._ChannelStripController__on_selected_track_changed()
        for s in self._ChannelStripController__own_channel_strips:
            s.set_channel_strip_controller(self)

        self._ChannelStripController__reassign_channel_strip_offsets()
        self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
        self._last_assignment_mode = self._ChannelStripController__assignment_mode

    def destroy(self):
        self.song().remove_visible_tracks_listener(self._ChannelStripController__on_tracks_added_or_deleted)
        self.song().view.remove_selected_track_listener(self._ChannelStripController__on_selected_track_changed)
        for t in chain(self.song().visible_tracks, self.song().return_tracks):
            if t.solo_has_listener(self._ChannelStripController__update_rude_solo_led):
                t.remove_solo_listener(self._ChannelStripController__update_rude_solo_led)
            if t.has_audio_output_has_listener(self._ChannelStripController__on_any_tracks_output_type_changed):
                t.remove_has_audio_output_listener(self._ChannelStripController__on_any_tracks_output_type_changed)

        st = self._ChannelStripController__last_attached_selected_track
        if st:
            if st.devices_has_listener(self._ChannelStripController__on_selected_device_chain_changed):
                st.remove_devices_listener(self._ChannelStripController__on_selected_device_chain_changed)
        for note in channel_strip_assignment_switch_ids:
            self.send_midi((NOTE_ON_STATUS, note, BUTTON_STATE_OFF))

        for note in channel_strip_control_switch_ids:
            self.send_midi((NOTE_ON_STATUS, note, BUTTON_STATE_OFF))

        self.send_midi((NOTE_ON_STATUS, SELECT_RUDE_SOLO, BUTTON_STATE_OFF))
        self.send_midi((CC_STATUS, 75, g7_seg_led_conv_table[" "]))
        self.send_midi((CC_STATUS, 74, g7_seg_led_conv_table[" "]))
        MackieControlComponent.destroy(self)

    def set_controller_extensions(self, left_extensions, right_extensions):
        self._ChannelStripController__left_extensions = left_extensions
        self._ChannelStripController__right_extensions = right_extensions
        self._ChannelStripController__channel_strips = []
        stack_offset = 0
        for le in left_extensions:
            for s in le.channel_strips():
                self._ChannelStripController__channel_strips.append(s)
                s.set_stack_offset(stack_offset)

            stack_offset += NUM_CHANNEL_STRIPS

        for s in self._ChannelStripController__own_channel_strips:
            self._ChannelStripController__channel_strips.append(s)
            s.set_stack_offset(stack_offset)

        stack_offset += NUM_CHANNEL_STRIPS
        for re in right_extensions:
            for s in re.channel_strips():
                self._ChannelStripController__channel_strips.append(s)
                s.set_stack_offset(stack_offset)

            stack_offset += NUM_CHANNEL_STRIPS

        for s in self._ChannelStripController__channel_strips:
            s.set_channel_strip_controller(self)

        self.refresh_state()

    def refresh_state(self):
        self._ChannelStripController__update_assignment_mode_leds()
        self._ChannelStripController__update_assignment_display()
        self._ChannelStripController__update_rude_solo_led()
        self._ChannelStripController__reassign_channel_strip_offsets()
        self._ChannelStripController__on_flip_changed()
        self._ChannelStripController__update_view_returns_mode()

    def request_rebuild_midi_map(self):
        MackieControlComponent.request_rebuild_midi_map(self)
        for ex in self._ChannelStripController__left_extensions + self._ChannelStripController__right_extensions:
            ex.request_rebuild_midi_map()

    def on_update_display_timer(self):
        self._ChannelStripController__update_channel_strip_strings()

    def toggle_meter_mode(self):
        self._ChannelStripController__meters_enabled = not self._ChannelStripController__meters_enabled
        self._ChannelStripController__apply_meter_mode(meter_state_changed=True)

    def handle_assignment_switch_ids(self, switch_id, value):
        if switch_id == SID_ASSIGNMENT_IO:
            if value == BUTTON_PRESSED:
                self._ChannelStripController__set_assignment_mode(CSM_IO)
        else:
            if switch_id == SID_ASSIGNMENT_SENDS:
                if value == BUTTON_PRESSED:
                    self._ChannelStripController__set_assignment_mode(CSM_SENDS)
            else:
                if switch_id == SID_ASSIGNMENT_PAN:
                    if value == BUTTON_PRESSED:
                        self._ChannelStripController__set_assignment_mode(CSM_VOLPAN)
                else:
                    if switch_id == SID_ASSIGNMENT_PLUG_INS:
                        if value == BUTTON_PRESSED:
                            self._ChannelStripController__set_assignment_mode(CSM_PLUGINS)
                    else:
                        if switch_id == SID_ASSIGNMENT_EQ:
                            if value == BUTTON_PRESSED:
                                self._ChannelStripController__switch_to_prev_page()
                        else:
                            if switch_id == SID_ASSIGNMENT_DYNAMIC:
                                if value == BUTTON_PRESSED:
                                    self._ChannelStripController__switch_to_next_page()
                            else:
                                if switch_id == SID_FADERBANK_PREV_BANK:
                                    if value == BUTTON_PRESSED:
                                        if self.shift_is_pressed():
                                            self._ChannelStripController__set_channel_offset(0)
                                        else:
                                            self._ChannelStripController__set_channel_offset(self._ChannelStripController__strip_offset() - len(self._ChannelStripController__channel_strips))
                                else:
                                    if switch_id == SID_FADERBANK_NEXT_BANK:
                                        if value == BUTTON_PRESSED:
                                            if self.shift_is_pressed():
                                                last_possible_offset = old_div(self._ChannelStripController__controlled_num_of_tracks() - self._ChannelStripController__strip_offset(), len(self._ChannelStripController__channel_strips)) * len(self._ChannelStripController__channel_strips) + self._ChannelStripController__strip_offset()
                                                if last_possible_offset == self._ChannelStripController__controlled_num_of_tracks():
                                                    last_possible_offset -= len(self._ChannelStripController__channel_strips)
                                                self._ChannelStripController__set_channel_offset(last_possible_offset)
                                            else:
                                                if self._ChannelStripController__strip_offset() < self._ChannelStripController__controlled_num_of_tracks() - len(self._ChannelStripController__channel_strips):
                                                    self._ChannelStripController__set_channel_offset(self._ChannelStripController__strip_offset() + len(self._ChannelStripController__channel_strips))
                                        else:
                                            if switch_id == SID_FADERBANK_PREV_CH:
                                                if value == BUTTON_PRESSED:
                                                    if self.shift_is_pressed():
                                                        self._ChannelStripController__set_channel_offset(0)
                                            else:
                                                self._ChannelStripController__set_channel_offset(self._ChannelStripController__strip_offset() - 1)
                                    else:
                                        pass
        if switch_id == SID_FADERBANK_NEXT_CH:
            if value == BUTTON_PRESSED:
                if self.shift_is_pressed():
                    self._ChannelStripController__set_channel_offset(self._ChannelStripController__controlled_num_of_tracks() - len(self._ChannelStripController__channel_strips))
            elif self._ChannelStripController__strip_offset() < self._ChannelStripController__controlled_num_of_tracks() - len(self._ChannelStripController__channel_strips):
                self._ChannelStripController__set_channel_offset(self._ChannelStripController__strip_offset() + 1)
        else:
            if switch_id == SID_FADERBANK_FLIP:
                if value == BUTTON_PRESSED:
                    self._ChannelStripController__toggle_flip()
            elif switch_id == SID_FADERBANK_EDIT:
                if value == BUTTON_PRESSED:
                    self._ChannelStripController__toggle_view_returns()

    def handle_vpot_rotation(self, strip_index, stack_offset, cc_value):
        if self._ChannelStripController__assignment_mode == CSM_IO:
            if cc_value >= 64:
                direction = -1
            else:
                direction = 1
            channel_strip = self._ChannelStripController__channel_strips[stack_offset + strip_index]
            current_routing = self._ChannelStripController__routing_target(channel_strip)
            available_routings = self._ChannelStripController__available_routing_targets(channel_strip)
            if current_routing and available_routings:
                if current_routing in available_routings:
                    i = list(available_routings).index(current_routing)
                    if direction == 1:
                        new_i = min(len(available_routings) - 1, i + direction)
                    else:
                        new_i = max(0, i + direction)
                    new_routing = available_routings[new_i]
                else:
                    if len(available_routings):
                        new_routing = available_routings[0]
                self._ChannelStripController__set_routing_target(channel_strip, new_routing)
        elif self._ChannelStripController__assignment_mode == CSM_PLUGINS:
            pass
        else:
            channel_strip = self._ChannelStripController__channel_strips[stack_offset + strip_index]

    def handle_fader_touch(self, strip_offset, stack_offset, touched):
        self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=True)

    def handle_pressed_v_pot(self, strip_index, stack_offset):
        if not (self._ChannelStripController__assignment_mode == CSM_VOLPAN or self._ChannelStripController__assignment_mode == CSM_SENDS):
            if not self._ChannelStripController__assignment_mode == CSM_PLUGINS or self._ChannelStripController__plugin_mode == PCM_PARAMETERS:
                if stack_offset + strip_index in range(0, len(self._ChannelStripController__channel_strips)):
                    param = self._ChannelStripController__channel_strips[stack_offset + strip_index].v_pot_parameter()
                elif param:
                    if param.is_enabled:
                        if param.is_quantized:
                            if param.value + 1 > param.max:
                                param.value = param.min
                            else:
                                param.value = param.value + 1
                        else:
                            param.value = param.default_value
        elif self._ChannelStripController__assignment_mode == CSM_PLUGINS:
            if self._ChannelStripController__plugin_mode == PCM_DEVICES:
                device_index = strip_index + stack_offset + self._ChannelStripController__plugin_mode_offsets[PCM_DEVICES]
                if device_index >= 0:
                    if device_index < len(self.song().view.selected_track.devices):
                        if self._ChannelStripController__chosen_plugin != None:
                            self._ChannelStripController__chosen_plugin.remove_parameters_listener(self._ChannelStripController__on_parameter_list_of_chosen_plugin_changed)
                        self._ChannelStripController__chosen_plugin = self.song().view.selected_track.devices[device_index]
                        if self._ChannelStripController__chosen_plugin != None:
                            self._ChannelStripController__chosen_plugin.add_parameters_listener(self._ChannelStripController__on_parameter_list_of_chosen_plugin_changed)
                        self._ChannelStripController__reorder_parameters()
                        self._ChannelStripController__plugin_mode_offsets[PCM_PARAMETERS] = 0
                        self._ChannelStripController__set_plugin_mode(PCM_PARAMETERS)

    def assignment_mode(self):
        return self._ChannelStripController__assignment_mode

    def __strip_offset(self):
        if self._ChannelStripController__view_returns:
            return self._ChannelStripController__bank_cha_offset_returns
        return self._ChannelStripController__bank_cha_offset

    def __controlled_num_of_tracks(self):
        if self._ChannelStripController__view_returns:
            return len(self.song().return_tracks)
        return len(self.song().visible_tracks)

    def __send_parameter(self, strip_index, stack_index):
        send_index = strip_index + stack_index + self._ChannelStripController__send_mode_offset
        if send_index < len(self.song().view.selected_track.mixer_device.sends):
            p = self.song().view.selected_track.mixer_device.sends[send_index]
            return (p, p.name)
        return (None, None)

    def __plugin_parameterParse error at or near `COME_FROM' instruction at offset 82_0

    def __any_slider_is_touched(self):
        for s in self._ChannelStripController__channel_strips:
            if s.is_touched():
                return True

        return False

    def __can_flip(self):
        if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
            if self._ChannelStripController__plugin_mode == PCM_DEVICES:
                return False
        if self._ChannelStripController__assignment_mode == CSM_IO:
            return False
        return True

    def __can_switch_to_prev_page(self):
        if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
            return self._ChannelStripController__plugin_mode_offsets[self._ChannelStripController__plugin_mode] > 0
        if self._ChannelStripController__assignment_mode == CSM_SENDS:
            return self._ChannelStripController__send_mode_offset > 0
        return False

    def __can_switch_to_next_page(self):
        if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
            sel_track = self.song().view.selected_track
            if self._ChannelStripController__plugin_mode == PCM_DEVICES:
                return self._ChannelStripController__plugin_mode_offsets[PCM_DEVICES] + len(self._ChannelStripController__channel_strips) < len(sel_track.devices)
            if self._ChannelStripController__plugin_mode == PCM_PARAMETERS:
                parameters = self._ChannelStripController__ordered_plugin_parameters
                return self._ChannelStripController__plugin_mode_offsets[PCM_PARAMETERS] + len(self._ChannelStripController__channel_strips) < len(parameters)
        elif self._ChannelStripController__assignment_mode == CSM_SENDS:
            return self._ChannelStripController__send_mode_offset + len(self._ChannelStripController__channel_strips) < len(self.song().return_tracks)
        return False

    def __available_routing_targets(self, channel_strip):
        t = channel_strip.assigned_track()
        if t:
            if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_INPUT_MAIN:
                return flatten_target_list(t.available_input_routing_types)
            if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_INPUT_SUB:
                return flatten_target_list(t.available_input_routing_channels)
            if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_OUTPUT_MAIN:
                return flatten_target_list(t.available_output_routing_types)
            if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_OUTPUT_SUB:
                return flatten_target_list(t.available_output_routing_channels)
        else:
            return

    def __routing_target(self, channel_strip):
        t = channel_strip.assigned_track()
        if t:
            if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_INPUT_MAIN:
                return flatten_target(t.input_routing_type)
            if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_INPUT_SUB:
                return flatten_target(t.input_routing_channel)
            if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_OUTPUT_MAIN:
                return flatten_target(t.output_routing_type)
            if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_OUTPUT_SUB:
                return flatten_target(t.output_routing_channel)
        else:
            return

    def __set_routing_targetParse error at or near `COME_FROM' instruction at offset 116_4

    def __set_channel_offset(self, new_offset):
        if new_offset < 0:
            new_offset = 0
        else:
            if new_offset >= self._ChannelStripController__controlled_num_of_tracks():
                new_offset = self._ChannelStripController__controlled_num_of_tracks() - 1
            elif self._ChannelStripController__view_returns:
                self._ChannelStripController__bank_cha_offset_returns = new_offset
            else:
                self._ChannelStripController__bank_cha_offset = new_offset
            self._ChannelStripController__main_display_controller.set_channel_offset(new_offset)
            self._ChannelStripController__reassign_channel_strip_offsets()
            self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
            self._ChannelStripController__update_channel_strip_strings()
            self.request_rebuild_midi_map()

    def __set_assignment_mode(self, mode):
        for plugin in self._ChannelStripController__displayed_plugins:
            if plugin != None:
                plugin.remove_name_listener(self._ChannelStripController__update_plugin_names)

        self._ChannelStripController__displayed_plugins = []
        if mode == CSM_PLUGINS:
            self._ChannelStripController__assignment_mode = mode
            self._ChannelStripController__main_display_controller.set_show_parameter_names(True)
            self._ChannelStripController__set_plugin_mode(PCM_DEVICES)
        else:
            if mode == CSM_SENDS:
                self._ChannelStripController__main_display_controller.set_show_parameter_names(True)
                self._ChannelStripController__assignment_mode = mode
            else:
                if mode == CSM_IO:
                    for s in self._ChannelStripController__channel_strips:
                        s.unlight_vpot_leds()

                else:
                    self._ChannelStripController__main_display_controller.set_show_parameter_names(False)
                    if self._ChannelStripController__assignment_mode != mode:
                        self._ChannelStripController__assignment_mode = mode
                    else:
                        if self._ChannelStripController__assignment_mode == CSM_IO:
                            self._ChannelStripController__switch_to_next_io_mode()
        self._ChannelStripController__update_assignment_mode_leds()
        self._ChannelStripController__update_assignment_display()
        self._ChannelStripController__apply_meter_mode()
        self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
        self._ChannelStripController__update_channel_strip_strings()
        self._ChannelStripController__update_page_switch_leds()
        if mode == CSM_PLUGINS:
            self._ChannelStripController__update_vpot_leds_in_plugins_device_choose_mode()
        self._ChannelStripController__update_flip_led()
        self.request_rebuild_midi_map()

    def __set_plugin_mode(self, new_mode):
        if self._ChannelStripController__plugin_mode != new_mode:
            self._ChannelStripController__plugin_mode = new_mode
            self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
            self.request_rebuild_midi_map()
            if self._ChannelStripController__plugin_mode == PCM_DEVICES:
                self._ChannelStripController__update_vpot_leds_in_plugins_device_choose_mode()
            else:
                for plugin in self._ChannelStripController__displayed_plugins:
                    if plugin != None:
                        plugin.remove_name_listener(self._ChannelStripController__update_plugin_names)

                self._ChannelStripController__displayed_plugins = []
            self._ChannelStripController__update_page_switch_leds()
            self._ChannelStripController__update_flip_led()
            self._ChannelStripController__update_page_switch_leds()

    def __switch_to_prev_page(self):
        if self._ChannelStripController__can_switch_to_prev_page():
            if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
                self._ChannelStripController__plugin_mode_offsets[self._ChannelStripController__plugin_mode] -= len(self._ChannelStripController__channel_strips)
            else:
                if self._ChannelStripController__assignment_mode == CSM_SENDS:
                    self._ChannelStripController__send_mode_offset -= len(self._ChannelStripController__channel_strips)
            self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
            self._ChannelStripController__update_channel_strip_strings()
            self._ChannelStripController__update_page_switch_leds()
            self.request_rebuild_midi_map()

    def __switch_to_next_page(self):
        if self._ChannelStripController__can_switch_to_next_page():
            if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
                self._ChannelStripController__plugin_mode_offsets[self._ChannelStripController__plugin_mode] += len(self._ChannelStripController__channel_strips)
            else:
                if self._ChannelStripController__assignment_mode == CSM_SENDS:
                    self._ChannelStripController__send_mode_offset += len(self._ChannelStripController__channel_strips)
                else:
                    self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
                    self._ChannelStripController__update_channel_strip_strings()
                    self._ChannelStripController__update_page_switch_leds()
                    self.request_rebuild_midi_map()

    def __switch_to_next_io_mode(self):
        self._ChannelStripController__sub_mode_in_io_mode += 1
        if self._ChannelStripController__sub_mode_in_io_mode > CSM_IO_LAST_MODE:
            self._ChannelStripController__sub_mode_in_io_mode = CSM_IO_FIRST_MODE

    def __reassign_channel_strip_offsets(self):
        for s in self._ChannelStripController__channel_strips:
            s.set_bank_and_channel_offset(self._ChannelStripController__strip_offset(), self._ChannelStripController__view_returns, self._ChannelStripController__within_track_added_or_deleted)

    def __reassign_channel_strip_parameters(self, for_display_only):
        display_parameters = []
        for s in self._ChannelStripController__channel_strips:
            vpot_param = (None, None)
            slider_param = (None, None)
            vpot_display_mode = VPOT_DISPLAY_SINGLE_DOT
            slider_display_mode = VPOT_DISPLAY_SINGLE_DOT
            if self._ChannelStripController__assignment_mode == CSM_VOLPAN:
                if s.assigned_track():
                    if s.assigned_track().has_audio_output:
                        vpot_param = (
                         s.assigned_track().mixer_device.panning, "Pan")
                        vpot_display_mode = VPOT_DISPLAY_BOOST_CUT
                        slider_param = (
                         s.assigned_track().mixer_device.volume, "Volume")
                        slider_display_mode = VPOT_DISPLAY_WRAP
                elif self._ChannelStripController__assignment_mode == CSM_PLUGINS:
                    vpot_param = self._ChannelStripController__plugin_parameter(s.strip_index(), s.stack_offset())
                    vpot_display_mode = VPOT_DISPLAY_WRAP
                    if s.assigned_track():
                        if s.assigned_track().has_audio_output:
                            slider_param = (
                             s.assigned_track().mixer_device.volume, "Volume")
                            slider_display_mode = VPOT_DISPLAY_WRAP
                elif self._ChannelStripController__assignment_mode == CSM_SENDS:
                    vpot_param = self._ChannelStripController__send_parameter(s.strip_index(), s.stack_offset())
                    vpot_display_mode = VPOT_DISPLAY_WRAP
                    if s.assigned_track():
                        if s.assigned_track().has_audio_output:
                            slider_param = (
                             s.assigned_track().mixer_device.volume, "Volume")
                            slider_display_mode = VPOT_DISPLAY_WRAP
                else:
                    if self._ChannelStripController__assignment_mode == CSM_IO:
                        if s.assigned_track():
                            if s.assigned_track().has_audio_output:
                                slider_param = (
                                 s.assigned_track().mixer_device.volume, "Volume")
                    if self._ChannelStripController__flip and self._ChannelStripController__can_flip():
                        if self._ChannelStripController__any_slider_is_touched():
                            display_parameters.append(vpot_param)
                        else:
                            display_parameters.append(slider_param)
                        if not for_display_only:
                            s.set_v_pot_parameter(slider_param[0], slider_display_mode)
                            s.set_fader_parameter(vpot_param[0])
            else:
                if self._ChannelStripController__any_slider_is_touched():
                    display_parameters.append(slider_param)
                else:
                    display_parameters.append(vpot_param)
                for_display_only or s.set_v_pot_parameter(vpot_param[0], vpot_display_mode)
                s.set_fader_parameter(slider_param[0])

        self._ChannelStripController__main_display_controller.set_channel_offset(self._ChannelStripController__strip_offset())
        if len(display_parameters):
            self._ChannelStripController__main_display_controller.set_parameters(display_parameters)
        if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
            if self._ChannelStripController__plugin_mode == PCM_DEVICES:
                self._ChannelStripController__update_vpot_leds_in_plugins_device_choose_mode()

    def _need_to_update_meter(self, meter_state_changed):
        return meter_state_changed and self._ChannelStripController__assignment_mode == CSM_VOLPAN

    def __apply_meter_mode(self, meter_state_changed=False):
        enabled = self._ChannelStripController__meters_enabled and self._ChannelStripController__assignment_mode is CSM_VOLPAN
        send_meter_mode = self._last_assignment_mode != self._ChannelStripController__assignment_mode or self._need_to_update_meter(meter_state_changed)
        for s in self._ChannelStripController__channel_strips:
            s.enable_meter_mode(enabled, needs_to_send_meter_mode=send_meter_mode)

        self._ChannelStripController__main_display_controller.enable_meters(enabled)
        self._last_assignment_mode = self._ChannelStripController__assignment_mode

    def __toggle_flip(self):
        if self._ChannelStripController__can_flip():
            self._ChannelStripController__flip = not self._ChannelStripController__flip
            self._ChannelStripController__on_flip_changed()

    def __toggle_view_returns(self):
        self._ChannelStripController__view_returns = not self._ChannelStripController__view_returns
        self._ChannelStripController__update_view_returns_mode()

    def __update_assignment_mode_leds(self):
        if self._ChannelStripController__assignment_mode == CSM_IO:
            sid_on_switch = SID_ASSIGNMENT_IO
        else:
            if self._ChannelStripController__assignment_mode == CSM_SENDS:
                sid_on_switch = SID_ASSIGNMENT_SENDS
            else:
                if self._ChannelStripController__assignment_mode == CSM_VOLPAN:
                    sid_on_switch = SID_ASSIGNMENT_PAN
                else:
                    if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
                        sid_on_switch = SID_ASSIGNMENT_PLUG_INS
                    else:
                        sid_on_switch = None
        for s in (
         SID_ASSIGNMENT_IO,
         SID_ASSIGNMENT_SENDS,
         SID_ASSIGNMENT_PAN,
         SID_ASSIGNMENT_PLUG_INS):
            if s == sid_on_switch:
                self.send_midi((NOTE_ON_STATUS, s, BUTTON_STATE_ON))
            else:
                self.send_midi((NOTE_ON_STATUS, s, BUTTON_STATE_OFF))

    def __update_assignment_display(self):
        ass_string = [
         " ", " "]
        if self._ChannelStripController__assignment_mode == CSM_VOLPAN:
            ass_string = [
             "P", "N"]
        else:
            if self._ChannelStripController__assignment_mode == CSM_PLUGINS or self._ChannelStripController__assignment_mode == CSM_SENDS:
                if self._ChannelStripController__last_attached_selected_track == self.song().master_track:
                    ass_string = [
                     "M", "A"]
                for t in self.song().return_tracks:
                    if t == self._ChannelStripController__last_attached_selected_track:
                        ass_string = ["R",
                         chr(ord("A") + list(self.song().return_tracks).index(t))]
                        break

                for t in self.song().visible_tracks:
                    if t == self._ChannelStripController__last_attached_selected_track:
                        ass_string = list("%.2d" % min(99, list(self.song().visible_tracks).index(t) + 1))
                        break

            else:
                if self._ChannelStripController__assignment_mode == CSM_IO:
                    if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_INPUT_MAIN:
                        ass_string = [
                         "I", "'"]
                    else:
                        if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_INPUT_SUB:
                            ass_string = [
                             "I", ","]
                        else:
                            if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_OUTPUT_MAIN:
                                ass_string = [
                                 "0", "'"]
                            else:
                                if self._ChannelStripController__sub_mode_in_io_mode == CSM_IO_MODE_OUTPUT_SUB:
                                    ass_string = [
                                     "0", ","]
                                else:
                                    pass
                else:
                    self.send_midi((CC_STATUS, 75, g7_seg_led_conv_table[ass_string[0]]))
                    self.send_midi((CC_STATUS, 74, g7_seg_led_conv_table[ass_string[1]]))

    def __update_rude_solo_led(self):
        any_track_soloed = False
        for t in chain(self.song().tracks, self.song().return_tracks):
            if t.solo:
                any_track_soloed = True
                break

        if any_track_soloed:
            self.send_midi((NOTE_ON_STATUS, SELECT_RUDE_SOLO, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SELECT_RUDE_SOLO, BUTTON_STATE_OFF))

    def __update_page_switch_leds(self):
        if self._ChannelStripController__can_switch_to_prev_page():
            self.send_midi((NOTE_ON_STATUS, SID_ASSIGNMENT_EQ, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_ASSIGNMENT_EQ, BUTTON_STATE_OFF))
        if self._ChannelStripController__can_switch_to_next_page():
            self.send_midi((NOTE_ON_STATUS, SID_ASSIGNMENT_DYNAMIC, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_ASSIGNMENT_DYNAMIC, BUTTON_STATE_OFF))

    def __update_flip_led(self):
        if self._ChannelStripController__flip and self._ChannelStripController__can_flip():
            self.send_midi((NOTE_ON_STATUS, SID_FADERBANK_FLIP, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_FADERBANK_FLIP, BUTTON_STATE_OFF))

    def __update_vpot_leds_in_plugins_device_choose_mode(self):
        sel_track = self.song().view.selected_track
        count = 0
        for s in self._ChannelStripController__channel_strips:
            offset = self._ChannelStripController__plugin_mode_offsets[self._ChannelStripController__plugin_mode]
            if sel_track and offset + count >= 0 and offset + count < len(sel_track.devices):
                s.show_full_enlighted_poti()
            else:
                s.unlight_vpot_leds()
            count += 1

    def __update_channel_strip_strings(self):
        if (self._ChannelStripController__any_slider_is_touched() or self._ChannelStripController__assignment_mode) == CSM_IO:
            targets = []
            for s in self._ChannelStripController__channel_strips:
                if self._ChannelStripController__routing_target(s):
                    targets.append(self._ChannelStripController__routing_target(s))
                else:
                    targets.append("")

            self._ChannelStripController__main_display_controller.set_channel_strip_strings(targets)
        else:
            if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
                if self._ChannelStripController__plugin_mode == PCM_DEVICES:
                    for plugin in self._ChannelStripController__displayed_plugins:
                        if plugin != None:
                            plugin.remove_name_listener(self._ChannelStripController__update_plugin_names)

                    self._ChannelStripController__displayed_plugins = []
                    sel_track = self.song().view.selected_track
                    for i in range(len(self._ChannelStripController__channel_strips)):
                        device_index = i + self._ChannelStripController__plugin_mode_offsets[PCM_DEVICES]
                        if device_index >= 0 and device_index < len(sel_track.devices):
                            sel_track.devices[device_index].add_name_listener(self._ChannelStripController__update_plugin_names)
                            self._ChannelStripController__displayed_plugins.append(sel_track.devices[device_index])
                        else:
                            self._ChannelStripController__displayed_plugins.append(None)

                    self._ChannelStripController__update_plugin_names()

    def __update_plugin_names(self):
        device_strings = []
        for plugin in self._ChannelStripController__displayed_plugins:
            if plugin != None:
                device_strings.append(plugin.name)
            else:
                device_strings.append("")

        self._ChannelStripController__main_display_controller.set_channel_strip_strings(device_strings)

    def __update_view_returns_mode(self):
        if self._ChannelStripController__view_returns:
            self.send_midi((NOTE_ON_STATUS, SID_FADERBANK_EDIT, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_FADERBANK_EDIT, BUTTON_STATE_OFF))
        self._ChannelStripController__main_display_controller.set_show_return_track_names(self._ChannelStripController__view_returns)
        self._ChannelStripController__reassign_channel_strip_offsets()
        self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
        self.request_rebuild_midi_map()

    def __on_selected_track_changed(self):
        st = self._ChannelStripController__last_attached_selected_track
        if st:
            if st.devices_has_listener(self._ChannelStripController__on_selected_device_chain_changed):
                st.remove_devices_listener(self._ChannelStripController__on_selected_device_chain_changed)
        else:
            self._ChannelStripController__last_attached_selected_track = self.song().view.selected_track
            st = self._ChannelStripController__last_attached_selected_track
            if st:
                st.add_devices_listener(self._ChannelStripController__on_selected_device_chain_changed)
            if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
                self._ChannelStripController__plugin_mode_offsets = [0 for x in range(PCM_NUMMODES)]
                if self._ChannelStripController__chosen_plugin != None:
                    self._ChannelStripController__chosen_plugin.remove_parameters_listener(self._ChannelStripController__on_parameter_list_of_chosen_plugin_changed)
                self._ChannelStripController__chosen_plugin = None
                self._ChannelStripController__ordered_plugin_parameters = []
                self._ChannelStripController__update_assignment_display()
                if self._ChannelStripController__plugin_mode == PCM_DEVICES:
                    self._ChannelStripController__update_vpot_leds_in_plugins_device_choose_mode()
                else:
                    self._ChannelStripController__set_plugin_mode(PCM_DEVICES)
            elif self._ChannelStripController__assignment_mode == CSM_SENDS:
                self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
                self._ChannelStripController__update_assignment_display()
                self.request_rebuild_midi_map()

    def __on_flip_changed(self):
        self._ChannelStripController__update_flip_led()
        if self._ChannelStripController__can_flip():
            self._ChannelStripController__update_assignment_display()
            self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
            self.request_rebuild_midi_map()

    def __on_selected_device_chain_changed(self):
        if self._ChannelStripController__assignment_mode == CSM_PLUGINS:
            if self._ChannelStripController__plugin_mode == PCM_DEVICES:
                self._ChannelStripController__update_vpot_leds_in_plugins_device_choose_mode()
                self._ChannelStripController__update_page_switch_leds()
            else:
                if self._ChannelStripController__plugin_mode == PCM_PARAMETERS:
                    if not self._ChannelStripController__chosen_plugin:
                        self._ChannelStripController__set_plugin_mode(PCM_DEVICES)
                    else:
                        if self._ChannelStripController__chosen_plugin not in self._ChannelStripController__last_attached_selected_track.devices:
                            if self._ChannelStripController__chosen_plugin != None:
                                self._ChannelStripController__chosen_plugin.remove_parameters_listener(self._ChannelStripController__on_parameter_list_of_chosen_plugin_changed)
                            self._ChannelStripController__chosen_plugin = None
                            self._ChannelStripController__set_plugin_mode(PCM_DEVICES)

    def __on_tracks_added_or_deleted(self):
        self._ChannelStripController__within_track_added_or_deleted = True
        for t in chain(self.song().visible_tracks, self.song().return_tracks):
            if not t.solo_has_listener(self._ChannelStripController__update_rude_solo_led):
                t.add_solo_listener(self._ChannelStripController__update_rude_solo_led)
            if not t.has_audio_output_has_listener(self._ChannelStripController__on_any_tracks_output_type_changed):
                t.add_has_audio_output_listener(self._ChannelStripController__on_any_tracks_output_type_changed)

        if self._ChannelStripController__send_mode_offset >= len(self.song().return_tracks):
            self._ChannelStripController__send_mode_offset = 0
            self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
            self._ChannelStripController__update_channel_strip_strings()
        if self._ChannelStripController__strip_offset() + len(self._ChannelStripController__channel_strips) >= self._ChannelStripController__controlled_num_of_tracks():
            self._ChannelStripController__set_channel_offset(max(0, self._ChannelStripController__controlled_num_of_tracks() - len(self._ChannelStripController__channel_strips)))
        self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
        self._ChannelStripController__update_channel_strip_strings()
        if self._ChannelStripController__assignment_mode == CSM_SENDS:
            self._ChannelStripController__update_page_switch_leds()
        self.refresh_state()
        self._ChannelStripController__main_display_controller.refresh_state()
        self._ChannelStripController__within_track_added_or_deleted = False
        self.request_rebuild_midi_map()

    def __on_any_tracks_output_type_changed(self):
        self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
        self.request_rebuild_midi_map()

    def __on_parameter_list_of_chosen_plugin_changed(self):
        self._ChannelStripController__reorder_parameters()
        self._ChannelStripController__reassign_channel_strip_parameters(for_display_only=False)
        self.request_rebuild_midi_map()

    def __reorder_parameters(self):
        result = []
        if self._ChannelStripController__chosen_plugin:
            result = [(p, p.name) for p in self._ChannelStripController__chosen_plugin.parameters[1[:None]]]
        else:
            self._ChannelStripController__ordered_plugin_parameters = result
