#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
defines methods which mimic user interaction
"""

from page_elements import LoginPageElements


class BasePageObject(object):
    def __init__(self, browser):
        self.browser = browser


class LoginPageMethods(BasePageObject):

    pass