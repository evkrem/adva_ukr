from .base_page import BasePage
from .locators import LkPaketiLocators
from .input_data import TestUser, RandomUserData
import time

class OrderService(BasePage):
    def order_service(self,browser):
        self.browser.find_element(*LkPaketiLocators.ORDER_SERVICE).click()
        # self.browser.find_element(*LkPaketiLocators.CHOICE_SERVICE).click()
        self.browser.find_element(*LkPaketiLocators.CHOICE_SERVICE_IN_LIST).click()
        time.sleep(10)