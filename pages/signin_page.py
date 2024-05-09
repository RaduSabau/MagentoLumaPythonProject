from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SignInPage:
    EMAIL_INPUT_FIELD = (By.ID, "email")
    PASSWORD_INPUT_FIELD = (By.ID, "pass")
    SIGNIN_BUTTON = (By.ID, "send2")

    def __init__(self, browser):
        self.browser = browser

    def fill_login_fields(self, email, password):
        self.browser.find_element(*self.EMAIL_INPUT_FIELD).send_keys(email)
        self.browser.find_element(*self.PASSWORD_INPUT_FIELD).send_keys(password)
        self.browser.find_element(*self.SIGNIN_BUTTON).click()



