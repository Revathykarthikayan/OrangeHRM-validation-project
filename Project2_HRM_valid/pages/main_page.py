from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException
)
from pages.base_page import BasePage


class MainMenu(BasePage):
    # providing locators for the elements
    MAIN = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul')
    DROPDOWN = (By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]')
    LOGOUT = (By.XPATH, '//a[text()="Logout"]')

    # finding element - menu item
    def go_to_main_menu(self):
        try:
            # Wait for the element to be visible
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.MAIN))

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with main menu : {e}")

    # Check each menu item
    def check_all(self):
        # Unpack the tuple
        main_menu_elements = self.driver.find_elements(*self.MAIN)

        # for loop to get text of each element
        for element in main_menu_elements:
            # Get text and remove leading/trailing whitespaces
            text = element.text.strip()
            print(f"Menu items:  {text}   are present in Admin Page\n")

    # method for logging out
    def logout(self):
        try:
            # Wait for the element to be visible and click
            self.click_element(self.DROPDOWN)
            self.click_element(self.LOGOUT)
            print("Logged out successfully")

        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            print(f"Error waiting for or interacting with element in logout: {e}")
