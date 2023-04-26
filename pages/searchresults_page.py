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

        try:
            print(first_item.find_element(*self.NAME).text)
            # I am printing the title instead of just locating it to verify the correct product is identified
            # I checked changing the index for "first_item" and the printed name always matched the product
            # corresponding to the index, so I am confident my code is finding the name/picture/price within the first
            # product container, not just finding the first name/picture/price on the page
        except:
            raise Exception('Product name could not be located')

        try:
            first_item.find_element(*self.PICTURE)
        except:
            raise Exception('Product picture could not be located')

        try:
            first_item.find_element(*self.PRICE)
        except:
            raise Exception('Product price could not be located')