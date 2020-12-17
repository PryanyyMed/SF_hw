from selenium import webdriver
import unittest
import sys
import os
sys.path.append('..')
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/home/dasha/Documents/driver/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_scroll_down_assert_footer(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        page = driver.find_element_by_tag_name("html")
        page.send_keys(Keys.END)
        assert driver.find_element_by_xpath(homepage.footer_block)

    # def test_click_facebook(self):
    #     driver = self.driver
    #     driver.get("https://www.svyaznoy.ru/")
    #     driver.implicitly_wait(10)
    #     homepage = HomePage(driver)
    #     page = driver.find_element_by_tag_name("html")
    #     page.send_keys(Keys.END)
    #     homepage.click_facebook()
    #     URL = driver.current_url
    #     assert URL == "https://www.facebook.com/svyaznoy.ru"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test complete!')