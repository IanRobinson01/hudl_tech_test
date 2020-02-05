#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
fixtures for tests
"""

import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='module')
def browser():
    driver = Chrome('drivers/chromedriver.exe')
    driver.get('https://www.bbc.co.uk/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver  # the browser object created for the test
    driver.quit()  # tear down browser after test
