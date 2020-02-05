#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import pytest

if __name__ == "__main__":

    pytest.main(['--junitxml=reports/test_report.xml', '-v', '-k'])