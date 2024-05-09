import time

from pages.home_page import MagentoHomePage
from pages.signin_page import SignInPage


def test_sign_in_with_valid_credentials(browser):
    email = "peter@gmail.com"
    password = "P&E&T&E&R1234"
    firstname = "Peter"
    lastname = "Linch"

    home_page = MagentoHomePage(browser)
    signin = SignInPage(browser)

    home_page.load()
    home_page.click_signin()
    signin.fill_login_fields(email, password)
    assert firstname, lastname in home_page.get_welcome_message()
