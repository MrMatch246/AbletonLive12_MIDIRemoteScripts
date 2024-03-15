# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\components\device.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 12300 bytes

-- Stacks of completed symbols:
START ::= |- stmts . 
_ifstmts_jump ::= \e_c_stmts_opt . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . ELSE
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD \e__come_froms
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_ABSOLUTE JUMP_FORWARD _come_froms
_ifstmts_jump ::= \e_c_stmts_opt . come_froms
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
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg CALL_METHOD_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr . pos_arg pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . CALL_METHOD_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg . pos_arg pos_arg pos_arg pos_arg CALL_FUNCTION_5
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . pos_arg pos_arg pos_arg CALL_FUNCTION_5
call_stmt ::= expr . POP_TOP
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
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= compare . 
expr ::= list . 
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
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
ifelsestmtr ::= testexpr . return_if_stmts returns
ifstmt ::= testexpr . _ifstmts_jump
ifstmtl ::= testexpr . _ifstmts_jumpl
jitop_come_from_expr ::= JUMP_IF_TRUE_OR_POP . come_froms expr
jmp_false ::= POP_JUMP_IF_FALSE . 
list ::= expr . expr BUILD_LIST_2
list ::= expr expr . BUILD_LIST_2
list ::= expr expr BUILD_LIST_2 . 
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= and . jitop_come_from_expr COME_FROM
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
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
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
testfalse_not_and ::= and . jmp_true come_froms
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false . expr jmp_true COME_FROM
testfalse_not_and ::= expr jmp_false expr . jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false . expr jmp_false COME_FROM
testfalse_not_or ::= expr jmp_false expr . jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
   
 L.  60         2  LOAD_GLOBAL              legacy_bank_definitions
                   4  LOAD_METHOD              banked
                   6  CALL_METHOD_0         0  '0 positional arguments'
                   8  LOAD_GLOBAL              legacy_bank_definitions
                  10  LOAD_METHOD              best_of_banks
                  12  CALL_METHOD_0         0  '0 positional arguments'
                  14  BUILD_LIST_2          2 
                  16  COMPARE_OP               not-in
                  18  POP_JUMP_IF_FALSE    30  'to 30'
                  20  LOAD_FAST                'device_decorator_factory'
                  22  JUMP_IF_TRUE_OR_POP    32  'to 32'
                  24  LOAD_GLOBAL              DeviceDecoratorFactory
                  26  CALL_FUNCTION_0       0  '0 positional arguments'
->                28  RETURN_VALUE     
                30_0  COME_FROM            18  '18'
from __future__ import absolute_import, print_function, unicode_literals
from typing import cast
from ableton.v2.control_surface.simpler_slice_nudging import SimplerSliceNudging
from ...base import depends, find_if, listenable_property, listens
from ...live import deduplicate_parameters, liveobj_changed, liveobj_valid
from .. import DEFAULT_BANK_SIZE, BankingInfo, Component, ParameterProvider, create_parameter_bank, legacy_bank_definitions
from ..controls import MappedButtonControl, ToggleButtonControl
from ..default_bank_definitions import BANK_DEFINITIONS
from ..device_decorators import DeviceDecoratorFactory
from ..display import Renderable
from ..parameter_info import ParameterInfo
from ..parameter_mapping_sensitivities import DEFAULT_CONTINUOUS_PARAMETER_SENSITIVITY, DEFAULT_QUANTIZED_PARAMETER_SENSITIVITY, parameter_mapping_sensitivities
from .device_bank_navigation import DeviceBankNavigationComponent
from .device_parameters import DeviceParametersComponent

def get_on_off_parameter(device):
    if liveobj_valid(device):
        return find_if((lambda p: p.original_name.startswith("Device On") and liveobj_valid(p) and p.is_enabled), device.parameters)


