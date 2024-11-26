from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException
)


class ResetPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.forgot_pwd = (By.XPATH, '//p[text()="Forgot your password? "]')
        self.user_pwd = (By.XPATH, '//input[@placeholder="Username"]')
        self.reset_pwd = (By.XPATH, '// button[text() = " Reset Password "]')
        self.message = (By.XPATH, '//h6[@class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]')

    # method for checking compatibility of the browser
    def compatibility(self):
        try:
            warning_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'unsupported browser')]")
            assert not warning_message.is_displayed(), "Unsupported browser warning detected."
        except NoSuchElementException:
            # If no warning is found, assume compatibility is okay
            pass

    # method to enter username
    def enter_username(self, username):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).send_keys(
                username)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:

            print(f"Error waiting for or interacting with username element: {e}")

    # method to click forgot password button
    def forgot_password(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.forgot_pwd)).click()
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with password element: {e}")

    # method for entering username to get new password
    def username_password(self, username_pwd):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.user_pwd)).send_keys(username_pwd)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with login button: {e}")

    # method for clicking reset password button
    def reset_password(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.reset_pwd)).click()
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with reset button: {e}")

    # method for asserting success message
    def validate_confirmation(self):
        message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.message))
        success_message = message.text

        # validating the message
        expected_message = "Reset Password link sent successfully"
        assert success_message == expected_message, f"Expected '{expected_message}', Resend request once again!!!"
        print("Reset Password Success message seen.\n Browser is closed successfully")
