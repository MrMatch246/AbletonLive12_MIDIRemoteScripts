# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MPD24\config.py
# Size of source mod 2**32: 4860 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {
  'STOP': GENERIC_STOP,
  'PLAY': GENERIC_PLAY,
  'REC': GENERIC_REC,
  'LOOP': GENERIC_LOOP,
  'RWD': GENERIC_RWD,
  'FFWD': GENERIC_FFWD,
  'NORELEASE': 0}
DEVICE_CONTROLS = GENERIC_ENCODERS
VOLUME_CONTROLS = (
 (
  GENERIC_SLI1, -1),
 (
  GENERIC_SLI2, -1),
 (
  GENERIC_SLI3, -1),
 (
  GENERIC_SLI4, -1),
 (
  GENERIC_SLI5, -1),
 (
  GENERIC_SLI6, -1),
 (
  GENERIC_SLI7, -1),
 (
  GENERIC_SLI8, -1))
TRACKARM_CONTROLS = (
 GENERIC_BUT1,
 GENERIC_BUT2,
 GENERIC_BUT3,
 GENERIC_BUT4,
 GENERIC_BUT5,
 GENERIC_BUT6,
 GENERIC_BUT7,
 GENERIC_BUT8)
BANK_CONTROLS = {
  'TOGGLELOCK': -1,
  'BANKDIAL': -1,
  'NEXTBANK': -1,
  'PREVBANK': -1,
  'BANK1': -1,
  'BANK2': -1,
  'BANK3': -1,
  'BANK4': -1,
  'BANK5': -1,
  'BANK6': -1,
  'BANK7': -1,
  'BANK8': -1}
PAD_TRANSLATION = ((0, 0, 48, 0), (1, 0, 49, 0), (2, 0, 50, 0), (3, 0, 51, 0), (0, 1, 44, 0),
                   (1, 1, 45, 0), (2, 1, 46, 0), (3, 1, 47, 0), (0, 2, 40, 0), (1, 2, 41, 0),
                   (2, 2, 42, 0), (3, 2, 43, 0), (0, 3, 36, 0), (1, 3, 37, 0), (2, 3, 38, 0),
                   (3, 3, 39, 0))
CONTROLLER_DESCRIPTION = {
  'INPUTPORT': "Akai MPD24",
  'OUTPUTPORT': "Akai MPD24",
  'CHANNEL': 0,
  'PAD_TRANSLATION': PAD_TRANSLATION}
MIXER_OPTIONS = {
  'NUMSENDS': 2,
  'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1),
  'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1),
  'MASTERVOLUME': -1}

# okay decompiling ./MIDIRemoteScripts/MPD24/config.pyc
