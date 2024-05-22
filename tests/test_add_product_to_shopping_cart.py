import time

from pages.home_page import MagentoHomePage
from pages.pants_page import PantsPage
from pages.product_page import ProductsPage


def test_homepage_widgets(browser):
    YOGA_CATEGORY = "pants"
    PORTIA_PANTS = "Portia Capri"
    COLOR = "Blue"
    SIZE = "28"

    home_page = MagentoHomePage(browser)
    pants_page = PantsPage(browser)
    product_page = ProductsPage(browser)

    home_page.load()
    home_page.click_clothes_widgets(YOGA_CATEGORY)
    pants_page.click_add_to_cart_product(PORTIA_PANTS)
    product_page.click_size_and_color(SIZE, COLOR)
    assert PORTIA_PANTS in product_page.get_you_added_product_message()
    assert product_page.get_cart_number_products() == 1
