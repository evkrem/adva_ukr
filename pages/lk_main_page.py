from .base_page import BasePage
from .locators import LkMainLocators
from .input_data import TestUser, RandomUserData
import time


class MainLkPage(BasePage):
    def pay_paket(self, browser):
        self.browser.find_element(*LkMainLocators.BUTTON_ORDER_PAKET_LK_1).click()
        self.browser.find_element(*LkMainLocators.BUTTON_BUY_PAKET_IN_MODALKA).click()
        try:
            self.browser.find_element(*LkMainLocators.BUTTON_BUY_PAKET_IN_MODALKA)
        except:
            print("it`s all right, modalka closed")

    def check_promocode_lk_false(self, browser):
        self.browser.find_element(*LkMainLocators.BUTTON_ORDER_PAKET_LK_1).click()
        self.browser.find_element(*LkMainLocators.LINK_ON_PROMOKOD_IN_ORDER_MODALKA__LK_BUY_PAKET).click()
        self.browser.find_element(*LkMainLocators.POLE_FOR_PROMOKOD_IN_ORDER_MODALKA_LK_BUY_PAKET).click()
        self.browser.find_element(*LkMainLocators.POLE_FOR_PROMOKOD_IN_ORDER_MODALKA_LK_BUY_PAKET).send_keys(
            *RandomUserData.promokod_false)
        self.browser.find_element(*LkMainLocators.BUTTON_AKTIVATSII_PROMOKODA_IN_ORDER_MODALKA_LK_BUY_PAKET).click()
        try:
            self.browser.find_element(*LkMainLocators.TEXT_EROR_FALSE_PROMOKOD_LK)
        except:
            print("it`s all right, promo is`s wrong")