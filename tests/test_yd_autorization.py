import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/')
    yield driver
    driver.quit()

@pytest.fixture
def user_phone():
    phone = os.getenv('PHONE')
    yield phone

def test_correct_phone(driver, user_phone):

    phone_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="text-field-input"]')
    phone_input.send_keys(user_phone)
    time.sleep(5)

    button_click = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="split-add-user-next-phone"]')
    button_click.click()
    time.sleep(5)

    current_url = driver.current_url

    assert current_url == 'https://passport.yandex.ru/pwl-yandex/auth/code'

