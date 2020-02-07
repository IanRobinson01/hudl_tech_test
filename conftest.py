#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
fixtures for tests
"""

import json
import pytest
from selenium.webdriver import Chrome, Firefox, Ie
from page_methods import LoginPageMethods, HomePageMethods


@pytest.fixture(scope='function')
def driver(request, config):
    driver = None
    if config['browser'] == 'chrome':
        driver = Chrome('drivers/chromedriver.exe')
    elif config['browser'] == 'firefox':
        driver = Firefox('drivers/geckodriver.exe')
    elif config['browser'] == 'ie':
        driver = Ie('drivers/IEDriverServer.exe')
    request.cls.driver = driver  # allows tests to access the driver
    driver.get('https://www.hudl.com/login')
    driver.maximize_window()
    yield driver
    driver.quit()  # tear down browser after test


@pytest.fixture(scope='function')
def login_page(driver):
    yield LoginPageMethods(driver)


@pytest.fixture(scope='function')
def home_page(driver):
    yield HomePageMethods(driver)


@pytest.fixture(scope='session')
def config():
    with open('test_cfg.json') as cfg:
        data = json.load(cfg)
    return data
