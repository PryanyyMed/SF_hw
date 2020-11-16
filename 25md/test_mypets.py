# python3 -m pytest -s -v --driver Chrome --driver-path /home/dasha/Documents/driver/chromedriver  test_mypets.py

import pytest
from selenium import webdriver
import uu
import os
import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# зайти на главную страницу со всеми петами, всех пользователей

@pytest.mark.usefixtures("testing")
def test_show_my_pets():
    # добавляю неявное ожидание всех элементов на странице
    pytest.driver.implicitly_wait(5)

    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('dan555505@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('123456Pp')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # Переход к моим петам
    pytest.driver.find_element_by_css_selector('button[type="button"]').click()
    pytest.driver.find_element_by_class_name("nav-link").click()

    # Проверяем, что мы оказались на странице пользователя с его петами
    assert pytest.driver.find_element_by_tag_name('h2').text == "Dan"

    # Явное ожидание появление элементов таблицы на странице
    wait = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located(('id', 'all_my_pets')))

    # посчитать кол-во петов на странице, проверка, что все они есть на странице пользователя
    pets = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr')
    assert len(pets) == 2

    # проверка, что у каждой карточки есть картинка, имя и описание
    images = pytest.driver.find_element_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/th/img')

    for i in range(len(pets)):
        # проверка наличия картинок у всех петов
        print(images.is_displayed())
    # у всех есть имя, описание и возраст
    assert pytest.driver.find_elements_by_css_selector('#all_my_pets tr')[1].text == "Crazy Cat crazy 1\n×"
    assert pytest.driver.find_elements_by_css_selector('#all_my_pets tr')[2].text == "Test testing cat 21\n×"

    """ # таже проверка, но через xpath
    assert pytest.driver.find_element_by_xpath(
            '//*[@id="all_my_pets"]/table/tbody/tr/td').text == "Crazy Cat"
    assert pytest.driver.find_element_by_xpath(
            '//*[@id="all_my_pets"]/table/tbody/tr[2]/td').text == "Test"
    # у всех есть описание
    assert pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr/td[2]').text == "crazy"
    assert pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr[2]/td[2]').text == "testing cat"
    # у всех есть возраст
    assert pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr/td[3]').text == "1"
    assert pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr[2]/td[3]').text == "21"
    # у всех разные имена
    assert pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr/td').text != pytest.driver.find_element_by_xpath(
        '//*[@id="all_my_pets"]/table/tbody/tr[2]/td').text"""
