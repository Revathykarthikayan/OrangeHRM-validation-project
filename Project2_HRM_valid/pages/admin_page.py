from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException
)
from pages.base_page import BasePage


class Admin(BasePage):
    # providing locators for the elements to be asserted below
    ADMIN = (By.XPATH, '//span[text()="Admin"]')
    USER_MANAGEMENT = (By.XPATH, '//span[text()="User Management "]')
    JOB = (By.XPATH, '//span[text()="Job "]')
    ORGANISATION = (By.XPATH, '//span[text()="Organization "]')
    QUALIFICATIONS = (By.XPATH, '// span[text() = "Qualifications "]')

    MORE = (By.XPATH, '//span[text()="More "]')
    NATIONALITIES = (By.XPATH, '//a[text()="Nationalities "] ')
    BRANDING = (By.XPATH, '//a[text()="Corporate Branding "] ')
    CONFIGRATION = (By.XPATH, '//a[text()="Configuration "] ')
    DROPDOWN = (By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]')
    LOGOUT = (By.XPATH, '//a[text()="Logout"]')

    def go_to_admin(self):
        try:
            # Wait for the element to be visible then click
            self.click_element(self.ADMIN)
            self.get_title()

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with admin element: {e}")

    def user_management(self, user_text):
        try:
            # Wait for the element to be visible then check
            self.assert_text(self.USER_MANAGEMENT, user_text)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with user_management element: {e}")

    def job(self, text):
        try:
            # Wait for the element to be visible then check
            self.assert_text(self.JOB, text)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with job element: {e}")

    def organisation(self, org_text):
        try:
            # Wait for the element to be visible then check
            self.assert_text(self.ORGANISATION, org_text)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with organisation element: {e}")

    def qualifications(self, qualification_text):
        try:
            # Wait for the element to be visible then check
            self.assert_text(self.QUALIFICATIONS, qualification_text)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with Qualifications element: {e}")

    def more(self):
        try:
            # Wait for the element to be visible then check
            self.click_element(self.MORE)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with more web element: {e}")

    def nationalities(self, nationality_text):
        try:
            # Wait for the element to be visible then check
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.
                                                 NATIONALITIES))
            self.assert_text(self.NATIONALITIES, nationality_text)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with nationalities element: {e}")

    def corporate_branding(self, corporate_text):
        try:
            # Wait for the element to be visible then check
            self.assert_text(self.BRANDING, corporate_text)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with corporate_branding element: {e}")

    def configuration(self, configuration_text):
        try:
            # Wait for the element to be visible then check
            self.assert_text(self.CONFIGRATION, configuration_text)

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with configuration element: {e}")

    def logout(self):
        try:
            # clicking logout after asserting all the element text
            self.click_element(self.DROPDOWN)
            self.click_element(self.LOGOUT)
            print("Logged out successfully")

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with element in logout: {e}")