def create_device_decorator_factoryParse error at or near `RETURN_VALUE' instruction at offset 28


class DeviceComponent(ParameterProvider, Component, Renderable):
    device_on_off_button = MappedButtonControl(color="Device.Off", on_color="Device.On")
    device_lock_button = ToggleButtonControl(color="Device.LockOff",
      on_color="Device.LockOn")

    @depends(device_provider=None,
      device_bank_registry=None,
      toggle_lock=None,
      show_message=None)
    def __init__(self, name="Device", continuous_parameter_sensitivity=DEFAULT_CONTINUOUS_PARAMETER_SENSITIVITY, quantized_parameter_sensitivity=DEFAULT_QUANTIZED_PARAMETER_SENSITIVITY, parameters_component_type=None, bank_size=DEFAULT_BANK_SIZE, bank_definitions=None, bank_navigation_component_type=None, device_provider=None, device_bank_registry=None, device_decorator_factory=None, toggle_lock=None, show_message=None, *a, **k):
        self._decorated_device = None
        self._provided_parameters = []
        self._device_provider = device_provider
        self._device_bank_registry = device_bank_registry
        self._decorator_factory = create_device_decorator_factory(device_decorator_factory, bank_definitions)
        self._parameter_mapping_sensitivities = parameter_mapping_sensitivities(continuous_parameter_sensitivity=continuous_parameter_sensitivity,
          quantized_parameter_sensitivity=quantized_parameter_sensitivity)
        parameters_component_type = parameters_component_type or DeviceParametersComponent
        self._parameters_component = parameters_component_type
        self._parameters_component.parameter_provider = self
        self._bank = None
        self._banking_info = BankingInfo((bank_definitions or BANK_DEFINITIONS),
          bank_size=bank_size)
        bank_navigation_component_type = bank_navigation_component_type or DeviceBankNavigationComponent
        self._bank_navigation_component = bank_navigation_component_type(banking_info=(self._banking_info),
          device_bank_registry=device_bank_registry)
        (super.__init__)(a, name=name, **k)
        self._toggle_lock = toggle_lock
        self._show_message = show_message
        self._slice_nudging = self.register_disconnectable(SimplerSliceNudging)
        self.add_children(self._parameters_component, self._bank_navigation_component)
        self._DeviceComponent__on_provided_device_changed.subject = device_provider
        self._DeviceComponent__on_provided_device_changed
        self.register_slot(self._device_provider, self._update_device_lock_button, "is_locked_to_device")
        self._update_device_lock_button

    @property
    def parameters(self):
        return self._provided_parameters

    @listenable_property
    def device(self):
        return self._decorated_device

    @device.setter
    def device(self, device):
        self._device_provider.device = device

    @listenable_property
    def bank_name(self):
        if self.device:
            return self._current_bank_details[0]
        return ""

    def set_parameter_controls(self, controls):
        self._parameters_component.set_parameter_controls(controls)
        self._show_device_and_bank_info

    def __getattr__(self, name):
        if name.startswith("set_"):
            if "bank" in name:
                return getattr(self._bank_navigation_component, name)
        raise AttributeError

    @device_lock_button.toggled
    def device_lock_button(self, *_):
        self._toggle_lock
        if liveobj_valid(self.device):
            self.notify(self.notifications.Device.lock, cast(str, self.device.name), self._device_provider.is_locked_to_device)

    def _create_parameter_info(self, parameter, name):
        default, fine_grain = self._parameter_mapping_sensitivities(parameter, self.device)
        return ParameterInfo(parameter=parameter,
          name=name,
          default_encoder_sensitivity=default,
          fine_grain_encoder_sensitivity=fine_grain)

    def _set_device(self, device):
        self._set_decorated_device(self._get_decorated_device(device))
        device_bank_registry = self._device_bank_registry
        self._DeviceComponent__on_bank_changed.subject = device_bank_registry
        self._set_bank_index(device_bank_registry.get_device_bank(device))
        self._update_parameters
        self._DeviceComponent__on_parameters_changed_in_device.subject = device
        self.device_on_off_button.mapped_parameter = get_on_off_parameter(device)
        self.notify_device
        self.notify_bank_name

    def _get_decorated_device(self, device):
        if self._decorator_factory is not None:
            return self._decorator_factory.decorate(device)
        return device

    def _set_decorated_device(self, decorated_device):
        self._decorated_device = decorated_device
        self._slice_nudging.set_device(decorated_device)
        self._setup_bank(decorated_device)
        self._DeviceComponent__on_bank_parameters_changed.subject = self._bank

    def _on_device_changed(self, device):
        current_device = getattr(self.device, "_live_object", self.device)
        if liveobj_changed(current_device, device):
            self._set_device(device)

    def _setup_bank(self, device, bank_factory=create_parameter_bank):
        if self._bank is not None:
            self.disconnect_disconnectable(self._bank)
            self._bank = None
        if liveobj_valid(device):
            self._bank = self.register_disconnectable(bank_factory(device, self._banking_info))
        self._bank_navigation_component.bank_provider = self._bank

    def _set_bank_index(self, bank):
        if self._bank is not None:
            self._bank.index = bank
        if liveobj_valid(self.device):
            self.notify_bank_name
            self._show_device_and_bank_info

    def _current_bank_details(self):
        if self._bank is not None:
            return (self._bank.name, self._bank.parameters)
        return (
         "", [None] * self._parameters_component.controls.control_count)

    def _show_device_and_bank_info(self):
        device = self.device
        if liveobj_valid(device):
            if self._parameters_component.controls[0].control_element:
                self._show_message("Controlling {}: {}".format(device.name, self.bank_name))

    def _get_provided_parameters(self):
        _, parameters = self._current_bank_details if self.device else (None, ())
        return deduplicate_parameters([self._create_parameter_info(param, name) for param, name in parameters])

    def _update_parameters(self):
        self._provided_parameters = self._get_provided_parameters
        self.notify_parameters

    def _update_device_lock_button(self):
        self.device_lock_button.is_on = self._device_provider.is_locked_to_device

    @listens("device")
    def __on_provided_device_changed(self):
        self._on_device_changed(self._device_provider.device)

    @listens("device_bank")
    def __on_bank_changed(self, device, bank):
        if device == self.device:
            self._set_bank_index(bank)

    @listens("parameters")
    def __on_parameters_changed_in_device(self):
        self._update_parameters

    @listens("parameters")
    def __on_bank_parameters_changed(self):
        self._update_parameters
        self._device_bank_registry.set_device_bank(self.device, self._bank.index)
