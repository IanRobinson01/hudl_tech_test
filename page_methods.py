#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
defines methods which mimic user interaction
"""

import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_locators import LoginPageElements, HomePageElements
from utils import add_log_entry, cfg


class BasePageObject:
    """ class which all page method classes inherit from"""
    def __init__(self, driver):
        self.driver = driver


class LoginPageMethods(BasePageObject):
    """ defines all methods for interacting with the login page """

    def enter_email(self, email_text):
        EnterText(self.driver, LoginPageElements.email, email_text)

    def enter_password(self, pwd_text):
        EnterText(self.driver, LoginPageElements.password, pwd_text)

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
    """ defines all methods for interacting with the home page """

    def get_home_text(self):
        return PageHelpers(self.driver).check_element_visible(HomePageElements.home_text)


class PageHelpers(BasePageObject):
    """ helper methods for use in page method classes """

    def check_element_visible(self, element):
        try:
            WebDriverWait(self.driver, cfg['wait_time'])\
                .until(EC.visibility_of_element_located(element))
            return True
        except TimeoutException:
            add_log_entry(f'test timed out whilst looking for element: {element}')
            pytest.fail('test timed out whilst looking for element')


class EnterText(BasePageObject):
    """ generic class for entering text into a text field """

    def __init__(self, driver, locator, text):
        super().__init__(driver)
        self.locator = locator
        self.text = text
        PageHelpers(self.driver).check_element_visible(self.locator)
        field = self.driver.find_element(*self.locator)
        field.clear()
        field.send_keys(text)
