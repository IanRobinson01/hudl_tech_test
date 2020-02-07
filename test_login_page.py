#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
the set of tests to be executed for the login page
"""
import pytest


@pytest.mark.usefixtures('driver')
class TestLoginPage:

    def test_successful_login(self, login_page, home_page):
        login_page.enter_email('ianrobinson01@hotmail.com')
        login_page.enter_password('7784ian')
        login_page.click_login()
        assert home_page.get_home_text()  # checks that the word 'home' appears in the nav bar
        assert self.driver.current_url == 'https://www.hudl.com/home'

    @pytest.mark.parametrize('email, password', [
        ('ianrobinson01@hotmail.com', '1234567'),  # correct email and incorrect password
        ('x@x.com', '7784ian'),  # incorrect email and correct password
        ('x@x.com', '1234567'),  # incorrect email and incorrect password
        ('', ''),  # empty email and password
    ])
    def test_unsuccessful_login(self, login_page, email, password):
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()
        assert login_page.get_error_text() == "We didn't recognize that email and/or password. Need help?"
        assert self.driver.current_url == 'https://www.hudl.com/login'

    # def test_remember_me(self, login_page, home_page):
    #     login_page.enter_email('ianrobinson01@hotmail.com')
    #     login_page.enter_password('7784ian')
    #     login_page.click_remember_me()
    #     login_page.click_login()
    #     home_page.get_home_text()
    #     cookies = self.driver.get_cookies()
    #     for cookie in cookies:
    #         if 'expiry' in cookie:
    #             self.driver.delete_cookie(cookie['name'])
    #     self.driver.get('https://www.hudl.com/login')
    #     assert home_page.get_home_text()
    #     assert self.driver.current_url == 'https://www.hudl.com/home'
