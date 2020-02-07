#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
fixtures for tests
"""

import pytest
from selenium.webdriver import Chrome
from page_methods import LoginPageMethods, HomePageMethods


@pytest.fixture()
def driver(request):
    driver = Chrome('drivers/chromedriver.exe')
    request.cls.driver = driver  # allows tests to access the driver
    driver.get('https://www.hudl.com/login')
    driver.maximize_window()
    yield driver
    driver.quit()  # tear down browser after test


@pytest.fixture()
def login_page(driver):
    yield LoginPageMethods(driver)


@pytest.fixture()
def home_page(driver):
    yield HomePageMethods(driver)
