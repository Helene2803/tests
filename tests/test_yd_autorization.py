import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    phone_input = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="phone-input"]')
    phone_input.send_keys(user_phone)
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.element_to_be_clickable
                        ((By.CSS_SELECTOR, 'button[data-testid="split-add-user-next-phone"]')))
    button.click()

    input_field = wait.until(EC.visibility_of_element_located
                             ((By.CSS_SELECTOR, 'input[data-testid="code-field-segment"]')))

    assert input_field.is_displayed() == True


