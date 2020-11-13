import pytest
from selenium import webdriver
import uu
import os
import uuid
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# зайти на главную страницу со всеми петами

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
    time.sleep(0)

    # Переход к моим петам
    pytest.driver.find_element_by_css_selector('button[type="button"]').click()
    pytest.driver.find_element_by_class_name("nav-link").click()
    time.sleep(0)

    # Проверяем, что мы оказались на странице пользователя с его петами
    assert pytest.driver.find_element_by_tag_name('h2').text == "Dan"

    # Явное ожидание появление элементов таблицы на странице
    wait = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located(('id', 'all_my_pets')))

    # посчитать кол-во петов на странице
    assert len(pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr')) == 6

    # проверка, что у каждой карточки есть картинка, имя и описание
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')

    for i in range(len(names)):
        # хотябы у половины петов есть картинка
        assert images[i].get_attribute('src') >= 2
        # у всех есть имя
        assert names[i].text != ''
        # у всех есть описание
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
        # у всех разные имена
        assert names.text != names[3].text
