from selenium import webdriver
import unittest
import sys
import time
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

    def test_click_logo(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_logo()
        URL = driver.current_url
        assert URL == 'https://www.svyaznoy.ru/'

    def test_click_special_offer(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_special_offer()
        URL = driver.current_url
        assert URL == 'https://www.svyaznoy.ru/special-offers'

    def test_click_compare(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_compare()
        assert driver.find_element_by_xpath(homepage.drop_down_compare)

    def test_watched(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_watched()
        URL = driver.current_url
        assert URL == 'https://www.svyaznoy.ru/product-you-watched'

    def test_wish_list(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_wish_list()
        assert driver.find_element_by_xpath(homepage.drop_down_wish_list)

    def test_click_cart(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_cart()
        URL = driver.current_url
        assert URL == 'https://www.svyaznoy.ru/cart/'

    # проверяю что при наведении курсора на пункт меню, отуроется выпадающая страница, с работающей ссылкй на товары
    def test_telephone_btn(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        # homepage.название_def_из-homePage
        # -это ссылка на класс из файла homePage, от туда идут ссылки на локаторы и функции с ними.
        # Здесь можно передавать переменные в тест (логин, пароль и тд)
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_telephone_btn()
        assert self.driver.find_element_by_tag_name('h1').text == "Телефоны и аксессуары"

    # при клике на продукт, происходит переход на его страницу
    def test_click_on_product_page_link(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/catalog/phone/224")
        homepage = HomePage(driver)
        homepage.click_on_product_page_link()
        URL = driver.current_url
        assert homepage.first_telephone_link in URL
        # self.driver.back()

    def test_place_cursor_telephone_btn(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_catalog()
        homepage.place_cursor_telephone_btn()
        assert self.driver.find_element_by_xpath(homepage.hover_telephone_btn)

    def test_smart_clock_gadgets(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_smart_clock_gadgets()
        assert self.driver.find_element_by_tag_name('h1').text == "Смарт-часы и гаджеты"

    def test_click_first_clock(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/catalog/accessories/8936")
        homepage = HomePage(driver)
        homepage.click_on_product_page_link_clock()
        URL = driver.current_url
        assert homepage.first_clock_link in URL

    def test_place_cursor_clock_gadgets(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_catalog()
        homepage.place_cursor_clock_gadgets()
        assert self.driver.find_element_by_xpath(homepage.hover_clock_gadgets)

    def test_click_pc(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_pc()
        assert self.driver.find_element_by_tag_name('h1').text == "Ноутбуки и компьютеры"

    def test_click_first_mac(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/catalog/notebook/1738/apple")
        homepage = HomePage(driver)
        homepage.click_on_first_mac()
        URL = driver.current_url
        assert homepage.first_mac_link in URL

    def test_place_cursor_pc(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_catalog()
        homepage.place_cursor_pc()
        assert self.driver.find_element_by_xpath(homepage.hover_macbook)

    def test_click_audio(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/")
        homepage = HomePage(driver)
        homepage.close_pop_up()
        homepage.click_audio()

    def test_click_first_audio(self):
        driver = self.driver
        driver.get("https://www.svyaznoy.ru/catalog/audiovideo/1558/tag/besprovodnye")
        homepage = HomePage(driver)
        homepage.click_on_first_audio()
        URL = driver.current_url
        assert homepage.first_audio_link in URL



        # homepage.click_pc()
        # homepage.click_audio()
        # homepage.click_gaming()
        # homepage.click_household()
        # homepage.click_photo_video()
        # homepage.click_repairs()
        # homepage.click_accessories()
        # homepage.click_kids()
        # homepage.click_essential_goods()
        # homepage.click_auto()
        # homepage.click_soft()
        # homepage.click_NY_goods()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test complete!')
