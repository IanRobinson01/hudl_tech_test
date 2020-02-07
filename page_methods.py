#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
defines methods which mimic user interaction
"""

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_elements import LoginPageElements, HomePageElements


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

    def click_login(self):
        PageHelpers(self.driver).check_element_visible(LoginPageElements.login)
        login_btn = self.driver.find_element(*LoginPageElements.login)
        login_btn.click()

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
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
            return True
        except TimeoutException:
            pytest.fail('test timed out whilst looking for element')
