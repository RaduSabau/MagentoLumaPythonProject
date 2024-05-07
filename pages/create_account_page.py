from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CreateAccountPage:
    FIRSTNAME_FIELD = (By.ID, "firstname")
    LASTNAME_FIELD = (By.ID, "lastname")
    EMAIL_FIELD = (By.ID, "email_address")
    PASSWORD_FIELD = (By.ID, "password")
    PASSWORD_CONFIRMATION_FIELD = (By.ID, "password-confirmation")
    SUBMIT_CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[title='Create an Account']")

    def __init__(self, browser):
        self.browser = browser

    def fill_account_info_fields(self, firstname, lastname, email, password):
        self.browser.find_element(*self.FIRSTNAME_FIELD).send_keys(firstname)
        self.browser.find_element(*self.LASTNAME_FIELD).send_keys(lastname)
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*self.PASSWORD_CONFIRMATION_FIELD).send_keys(password)
        self.browser.find_element(*self.SUBMIT_CREATE_ACCOUNT_BUTTON).click()
