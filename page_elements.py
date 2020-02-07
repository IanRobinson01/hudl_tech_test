#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
identifies all elements that may be interacted with
"""

from selenium.webdriver.common.by import By


class LoginPageElements(object):

    email = (By.ID, 'email')
    password = (By.ID, 'password')
    login = (By.ID, 'logIn')
    remember_me = (By.ID, 'remember-me')
    login_error = (By.CLASS_NAME, 'login-error-container')


class HomePageElements(object):

    home_text = (By.CLASS_NAME, 'hui-globalnav__home')
