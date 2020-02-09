#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
set of utility functions for use in other modules
"""

import json
import os
from datetime import datetime

cfg = None  # config options


def create_dir(dir_path):
    """ creates specified directory if it doesn't already exist """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        add_log_entry(f'created directory: {dir_path}')
    return dir_path


def load_config(file_path):
    """ initialises config and stores in global variable 'cfg' """
    global cfg
    with open(file_path) as cfg_file:
        data = json.load(cfg_file)
    cfg = data


def add_log_entry(log_text):
    """ simple function for logging test automation information """
    log_file_path = f'{cfg["output_path"]}{cfg["log_name"]}'
    time_string = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{time_string}: {log_text} \n')
