#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
set of utility functions for use in other modules
"""

import os


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
