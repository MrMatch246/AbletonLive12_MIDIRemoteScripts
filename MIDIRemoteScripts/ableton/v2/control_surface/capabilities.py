# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\capabilities.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 2178 bytes
from __future__ import absolute_import, print_function, unicode_literals
from future.utils import string_types
GENERIC_SCRIPT_KEY = "generic_script"
PORTS_KEY = "ports"
CONTROLLER_ID_KEY = "controller_id"
TYPE_KEY = "surface_type"
FIRMWARE_KEY = "firmware_version"
AUTO_LOAD_KEY = "auto_load"
SUGGESTED_PORT_NAMES_KEY = "suggested_port_names"
VENDORID = "vendor_id"
PRODUCTIDS = "product_ids"
MODEL_NAMES = "model_names"
DIRECTIONKEY = "direction"
PORTNAMEKEY = "name"
MACNAMEKEY = "mac_name"
PROPSKEY = "props"
HIDDEN = "hidden"
SYNC = "sync"
SCRIPT = "script"
NOTES_CC = "notes_cc"
REMOTE = "remote"
PLAIN_OLD_MIDI = "plain_old_midi"

def __create_port_dict(direction, port_name, mac_name, props):
    if props:
        for prop in props:
            pass

    capabilities = {DIRECTIONKEY: direction, PORTNAMEKEY: port_name, PROPSKEY: props}
    if mac_name:
        capabilities[MACNAMEKEY] = mac_name
    return capabilities


def inport(port_name="", props=[], mac_name=None):
    return __create_port_dict("in", port_name, mac_name, props)


def outport(port_name="", props=[], mac_name=None):
    return __create_port_dict("out", port_name, mac_name, props)


def controller_id(vendor_id, product_ids, model_name):
    for product_id in product_ids:
        pass

    model_names = model_name if type(model_name) is list else [model_name]
    return {VENDORID: vendor_id, PRODUCTIDS: product_ids, MODEL_NAMES: model_names}

# okay decompiling ./MIDIRemoteScripts/ableton/v2/control_surface/capabilities.pyc