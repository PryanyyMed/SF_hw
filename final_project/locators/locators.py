# новвй локатор добавляю сюда, потом иду в honePage

class Locators():
    # Login Page objects
    username_xpath = '//*[@id="user"]/div[1]/label/input'
    password_xpath = '//*[@id="user"]/div[2]/label/input'
    login_button2_xpath = '//*[@id="user"]/div[4]/div/label'
    # User Page
    categories_menu = "//div[contains(@class, 'c-personal-container__left')]"
    order = '//a[@href="https://www.svyaznoy.ru/personal/order"]'
    favorite_product = '//a[@href="https://www.svyaznoy.ru/personal/favorite-product"]'
    profile = '//a[@href="https://www.svyaznoy.ru/personal/profile"]'
    subscription = '//a[@href="https://www.svyaznoy.ru/personal/subscription"]'
    pre_order = '//a[@href="https://www.svyaznoy.ru/personal/pre-order"]'
    comments = '//a[@href="https://www.svyaznoy.ru/personal/comments"]'
    faq = '//a[@href="https://www.svyaznoy.ru/personal/faq"]'
    advice = '//a[@href="https://www.svyaznoy.ru/personal/advice"]'

    # Home page objects
    hero_image = "//div[contains(@class, 'b-grid__main b-first-line__main s-first-line__main')]"
    slide_hero_img_btn = "//button[contains(@class, 'slick-next slick-arrow')]"
    pop_up_message_close = 'div.s-geo-confirm-close.b-geo-confirm__close'
    search_bar_name = '//body/div[2]/div[7]/div[1]/div[3]/div[1]/form[1]/input[1]'
    search_button_css_selector = "//body/div[2]/div[7]/div[1]/div[3]/div[1]/form[1]/button[1]/*[1]"
    search_drop_down = "//div[contains(@class, 'b-css-dropdown _search _pl')]"
    products_titles = '//body/div[6]/div[1]/div[2]/div[1]/div[2]/div[1]/div'
    invalid_search_result = '//*[@id="pjax-container"]/div/div/div[1]'

    # Header buttons
    logo = '//a[@href="/"]'
    special_offer = '//a[@href="/special-offers"]'
    catalog = "//button[contains(text(),'Каталог товаров')]"
    login_button_class_name = 'b-header-account__inner'
    compare = "//div[contains(@class, 'b-header-compare__icon')]"
    drop_down_compare = "/html/body/div[2]/div[7]/div[1]/div[4]/div[3]/div[2]"
    watched = "//div[contains(@class, 'b-header-watched__icon')]"
    wish_list = "//div[contains(@class, 'b-header-wishlist__icon')]"
    drop_down_wish_list = '//a[@href="/catalog"]'
    cart = "//div[contains(@class, '_to-cart-area')]"
    # telephone
    telephone_btn = '//a[@href="/catalog/8660"]'
    hover_telephone_btn = '//a[@href="/catalog/phone/224"]'
    first_telephone = '//*[@id="pjax-container"]/div[2]/div/div[1]/div/div[2]/div[2]/a[1]'
    first_telephone_link = "/catalog/phone/224/5722937"
    # smart_clock_gadgets
    smart_clock_gadgets = '//a[@href="/catalog/4629821"]'
    hover_clock_gadgets = '//a[@href="/catalog/4629837"]'
    all_clock_gadgets = 'Все смарт часы'
    first_clock = "//div[contains(text(),'Amazfit Bip S Lite A1823 (черный)')]"
    first_clock_link = 'https://www.svyaznoy.ru/catalog/accessories/8936/5815895'
    # PC
    PC = '//a[@href="/catalog/8651"]'
    hover_macbook = '//a[@href="/catalog/4617281"]'
    mac_book = 'MacBook'
    first_mac = "//div[contains(text(),'Apple MacBook Air 13.3')]"
    first_mac_link = 'https://www.svyaznoy.ru/catalog/notebook/1738/5719874'
    # audio
    audio = '//a[@href="/catalog/8738"]'
    hover_audio = '//a[@href="/catalog/audiovideo/1558/tag/besprovodnye"]'
    first_audio = "//div[contains(text(),'Apple AirPods Pro (белый)')]"
    first_audio_link = 'https://www.svyaznoy.ru/catalog/audiovideo/1558/5663081'
    # gaming
    gaming = '//a[@href="/catalog/4617225"]'
    household = '//a[@href="/catalog/8672"]'
    photo_video = '//a[@href="/catalog/8678"]'
    repairs = '//a[@href="/catalog/4622841"]'
    accessories = '//a[@href="/catalog/8897"]'
    kids = '//a[@href="/catalog/4620741"]'
    essential_goods = '//a[@href="/catalog/4632829"]'
    auto = '//a[@href="/catalog/4629825"]'
    soft = '//a[@href="/catalog/4633921"]'
    NY_goods = '//a[@href="/catalog/presents/18038"]'

    # Product page items
    title = "//div[contains(@class, 'b-offer-top')]"
    pic = "//div[contains(@class, 'slick-track')]"
    buy_btn = '//a[@href="javascript:void(0);"]'
    also_buy = '//*[@id="vue-recommend"]/div/div'
    product_card = "//div[contains(@class, 'c-product-card-box')]"
    similar = '//*[@id="vue-similar"]'
    looked_with = '//*[@id="vue-looked-with"]'
    slider_container = "//div[contains(@class, 'c-product-slider-container _orange')]"

    add_to_cart = "//div[@class='b-offer-box__buttons']/span[@class='b-main-btn__text']"
    pop_up_with_item = '//*[@id="cta"]/div'
    close_pop_up_with_item = '//*[@id="cta"]/div/button'
    continue_offer = "//div[contains(@class, 'svz-btn _fill _orange is-mobile-not')]"

    # footer-links
    footer_block = "//div[contains(@class, 'b-footer')]"
    subscribe_bar = "//input[@id='subscribe-email-form-email']"
    subscribe_btn = '//*[@id="subscribe-email-form"]/input'
    facebook = '//a[@href="https://www.facebook.com/svyaznoy.ru"]'
    vk = '//a[@href="https://vk.com/svyaznoy"]'
    twitter = '//a[@href="https://twitter.com/svyaznoy_ru"]'
    inst = '//a[@href="https://www.instagram.com/svyaznoy_russia/?hl=ru"]'
    googleplay = '//a[@href="https://play.google.com/store/apps/details?id=ru.svyaznoy.shop"]'
    appstore = '//a[@href="https://apps.apple.com/ru/app/svaznoj-internet-magazin-elektroniki/id1062774471"]'
    appgallery = '//a[@href="https://appgallery.cloud.huawei.com/marketshare/app/C102123139?locale=ru_RU&source=appshare&subsource=C102123139"]'






