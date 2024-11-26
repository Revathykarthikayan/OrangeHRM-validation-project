import pytest
from pages.reset_pwd_page import ResetPage


# calling every method of reset page
@pytest.mark.usefixtures("setup")
class TestResetPage:
    def test_reset(self):
        reset_page = ResetPage(self.driver)

        reset_page.enter_username("Admin")
        reset_page.forgot_password()
        reset_page.username_password("Admin")
        reset_page.reset_password()
        reset_page.validate_confirmation()
