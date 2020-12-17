from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append('..')
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from selenium.webdriver.support.ui import WebDriverWait


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/home/dasha/Documents/driver/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # 5 tests

    def test_search_request_valid_category(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.check_main_search("Ноутбуки")
        homepage.click_submit_search()
        time.sleep(5)

        wait = WebDriverWait(self.driver, 10)
        assert len(homepage.products_titles) >= 1
        # assert self.driver.find_element_by_xpath(homepage.products_titles).text == "Samsung"

    def test_search_request_valid_brand_name(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.check_main_search("Смартфоны Samsung")
        homepage.click_submit_search()
        time.sleep(5)

        wait = WebDriverWait(self.driver, 10)
        assert len(homepage.products_titles) >= 1
        # assert self.driver.find_element_by_xpath(homepage.products_titles).text == "Samsung"

    def test_search_request_valid_product_name(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.check_main_search("apple iphone 12 pro")
        homepage.click_submit_search()
        time.sleep(5)

        wait = WebDriverWait(self.driver, 10)
        assert len(homepage.products_titles) >= 1
        # assert self.driver.find_element_by_xpath(homepage.products_titles).text == "Samsung"

    def test_search_request_invalid_letters(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.check_main_search("игныимнг769вап97ц")
        homepage.click_submit_search()

        wait = WebDriverWait(self.driver, 10)
        assert self.driver.find_element_by_xpath(homepage.invalid_search_result).text == "Ничего не найдено"

    def test_search_request_invalid_symbols(self):
        driver = self.driver

        driver.get("https://www.svyaznoy.ru/")

        homepage = HomePage(driver)
        homepage.check_main_search("&&&")
        homepage.click_submit_search()

        wait = WebDriverWait(self.driver, 10)
        assert self.driver.find_element_by_xpath(homepage.invalid_search_result).text == "Ничего не найдено"

    def test_search_dropdown(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.check_main_search("Play")
        assert self.driver.find_element_by_xpath(homepage.search_drop_down)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test complete!')
