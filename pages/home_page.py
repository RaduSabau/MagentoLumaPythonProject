from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MagentoHomePage:
    MAIN_PAGE_URL = "https://magento.softwaretestingboard.com/"
    CONSENT_BUTTON = (By.XPATH, "//button[@aria-label='Consent']")
    CREATE_ACCOUNT_BUTTON = (By.LINK_TEXT, "https://magento.softwaretestingboard.com/customer/account/create/")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def load(self):
        self.browser.get(self.MAIN_PAGE_URL)
        consent_cookie_button = self.browser.find_element(*self.CONSENT_BUTTON)
        consent_cookie_button.click()

    def click_create_account(self):
        create_account_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(),'Create an Account')]")))
        create_account_button.click()
