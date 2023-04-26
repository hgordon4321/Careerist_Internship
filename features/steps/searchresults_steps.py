from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User navigates to search results from url')
def open_results(context):
    context.app.results_page.open_results()

@then('Verify the first product has a name, image, and price')
def check(context):
    context.first_item = context.app.results_page.check_first_prod()
