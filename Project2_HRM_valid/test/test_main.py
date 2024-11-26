import pytest
from pages.login_page import LoginPage
from pages.main_page import MainMenu


# calling every method of main menu page and login page
@pytest.mark.usefixtures("setup")
class TestMainPage:
    def test_main(self):
        login_page = LoginPage(self.driver)
        main_menu = MainMenu(self.driver)

        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        main_menu.go_to_main_menu()
        main_menu.check_all()
        main_menu.logout()
