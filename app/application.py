from pages.main_page import MainPage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage
from pages.product_group_page import ProductGroupPage
from pages.product_page import ProductPage
from pages.product_search_page import ProductSearchPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.prod_group_page = ProductGroupPage(self.driver)
        self.prod_page = ProductPage(self.driver)
        self.prod_search = ProductSearchPage(self.driver)

