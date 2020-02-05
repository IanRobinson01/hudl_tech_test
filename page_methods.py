#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
defines methods which mimic user interaction
"""


class BasePageObject(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPageMethods(BasePageObject):

    pass