from .base_page import BasePage
from .locators import PaketPageLocators, SafeModeLocators
import time

class PaketsPage(BasePage):
    def campare_names_paket1(self,browser):
        self.browser.find_element(*PaketPageLocators.PAKET1).click()
        assert (self.browser.find_element(*PaketPageLocators.PAKET_NAME1_ON_MENU).text).lower() in (
            self.browser.find_element(
            *PaketPageLocators.PAKET_NAME).text).lower(),"name pakets is different"

    def campare_names_paket2(self,browser):
        self.browser.find_element(*PaketPageLocators.PAKET2).click()
        assert (self.browser.find_element(*PaketPageLocators.PAKET_NAME2_ON_MENU).text).lower() in (
            self.browser.find_element(
            *PaketPageLocators.PAKET_NAME).text).lower(),"name pakets is different"

    def campare_names_paket3(self,browser):
        self.browser.find_element(*PaketPageLocators.PAKET3).click()
        assert (self.browser.find_element(*PaketPageLocators.PAKET_NAME3_ON_MENU).text).lower() in (
            self.browser.find_element(
            *PaketPageLocators.PAKET_NAME).text).lower(),"name pakets is different"

    def campare_names_paket4(self,browser):
        self.browser.find_element(*PaketPageLocators.PAKET4).click()
        assert (self.browser.find_element(*PaketPageLocators.PAKET_NAME4_ON_MENU).text).lower() in (
            self.browser.find_element(
            *PaketPageLocators.PAKET_NAME).text).lower(),"name pakets is different"

    def campare_names_paket5(self,browser):
        self.browser.find_element(*PaketPageLocators.PAKET5).click()
        assert (self.browser.find_element(*PaketPageLocators.PAKET_NAME5_ON_MENU).text).lower() in (
            self.browser.find_element(
            *PaketPageLocators.PAKET_NAME).text).lower(),"name pakets is different"

    def campare_names_paket6(self,browser):
        self.browser.find_element(*PaketPageLocators.PAKET6).click()
        assert (self.browser.find_element(*PaketPageLocators.PAKET_NAME6_ON_MENU).text).lower() in (
            self.browser.find_element(
            *PaketPageLocators.PAKET_NAME).text).lower(),"name pakets is different"

    def check_opening_modal_buy(self,browser):
        self.browser.find_element(*PaketPageLocators.BUTTON_ON_PAKET).click()
        assert self.browser.find_element(*PaketPageLocators.BUTTON_ON_MODAL_BUY_PAKET).get_attribute("disabled") is \
               not None, "button is not dissabled"
