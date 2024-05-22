from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MagentoHomePage:
    MAIN_PAGE_URL = "https://magento.softwaretestingboard.com/"
    CONSENT_BUTTON = (By.XPATH, "//button[@aria-label='Consent']")
    WELCOME_MESSAGE = (By.CLASS_NAME, "logged-in")
    LOGO = (By.CLASS_NAME, "logo")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def load(self):
        self.browser.get(self.MAIN_PAGE_URL)
        #consent_cookie_button = self.browser.find_element(*self.CONSENT_BUTTON)
        #consent_cookie_button.click()

    def click_create_account(self):
        create_account_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(),'Create an Account')]")))
        create_account_button.click()

    def click_signin(self):
        signin_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Sign In')]")))
        signin_button.click()

    def get_welcome_message(self):
        welcome_text = self.browser.find_element(*self.WELCOME_MESSAGE).text
        return welcome_text

    def click_clothes_widgets(self, category):
        widget_xpath = "//a[@class='block-promo home-$category']"
        x = widget_xpath.replace("$category", category)
        self.browser.find_element(By.XPATH, x).click()

    def click_logo(self):
        self.browser.find_element(*self.LOGO).click()



