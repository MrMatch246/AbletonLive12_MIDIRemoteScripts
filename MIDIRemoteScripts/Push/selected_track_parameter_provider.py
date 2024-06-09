# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push\selected_track_parameter_provider.py
# Size of source mod 2**32: 921 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import ParameterInfo
from pushbase.selected_track_parameter_provider import SelectedTrackParameterProvider as SelectedTrackParameterProviderBase
from .parameter_mapping_sensitivities import fine_grain_parameter_mapping_sensitivity, parameter_mapping_sensitivity

class SelectedTrackParameterProvider(SelectedTrackParameterProviderBase):

    def _create_parameter_info(self, parameter, name):
        return ParameterInfo(name=name,
          parameter=parameter,
          default_encoder_sensitivity=(parameter_mapping_sensitivity(parameter)),
          fine_grain_encoder_sensitivity=(fine_grain_parameter_mapping_sensitivity(parameter)))

# okay decompiling ./MIDIRemoteScripts/Push/selected_track_parameter_provider.pyc
