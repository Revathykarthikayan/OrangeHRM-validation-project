import pytest
from pages.login_page import LoginPage
from pages.admin_page import Admin


# calling every method of admin page and login page
@pytest.mark.usefixtures("setup")
class TestAdminPage:
    def test_admin(self):
        login_page = LoginPage(self.driver)
        ad = Admin(self.driver)

        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        ad.go_to_admin()
        ad.user_management("User Management")
        ad.job("Job")
        ad.organisation("Organization")
        ad.more()
        ad.nationalities("Nationalities")
        ad.corporate_branding("Corporate Branding")
        ad.configuration("Configuration")
        ad.logout()
