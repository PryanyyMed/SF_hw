from selenium import webdriver
import unittest
import sys
import time
import os

sys.path.append('..')
from pages.homePage import HomePage
from pages.productPage import ProductPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/home/dasha/Documents/driver/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # у товаров есть заголовки
    def test_items_product_page_title(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/catalog/phone/224")
        productpage = ProductPage(driver)
        assert self.driver.find_element_by_xpath(productpage.title)

    # переход на страницу товара, наличие основных эл-ов страницы
    def test_items_product_page_pic(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/catalog/phone/224")
        productpage = ProductPage(driver)
        productpage.go_to_first_telephone_product_page()
        assert self.driver.find_element_by_xpath(productpage.pic)
        assert self.driver.find_element_by_xpath(productpage.buy_btn)
        assert self.driver.find_element_by_xpath(productpage.also_buy)
        assert self.driver.find_element_by_xpath(productpage.product_card)
        assert self.driver.find_element_by_xpath(productpage.similar)
        assert self.driver.find_element_by_xpath(productpage.looked_with)
        assert self.driver.find_element_by_xpath(productpage.slider_container)

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/catalog/phone/224/5722937")
        productpage = ProductPage(driver)
        time.sleep(5)
        productpage.to_add_to_cart()
        assert self.driver.find_element_by_xpath(productpage.pop_up_with_item)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test complete!')
