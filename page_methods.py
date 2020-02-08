#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
defines methods which mimic user interaction
"""

import pytest
import utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_locators import LoginPageElements, HomePageElements


class BasePageObject(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPageMethods(BasePageObject):

    def enter_email(self, email_text):
        PageHelpers(self.driver).check_element_visible(LoginPageElements.email)
        email_field = self.driver.find_element(*LoginPageElements.email)
        email_field.clear()
        email_field.send_keys(email_text)

    def enter_password(self, pwd_text):
        PageHelpers(self.driver).check_element_visible(LoginPageElements.password)
        pwd_field = self.driver.find_element(*LoginPageElements.password)
        pwd_field.clear()
        pwd_field.send_keys(pwd_text)

    def login(self, entry_method):
        PageHelpers(self.driver).check_element_visible(LoginPageElements.login)
        login_btn = self.driver.find_element(*LoginPageElements.login)
        if entry_method == 'button':
            login_btn.click()
        elif entry_method == 'return_key':
            login_btn.send_keys(Keys.RETURN)
        else:
            pytest.fail('entry method not recognised')

    def click_remember_me(self):
        PageHelpers(self.driver).check_element_visible(LoginPageElements.remember_me)
        rmbr_me_box = self.driver.find_element(*LoginPageElements.remember_me)
        rmbr_me_box.click()

    def get_error_text(self):
        PageHelpers(self.driver).check_element_visible(LoginPageElements.login_error)
        error_text = self.driver.find_element(*LoginPageElements.login_error)
        return error_text.text


class HomePageMethods(BasePageObject):

    def get_home_text(self):
        text = HomePageElements.home_text
        PageHelpers(self.driver).check_element_visible(text)
        return text


class PageHelpers(BasePageObject):

    def check_element_visible(self, element):
        try:
            WebDriverWait(self.driver, utils.cfg['wait_time']).until(EC.visibility_of_element_located(element))
            return True
        except TimeoutException:
            pytest.fail('test timed out whilst looking for element')
