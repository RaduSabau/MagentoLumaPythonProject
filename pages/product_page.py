from selenium.webdriver.common.by import By


class ProductsPage:
    ADD_TO_CART_BUTTON = (By.ID, "product-addtocart-button")
    YOU_ADDED_PRODUCT_MESSAGE = (By.XPATH, "//div[contains(text(),'You added Portia Capri to your ')]")
    CART_NUMBER_OF_PRODUCTS = (By.CLASS_NAME, "counter-number")
    def __init__(self, browser):
        self.browser = browser

    def click_size_and_color(self, size, color):
        size_xpath = "//div[contains(text(),'$size')]"
        color_xpath = "//div[@aria-label='$color']"
        self.browser.find_element(By.XPATH, size_xpath.replace("$size", size)).click()
        self.browser.find_element(By.XPATH, color_xpath.replace("$color", color)).click()
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click()

    def get_you_added_product_message(self):
        return self.browser.find_element(*self.YOU_ADDED_PRODUCT_MESSAGE).text

    def get_cart_number_products(self):
        return int(self.browser.find_element(*self.CART_NUMBER_OF_PRODUCTS).text)
