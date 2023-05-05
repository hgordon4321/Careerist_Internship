from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    # Chrome Setup
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(chrome_options=options)

    # Chrome mobile emulation setup
    mobile_emulation = {"deviceName": "Nexus 5"}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                      desired_capabilities=options.to_capabilities())


    # Firefox setup
    # options = webdriver.FirefoxOptions()
    # options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
    # options.add_argument('--headless')
    # context.driver = webdriver.Firefox(options=options)

#Browserstack setup
    # desired_cap = {
    #     'browser': 'chrome',
    #     'browser_version': '89',
    #     'os': 'Windows',
    #     'os_version': '10'
    #     #'name': test_name
    #
    # }
    # bs_user = 'henrygordon_TluWsD'
    # bs_key = 'Niypj57ZKysF2jWf5PG9'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
