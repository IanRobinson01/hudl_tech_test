#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
the set of tests to be executed for the login page
"""

from page_methods import LoginPageMethods


def test_successful_login(browser):
    login_page = LoginPageMethods(browser)
    import time
    time.sleep(5)