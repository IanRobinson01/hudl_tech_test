#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
entry point for running tests
"""

import pytest
import utils
from utils import create_dir, load_config, add_log_entry

config_file_name = 'test_cfg.json'

if __name__ == "__main__":


    # initialise configuration
    load_config(config_file_name)

    # create report directory and report name
    output_dir = create_dir(utils.cfg['output_path'])
    report_name = utils.cfg['report_name']

    # execute tests
    add_log_entry('starting tests')
    pytest.main([f'--junitxml={output_dir}{report_name}', '-v'])
    add_log_entry('testing finished')
