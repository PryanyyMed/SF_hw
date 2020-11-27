import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def test_show_banner():
    driver = webdriver.Chrome('/home/dasha/Documents/driver/chromedriver')
    # Переходим на главную страницу
    driver.get('https://aliexpress.ru/home.htm')
    # переключение на iframe, чтобы можно было найти и нажать на баннер
    driver.switch_to.frame("pc_1455_24317_20201127")
    try:
        # жду пока не появится баннер
        wait = WebDriverWait(driver, 10)
        # нажимаю на крестик на баннере
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.rax-image ')))
    # переключение на главную страницу сайта
    finally:
        driver.switch_to.default_content()
    #зайти на страницу с категорией товара
    # driver.find_element_by_xpath('//*[@id="home-firstscreen"]'
    #                              '/div[2]/div/div[2]/div/div[2]/dl[1]/dt/span/a').click()
    # assert driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li') >= 1
