from locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_xpath = Locators.username_xpath
        self.password_xpath = Locators.password_xpath
        self.login_button2_xpath = Locators.login_button2_xpath
        self.categories_menu = Locators.categories_menu
        self.order = Locators.order
        self.favorite_product = Locators.favorite_product
        self.profile = Locators.profile
        self.subscription = Locators.subscription
        self.pre_order = Locators.pre_order
        self.comments = Locators.comments
        self.faq = Locators.faq
        self.advice = Locators.advice

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_xpath).clear()
        self.driver.find_element_by_xpath(self.username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_xpath).clear()
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def click_login2(self):
        self.driver.find_element_by_xpath(self.login_button2_xpath).click()

    def assert_categories_menu_profile(self):
        self.driver.find_element_by_xpath(self.categories_menu)

    def click_order_page(self):
        self.driver.find_element_by_xpath(self.order).click()


