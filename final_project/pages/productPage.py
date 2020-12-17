from selenium import webdriver
from selenium.webdriver import ActionChains
from locators.locators import Locators
from pages.homePage import HomePage


class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        # items
        self.telephone_btn = Locators.telephone_btn
        self.first_telephone = Locators.first_telephone
        self.title = Locators.title
        self.pic = Locators.pic
        self.buy_btn = Locators.buy_btn
        self.also_buy = Locators.also_buy
        self.product_card = Locators.product_card
        self.similar = Locators.similar
        self.looked_with = Locators.looked_with
        self.slider_container = Locators.slider_container
        self.add_to_cart = Locators.add_to_cart
        self.pop_up_with_item = Locators.pop_up_with_item
        self.close_pop_up_with_item = Locators.close_pop_up_with_item
        self.continue_offer = Locators.continue_offer

    def go_to_first_telephone_product_page(self):
        self.driver.find_element_by_xpath(self.first_telephone).click()

    def to_add_to_cart(self):
        self.driver.find_element_by_xpath(self.add_to_cart()).click()




