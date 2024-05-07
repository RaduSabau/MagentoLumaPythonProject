from selenium.webdriver.common.by import By


class SignIn:
    EMAIL_INPUT_FIELD = (By.ID, "email")
    PASSWORD_INPUT_FIELD = (By.ID, "pass")
    SIGNIN_BUTTON = (By.ID, "send2")

    def __init__(self, browser):
        self.browser = browser

    def fill_login_fields(self):
        self.browser.find_element
