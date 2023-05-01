from pages.base_page import Page
from selenium.webdriver.common.by import By
import time


class ResultsPage(Page):
    RESULT_CONTAINERS = (By.CSS_SELECTOR, 'li.grid__item')
    NAME = (By.CSS_SELECTOR, 'a.card-information__text')
    PICTURE = (By.CSS_SELECTOR, 'lazy-image.media')
    PRICE = (By.CSS_SELECTOR, 'div.price')

    def open_results(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def check_first_prod(self):
        first_item = self.find_elements(*self.RESULT_CONTAINERS)[0]
        name = first_item.find_element(*self.NAME)
        assert name is not None, 'Product name could not be located'
        print(name.text)
        # I am printing the title instead of just locating it to verify the correct product is identified
        # I checked changing the index for "first_item" and the printed name always matched the product
        # corresponding to the index, so I am confident my code is finding the name/picture/price within the first
        # product container, not just finding the first name/picture/price on the page

        picture = first_item.find_element(*self.PICTURE)
        assert picture is not None, 'Product picture could not be located'

        price = first_item.find_element(*self.PRICE)
        assert price is not None, 'Product price could not be located'
