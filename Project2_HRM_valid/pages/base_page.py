from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # method for asserting the text of the web element
    def assert_text(self, locator, text, timeout=20):
        element = self.find_element(locator, timeout)
        actual_text = element.text
        expected_text = text

        assert actual_text == expected_text, f"Expected {text},but got {actual_text}"
        print(f'\n"{text}" header is displayed on the Admin page')

    # method for getting title of the page
    def get_title(self):
        title = self.driver.title
        print(f"Title of the page is : {title}")
