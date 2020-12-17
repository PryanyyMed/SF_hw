from selenium import webdriver
import unittest
import pickle
import sys
import os
sys.path.append('..')
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/home/dasha/Documents/driver/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # 6 tests

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.click_login_button()

        login = LoginPage(driver)
        login.enter_username("dan555505@yandex.ru")
        login.enter_password("123456Pp")
        login.click_login2()
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

        wait = WebDriverWait(self.driver, 10)
        assert self.driver.find_element_by_class_name('b-personal__board-name').text == "Dan"

    def test_login_invalid_username(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.click_login_button()

        login = LoginPage(driver)
        login.enter_username("dan123@yandex.ru")
        login.enter_password("123456Pp")
        login.click_login2()

        wait = WebDriverWait(self.driver, 10)
        assert self.driver.find_element_by_xpath(
            "//span[@id='user[username]-error']").text == "Логин или пароль неверен"

    def test_login_invalid_password(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.click_login_button()

        login = LoginPage(driver)
        login.enter_username("dan555505@yandex.ru")
        login.enter_password("123456")
        login.click_login2()

        wait = WebDriverWait(self.driver, 10)
        assert self.driver.find_element_by_xpath(
            "//span[@id='user[username]-error']").text == "Логин или пароль неверен"

    def test_login_emptyfield_username(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.click_login_button()

        login = LoginPage(driver)
        login.enter_username("")
        login.enter_password("123456")
        login.click_login2()

        wait = WebDriverWait(self.driver, 10)
        assert self.driver.find_element_by_xpath(
            "//span[@id='user[username]-error']").text == "Это поле необходимо заполнить."

    def test_login_emptyfield_password(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.click_login_button()

        login = LoginPage(driver)
        login.enter_username("dan555505@yandex.ru")
        login.enter_password("")
        login.click_login2()

        wait = WebDriverWait(self.driver, 10)
        assert self.driver.find_element_by_xpath(
            "//span[@id='user[password]-error']").text == "Это поле необходимо заполнить."

    def test_login_emptyfields_username_password(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.click_login_button()

        login = LoginPage(driver)
        login.enter_username("")
        login.enter_password("")
        login.click_login2()

        wait = WebDriverWait(self.driver, 10)
        assert self.driver.find_element_by_xpath(
            "//span[@id='user[username]-error']").text == "Это поле необходимо заполнить."
        assert self.driver.find_element_by_xpath(
            "//span[@id='user[password]-error']").text == "Это поле необходимо заполнить."

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test complete!')
