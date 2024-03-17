# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\profile.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1775 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial, wraps
ENABLE_PROFILING = False
if ENABLE_PROFILING:
    import cProfile
    PROFILER = cProfile.Profile()

def profile(fn):
    if ENABLE_PROFILING:

        @wraps(fn)
        def wrapper(self, *a, **k):
            if PROFILER:
                return PROFILER.runcall(partial(fn, self, *a, **k))
            print("Can not profile (%s), it is probably reloaded" % fn.__name__)
            return fn(*a, **k)

        return wrapper
    return fn


def dump(name='default'):
    import pstats
    fname = name + ".profile"
    PROFILER.dump_stats(fname)

    def save_human_data(sort):
        s = pstats.Stats(fname, stream=(open("%s.%s.txt" % (fname, sort), "w")))
        s.sort_stats(sort)
        s.print_stats()

    save_human_data("time")
    save_human_data("cumulative")

# okay decompiling ./MIDIRemoteScripts/ableton/v2/control_surface/profile.pyc
