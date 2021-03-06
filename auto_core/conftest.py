#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
set of common fixtures that can be used across test classes
"""

import pytest
from selenium.webdriver import Chrome, Firefox, Ie
from auto_core.page_methods import LoginPageMethods, HomePageMethods
from auto_core.utils import add_log_entry, cfg


@pytest.fixture(scope='function')
def driver(request, get_browser):
    driver = get_browser
    request.cls.driver = driver  # allows tests to access the driver
    driver.get(f'{cfg["hudl_url"]}{cfg["hudl_login"]}')
    driver.maximize_window()
    add_log_entry('web driver object initialised')
    yield driver
    driver.quit()  # tear down browser after test
    add_log_entry('web driver object destroyed')


@pytest.fixture(scope='function')
def get_browser():
    dvr_path = cfg["driver_dir_path"]
    brswr = cfg['browser']
    add_log_entry(f'browser being used: {brswr}')
    if brswr == 'chrome':
        yield Chrome(f'{dvr_path}chromedriver.exe')
    elif brswr == 'firefox':
        yield Firefox(f'{dvr_path}geckodriver.exe')
    elif brswr == 'ie':
        yield Ie(f'{dvr_path}IEDriverServer.exe')
    else:
        add_log_entry(f'browser not found: {brswr}')
        pytest.exit(f'browser not found: {brswr}')


@pytest.fixture(scope='function')
def login_page(driver):
    yield LoginPageMethods(driver)


@pytest.fixture(scope='function')
def home_page(driver):
    yield HomePageMethods(driver)
