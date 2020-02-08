#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
set of utility functions for use in other modules
"""

import json
import os

cfg = None  # config options


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def load_config(file_path):
    global cfg
    with open(file_path) as cfg_file:
        data = json.load(cfg_file)
    cfg = data
