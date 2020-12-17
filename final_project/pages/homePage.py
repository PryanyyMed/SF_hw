
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from locators.locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        actions = ActionChains(driver)

        # потом новый локатор (НЛ) оформляю как здесь и иду вниз к созданию def
        self.pop_up_message_close = Locators.pop_up_message_close
        self.hero_image = Locators.hero_image
        self.slide_hero_img_btn = Locators.slide_hero_img_btn
        self.login_button_class_name = Locators.login_button_class_name
        self.search_bar_name = Locators.search_bar_name
        self.search_button_css_selector = Locators.search_button_css_selector
        self.search_drop_down = Locators.search_drop_down
        self.products_titles = Locators.products_titles
        self.invalid_search_result = Locators.invalid_search_result

        # header buttons
        self.catalog = Locators.catalog
        self.logo = Locators.logo
        self.special_offer = Locators.special_offer
        self.compare = Locators.compare
        self.drop_down_compare = Locators.drop_down_compare
        self.watched = Locators.watched
        self.wish_list = Locators.wish_list
        self.drop_down_wish_list = Locators.drop_down_wish_list
        self.cart = Locators.cart

        # telephone
        self.telephone_btn = Locators.telephone_btn
        self.first_telephone_link = Locators.first_telephone_link
        self.hover_telephone_btn = Locators.hover_telephone_btn
        self.first_telephone = Locators.first_telephone
        # smart_clock
        self.smart_clock_gadgets = Locators.smart_clock_gadgets
        self.hover_clock_gadgets = Locators.hover_clock_gadgets
        self.all_clock_gadgets = Locators.all_clock_gadgets
        self.first_clock = Locators.first_clock
        self.first_clock_link = Locators.first_clock_link
        # PC
        self.PC = Locators.PC
        self.hover_macbook = Locators.hover_macbook
        self.mac_book = Locators.mac_book
        self.first_mac = Locators.first_mac
        self.first_mac_link = Locators.first_mac_link
        # audio
        self.audio = Locators.audio
        self.hover_audio = Locators.hover_audio
        self.first_audio = Locators.first_audio
        self.first_audio_link = Locators.first_audio_link
        # gaming
        self.gaming = Locators.gaming
        self.household = Locators.household
        self.photo_video = Locators.photo_video
        self.repairs = Locators.repairs
        self.accessories = Locators.accessories
        self.kids = Locators.kids
        self.essential_goods = Locators.essential_goods
        self.auto = Locators.auto
        self.soft = Locators.soft
        self.NY_goods = Locators.NY_goods
        # footer_links
        self.footer_block = Locators.footer_block
        self.subscribe_bar = Locators.subscribe_bar
        self.subscribe_btn = Locators.subscribe_btn
        self.facebook = Locators.facebook
        self.vk = Locators.vk
        self.twitter = Locators.twitter
        self.inst = Locators.inst
        self.googleplay = Locators.googleplay
        self.appstore = Locators.appstore
        self.appgallery = Locators.appgallery

    # после того как сделала def иду к станице с тестом и там пишу ссылку уже на новую созданную функцию def

    def click_login_button(self):
        self.driver.find_element_by_class_name(self.login_button_class_name).click()

    def go_to_hero_image_page(self):
        self.driver.find_element_by_xpath(self.hero_image).click()

    def click_slide_slide_hero_img_btn(self):
        self.driver.find_element_by_xpath(self.slide_hero_img_btn).click()

    def check_main_search(self, user_input):
        self.driver.find_element_by_xpath(self.search_bar_name).clear()
        self.driver.find_element_by_xpath(self.search_bar_name).send_keys(user_input)

    def click_submit_search(self):
        self.driver.find_element_by_xpath(self.search_button_css_selector).click()

    def close_pop_up(self):
        self.driver.find_element_by_css_selector(self.pop_up_message_close).click()

    def click_catalog(self):
        self.driver.find_element_by_xpath(self.catalog).click()

    def click_telephone_btn(self):
        self.driver.find_element_by_xpath(self.telephone_btn).click()

    def place_cursor_telephone_btn(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        self.driver.find_element_by_xpath(self.catalog).click()
        # hover_telephone_btn = self.driver.find_element_by_xpath(self.hover_telephone_btn)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.telephone_btn)))
        actions.move_to_element(element)

    def click_on_product_page_link(self):
        self.driver.find_element_by_xpath(self.first_telephone).click()
        # self.driver.back()
        # actions.double_click(telephone_btn).perform()
        # # self.driver.find_element_by_xpath(self.telephone_btn).click()
        # assert self.driver.find_element_by_tag_name('h1').text == "Телефоны и аксессуары"
        # self.driver.back()

    def click_smart_clock_gadgets(self):
        self.driver.find_element_by_xpath(self.smart_clock_gadgets).click()

    def place_cursor_clock_gadgets(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        # self.driver.find_element_by_xpath(self.catalog).click()
        # hover_smart_clock_gadgets = self.driver.find_element_by_xpath(self.hover_clock_gadgets)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.smart_clock_gadgets)))
        actions.move_to_element(element)

    def click_on_product_page_link_clock(self):
        self.driver.find_element_by_xpath(self.first_clock).click()
        # self.driver.find_element_by_xpath(self.all_clock_gadgets).click()
        # self.driver.back()

    def click_pc(self):
        self.driver.find_element_by_xpath(self.PC).click()
        # driver = self.driver
        # wait = WebDriverWait(driver, 10)
        # actions = ActionChains(driver)
        # hover_macbook = self.driver.find_element_by_xpath(self.hover_macbook)
        # element = wait.until(EC.presence_of_element_located((By.XPATH, self.PC)))
        # actions.move_to_element(element).move_to_element(hover_macbook).click().perform()
        # self.driver.find_element_by_link_text(self.mac_book).click()
        # assert self.driver.find_element_by_tag_name('h1').text == "Apple MacBook"
        # self.driver.back()

    def place_cursor_pc(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.PC)))
        actions.move_to_element(element)

    def click_on_first_mac(self):
        self.driver.find_element_by_xpath(self.first_mac).click()

    def click_audio(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        # self.driver.find_element_by_xpath(self.catalog)
        hover_audio = self.driver.find_element_by_xpath(self.hover_audio)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.audio)))
        actions.move_to_element(element).move_to_element(hover_audio).click().perform()
        assert self.driver.find_element_by_tag_name('h1').text == "Беспроводные наушники"

    def click_on_first_audio(self):
        self.driver.find_element_by_xpath(self.first_audio).click()

    def click_gaming(self):
        self.driver.find_element_by_xpath(self.gaming).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Гейминг"
        self.driver.back()

    def click_household(self):
        self.driver.find_element_by_xpath(self.household).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Видео и техника для дома"
        self.driver.back()

    def click_photo_video(self):
        self.driver.find_element_by_xpath(self.photo_video).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Фото- и видеокамеры"
        self.driver.back()

    def click_repairs(self):
        self.driver.find_element_by_xpath(self.repairs).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Для дома и ремонта"
        self.driver.back()

    def click_accessories(self):
        self.driver.find_element_by_xpath(self.accessories).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Аксессуары для электроники"
        self.driver.back()

    def click_kids(self):
        self.driver.find_element_by_xpath(self.kids).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Игрушки и товары для детей"
        self.driver.back()

    def click_essential_goods(self):
        self.driver.find_element_by_xpath(self.essential_goods).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Товары первой необходимости"
        self.driver.back()

    def click_auto(self):
        self.driver.find_element_by_xpath(self.auto).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Автотовары"
        self.driver.back()

    def click_soft(self):
        self.driver.find_element_by_xpath(self.soft).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Услуги и софт"
        self.driver.back()

    def click_NY_goods(self):
        self.driver.find_element_by_xpath(self.NY_goods).click()
        assert self.driver.find_element_by_tag_name('h1').text == "Новогодние товары"
        self.driver.back()

    def click_logo(self):
        self.driver.find_element_by_xpath(self.logo).click()

    def click_special_offer(self):
        self.driver.find_element_by_xpath(self.special_offer).click()

    def click_login_button_class_name(self):
        self.driver.find_element_by_xpath(self.login_button_class_name).click()

    def click_compare(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        # drop_down_compare = self.driver.find_element_by_xpath(self.drop_down_compare)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.compare)))
        actions.move_to_element(element)

    def click_watched(self):
        self.driver.find_element_by_xpath(self.watched).click()

    def click_wish_list(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.wish_list)))
        actions.move_to_element(element)
        self.driver.find_element_by_xpath(self.wish_list).click()

    def click_cart(self):
        self.driver.find_element_by_xpath(self.cart).click()

    def click_facebook(self):
        self.driver.find_element_by_xpath(self.facebook).click()
