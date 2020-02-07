#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
defines methods which mimic user interaction
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_elements import LoginPageElements, HomePageElements


class BasePageObject(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPageMethods(BasePageObject):

    def enter_email(self, email):
        email_field = self.driver.find_element(*LoginPageElements.email)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, pwd):
        pwd_field = self.driver.find_element(*LoginPageElements.password)
        pwd_field.clear()
        pwd_field.send_keys(pwd)

    def click_login(self):
        login_btn = self.driver.find_element(*LoginPageElements.login)
        login_btn.click()

    def click_remember_me(self):
        pass


class HomePageMethods(BasePageObject):

    def get_home_text(self):
        text = self.driver.find_element(*HomePageElements.home_text)
        # fails if i pass in the variable, but not when i pass in the element directly
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'hui-globalnav__home')))
