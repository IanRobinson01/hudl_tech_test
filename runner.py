#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
entry point for running tests
"""

import pytest
from utils import create_dir, load_config, add_log_entry

CFG_FILE_NAME = 'test_cfg.json'


def execute_test_framework():

    # initialise configuration
    load_config(CFG_FILE_NAME)
    from utils import cfg  # makes cfg available to all other modules

    # create report directory and report name
    output_dir = create_dir(cfg['output_path'])
    report_name = cfg['report_name']

    # execute tests
    add_log_entry('starting tests')
    pytest.main([f'--junitxml={output_dir}{report_name}', '-v'])
    add_log_entry('testing finished')


if __name__ == "__main__":
    execute_test_framework()
