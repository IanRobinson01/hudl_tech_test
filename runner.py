#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
entry point for running tests
"""

import pytest
from utils import create_dir

if __name__ == "__main__":

    create_dir('reports')

    pytest.main(['--junitxml=reports/test_report.xml', '-v'])
