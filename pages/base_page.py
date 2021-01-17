from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
import math
from selenium.webdriver.support.wait import WebDriverWait
from .locators import SafeModeLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.maximize_window()
        self.browser.get(self.url)
        try:
            self.browser.find_element(*SafeModeLocators.BUTTON_FOR_ENTRANCE_IN_SAFE_MODE).click()
            self.browser.find_element(*SafeModeLocators.BUTTON_FOR_ENTRANCE_ON_SITE).click()
        except NoSuchElementException:
            return