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

    def test_hero_image(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        assert driver.find_element_by_xpath(homepage.hero_image)
        homepage.click_slide_slide_hero_img_btn()

    def test_go_to_hero_image_page(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.go_to_hero_image_page()

    def test_scroll_down(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        page = driver.find_element_by_tag_name("html")
        page.send_keys(Keys.END)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test complete!')
