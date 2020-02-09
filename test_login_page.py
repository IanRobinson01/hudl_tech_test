#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
the set of tests to be executed for the login page
"""
import pytest
from utils import add_log_entry, cfg


@pytest.mark.usefixtures('driver')
class TestLoginPage:

    @pytest.mark.parametrize('entry_method', ['button', 'return_key'])
    def test_successful_login(self, login_page, home_page, entry_method):
        add_log_entry(f'testing {TestLoginPage.test_successful_login.__name__} '
                      f'with parameters: {entry_method}')
        login_page.enter_email('ianrobinson01@hotmail.com')
        login_page.enter_password('7784ian')
        login_page.login(entry_method)
        assert home_page.get_home_text()  # checks that the word 'home' appears in the nav bar
        assert self.driver.current_url == f'{cfg["hudl_url"]}{cfg["hudl_home"]}'

    @pytest.mark.parametrize('email, password', [
        ('ianrobinson01@hotmail.com', '1234567'),  # correct email and incorrect password
        ('x@x.com', '7784ian'),  # incorrect email and correct password
        ('x@x.com', '1234567'),  # incorrect email and incorrect password
        ('', ''),  # empty email and password
    ])
    def test_unsuccessful_login(self, login_page, email, password):
        add_log_entry(f'testing {TestLoginPage.test_successful_login.__name__} '
                      f'with parameters: {email} and {password}')
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.login('button')
        assert login_page.get_error_text() == \
            "We didn't recognize that email and/or password. Need help?"
        assert self.driver.current_url == f'{cfg["hudl_url"]}{cfg["hudl_login"]}'

    #@pytest.mark.skip('skipped')
    def test_remember_me(self, login_page, home_page):
        add_log_entry(f'testing {TestLoginPage.test_remember_me.__name__}')
        # login as normal and click remember me
        login_page.enter_email('ianrobinson01@hotmail.com')
        login_page.enter_password('7784ian')
        login_page.click_remember_me()
        login_page.login('button')
        home_page.get_home_text()
        # delete all cookies that have an expiry parameter
        # simulates closing the browser
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if 'expiry' in cookie:
                self.driver.delete_cookie(cookie['name'])
        # navigate to login page.  Should re-direct to home because remember me is checked
        self.driver.get(f'{cfg["hudl_url"]}{cfg["hudl_login"]}')
        assert home_page.get_home_text()
        assert self.driver.current_url == f'{cfg["hudl_url"]}{cfg["hudl_home"]}'
