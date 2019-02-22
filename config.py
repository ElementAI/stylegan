# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
"""Global configuration."""
import os

#----------------------------------------------------------------------------
# Paths.

trial_id = os.environ.get("SHK_TRIAL_ID")
result_dir = os.path.join('/results', trial_id)
exist = False
if not os.path.exists():
    os.makedirs(result_dir)
else:
    exist = True
data_dir = '/data'
cache_dir = 'cache'
run_dir_ignore = ['/results', '/data', 'cache']

#----------------------------------------------------------------------------
