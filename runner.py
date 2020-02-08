#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
entry point for running tests
"""

import pytest
import utils
from utils import create_dir, load_config

if __name__ == "__main__":

    # initialise configuration
    load_config('test_cfg.json')

    # create report directory and report name
    report_dir = create_dir(utils.cfg['report_dir_path'])
    report_name = utils.cfg['report_name']

    # execute tests
    pytest.main([f'--junitxml={report_dir}{report_name}', '-v'])
