import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_banner():
    driver = webdriver.Chrome('/home/dasha/Documents/driver/chromedriver')
    # Переходим на главную страницу
    driver.get('https://aliexpress.ru/home.htm')
    # ожидание баннера
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME('img.rax-image '))))
    finally:
        driver.quit()

    # # Нажимаем на кнопку "крестик" на баннере
    # pytest.driver.find_elements_by_css_selector('.rax-image ')[1].click()
