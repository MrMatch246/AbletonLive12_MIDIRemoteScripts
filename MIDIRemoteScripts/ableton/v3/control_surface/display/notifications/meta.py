# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\display\notifications\meta.py
# Size of source mod 2**32: 2425 bytes
from __future__ import absolute_import, annotations, print_function, unicode_literals
from inspect import getmro
from typing import Callable
from .type_decl import Notification, _DefaultText, _TransformDefaultText

def transform_notification(default: "Notification", transform_fn: "Callable[[str], str]"):
    if not callable(default):
        return transform_fn(default)

    def notification_fn(*a, **k):
        return transform_fn(default(*a, **k))

    return notification_fn


def update_special_attributes(cls, exclude_by_default=True):
    base_class = getmro(cls)[-2]
    for (name, value) in vars(base_class).items():
        subclass_value = vars(cls).get(name, None)
        if subclass_value is None:
            if isinstance(value, type):
                subclass_value = type(name, (value,), {})
                setattr(cls, name, subclass_value)
            if isinstance(subclass_value, type):
                include_all = getattr(subclass_value, "INCLUDE_ALL", False)
                update_special_attributes(subclass_value, False if include_all else exclude_by_default)
            if not name.startswith("__"):
                if exclude_by_default:
                    if subclass_value is None:
                        setattr(cls, name, None)
        if not not subclass_value is None:
            if isinstance(subclass_value, _DefaultText):
                setattr(cls, name, getattr(base_class, name))
            else:
                if isinstance(subclass_value, _TransformDefaultText):
                    setattr(cls, name, transform_notification(getattr(base_class, name), subclass_value.transform_fn))


class DefaultNotificationsMeta(type):

    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        update_special_attributes(new_cls)
        return new_cls

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/display/notifications/meta.pyc
