from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_show_banner():
    driver = webdriver.Chrome('/home/dasha/Documents/driver/chromedriver')
    # открываю страницу максимально широко, чтобы все ссылки не "прятались"
    driver.maximize_window()
    # Переходим на главную страницу
    driver.get('https://aliexpress.ru/home.htm')
    # жду пока не появится баннер
    wait = WebDriverWait(driver, 10)
    # переключение на iframe, чтобы можно было найти и нажать на баннер
    time.sleep(60)
    driver.switch_to.frame('pc_1455_24317_20201202')
    # проверка что баннер загрузился
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.rax-image ')))
    assert len(driver.find_elements_by_css_selector('img.rax-image ')) == 2
    # нажимаю на крестик на баннере
    driver.find_elements_by_css_selector('img.rax-image ')[1].click()
    # переключение на главную страницу сайта
    driver.switch_to.default_content()
    # проверяю, что баннера нет на странице
    assert not driver.find_elements_by_css_selector('img.rax-image ')
    # нажала на кнопку с телефонами
    driver.find_element_by_css_selector('#home-firstscreen .cl-item-phones .cate-name').click()
    # убираю баннер, нажимаю на крестик
    driver.find_element_by_css_selector('a.next-dialog-close').click()
    #проверка что в категории етсь товары
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()
    # проверяю что в каждой категории есть товары
    driver.find_element_by_css_selector('#home-firstscreen .cl-item-computer .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-electronics .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-homeImprovemen .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-women .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-men .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-toys .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-jewelry .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-shoes .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-garden .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-autoParts .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-beauty .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-sports .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
