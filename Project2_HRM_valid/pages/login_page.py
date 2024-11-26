from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException
)


class LoginPage:
    try:
        # initialising the web driver
        def __init__(self, driver):
            self.driver = driver
            self.username_field = (By.NAME, "username")
            self.password_field = (By.NAME, "password")
            self.login_button = (By.XPATH, '//button[@type="submit"]')
            self.error_message = (By.CSS_SELECTOR, '.error-message')

        def enter_username(self, username):
            # Wait for the element to be located then send keys
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).send_keys(
                username)

        def enter_password(self, password):
            # Wait for the element to be located then send keys
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).send_keys(
                password)

        def click_login(self):
            # Wait for the element to be located then click
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

        def login(self, username, password):
            self.enter_username(username)
            self.enter_password(password)
            self.click_login()

    except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
        print(f"Error waiting for or interacting with element: {e}")
