from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class PantsPage:
    def __init__(self, browser):
        self.browser = browser

    def click_add_to_cart_product(self, product):
        product_name = product.lower().replace(' ', '-')
        product_xpath = "//a[@href='https://magento.softwaretestingboard.com/$product_name.html']"
        final_xpath = product_xpath.replace("$product_name",product_name)
        self.browser.find_element(By.XPATH, final_xpath).click()
