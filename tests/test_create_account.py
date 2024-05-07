from pages.home_page import MagentoHomePage
from pages.create_account_page import CreateAccountPage
from pages.account_page import AccountPage
from faker import Faker


def test_create_account(browser):
    firstname = None
    lastname = None
    email = None
    password = None
    fake = Faker()
    for i in range(0, 10):
        firstname = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()
        password = fake.password()

    magento_home_page = MagentoHomePage(browser)
    create_account_page = CreateAccountPage(browser)
    account_page = AccountPage(browser)

    magento_home_page.load()
    magento_home_page.click_create_account()
    create_account_page.fill_account_info_fields(firstname, lastname, email, password)
    assert firstname, lastname in account_page.get_welcome_message()
    assert account_page.thank_you_registering_message() == "Thank you for registering with Main Website Store."

