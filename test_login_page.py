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
        try:
            home_page.get_home_text()
        except:
            pytest.fail()



    # correct email and password -> confirmed by display of hudl_logo

    # following error scenarios can be grouped into a single test and parameterised
    # correct email and incorrect password -> We didn't recognize that email and/or password. Need help?
    # incorrect email and correct password -> We didn't recognize that email and/or password. Need help?
    # incorrect email and incorrect password -> We didn't recognize that email and/or password. Need help?
    # empty email -> We didn't recognize that email and/or password. Need help?
    # empty password -> We didn't recognize that email and/or password. Need help?

    # remember me login (https://stackoverflow.com/questions/29338944/how-can-i-test-a-remember-me-checkbox-feature-in-selenium)
    # non-remember me login