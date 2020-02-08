#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
fixtures for tests
"""

import pytest
import utils
from selenium.webdriver import Chrome, Firefox, Ie
from page_methods import LoginPageMethods, HomePageMethods


@pytest.fixture(scope='function')
def driver(request, get_browser):
    driver = get_browser
    request.cls.driver = driver  # allows tests to access the driver
    driver.get(f'{utils.cfg["hudl_url"]}{utils.cfg["hudl_login"]}')
    driver.maximize_window()
    yield driver
    driver.quit()  # tear down browser after test


@pytest.fixture()
def get_browser():
    dvr_path = utils.cfg["driver_dir_path"]
    brswr = utils.cfg['browser']
    if brswr == 'chrome':
        yield Chrome(f'{dvr_path}chromedriver.exe')
    elif brswr == 'firefox':
        yield Firefox(f'{dvr_path}geckodriver.exe')
    elif brswr == 'ie':
        yield Ie(f'{dvr_path}IEDriverServer.exe')
    else:
        pytest.exit('browser not found')


@pytest.fixture(scope='function')
def login_page(driver):
    yield LoginPageMethods(driver)


@pytest.fixture(scope='function')
def home_page(driver):
    yield HomePageMethods(driver)
