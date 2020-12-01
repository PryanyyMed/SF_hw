import pytest
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
    driver.switch_to.frame('pc_1455_24317_20201201')
    # проверка что баннер загрузился
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.rax-image ')))
    assert len(driver.find_elements_by_css_selector('img.rax-image ')) == 2
    # нажимаю на крестик на баннере
    # element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.rax-image ')))
    driver.find_elements_by_css_selector('img.rax-image ')[1].click()
    time.sleep(5)
    # переключение на главную страницу сайта
    driver.switch_to.default_content()
    # driver.switch_to.frame('ym-native-frame')
    # проверяю, что баннера нет на странице
    # wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'img.rax-image ')))
    assert not driver.find_elements_by_css_selector('img.rax-image ')
    # нажала на кнопку с телефонами
    driver.find_element_by_css_selector('#home-firstscreen .cl-item-phones .cate-name').click()
    # убираю тупой баннер, который мешает номально дописать этот тест!!!!!!!!!!!!!!!!!!!!!!
    driver.switch_to.frame('ym-native-frame')
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.next-dialog-close')))
    # assert len(driver.find_elements_by_css_selector('a.next-dialog-close')) == 1
    driver.find_element_by_css_selector('a.next-dialog-close').click()
    # проверка что товары есть на старнице
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
