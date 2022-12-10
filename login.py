import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By


def test_login():
    #
    login = "standard_user"
    password = "secret_sauce"

    chrome_driver = Chrome('chromedriver.exe')
    chrome_driver.get('https://www.saucedemo.com/')
    time.sleep(5)
    login_input_locator = '//input[@id="user-name"]'
    login_input_element = chrome_driver.find_element(By.XPATH, login_input_locator)
    login_input_element.clear()
    login_input_element.send_keys(login)

    password_input_locator = '#password'
    password_input_element = chrome_driver.find_element(By.CSS_SELECTOR, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    password_input_element.send_keys(Keys.ENTER)
    # Page object
    login_button_locator = '#login-button'
    login_button_element = chrome_driver.find_element(By.CSS_SELECTOR, login_button_locator)
    login_button_element.click()
    time.sleep(5)
    shopping_card_locator = "#shopping_cart_container"
    shopping_card_element = chrome_driver.find_element(By.XPATH, shopping_card_locator)
    is_shopping_card = shopping_card_element.is_displayed()

    assert is_shopping_card is True, 'User was not logged-in'
    shopping_card_element.screenshot('element_screenshot.jpg')
    chrome_driver.back()
