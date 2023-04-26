from pages.searchresults_page import ResultsPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.results_page = ResultsPage(self.driver)


