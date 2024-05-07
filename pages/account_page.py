from selenium.webdriver.common.by import By


class AccountPage:
    WELCOME_MESSAGE = (By.CLASS_NAME, "logged-in")
    THANK_YOU_MESSAGE = (By.XPATH, "//div[contains(text(),'Thank you for registering with Main Website Store.')]")

    def __init__(self, browser):
        self.browser = browser

    def get_welcome_message(self):
        welcome_text = self.browser.find_element(*self.WELCOME_MESSAGE).text
        return welcome_text

    def thank_you_registering_message(self):
        return self.browser.find_element(*self.THANK_YOU_MESSAGE).text
