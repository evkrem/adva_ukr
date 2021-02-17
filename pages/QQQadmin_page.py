from .base_page import BasePage
from .locators import AdminnPageLocators, LoginPageLocators
import time

class AdminPage(BasePage):
    def get_sms_kod(self,browser):
        self.browser.find_element(*AdminnPageLocators.POLE_LOGIN_ADMINKA).click()
        self.browser.find_element(*AdminnPageLocators.POLE_LOGIN_ADMINKA).send_keys("siradmin@admin.com")
        self.browser.find_element(*AdminnPageLocators.POLE_PASWORD_ADMINKA).click()
        self.browser.find_element(*AdminnPageLocators.POLE_PASWORD_ADMINKA).send_keys("qweqwe123")
        self.browser.find_element(*AdminnPageLocators.BUTTON_LOGIN_ADMINKA).click()
        kod = self.browser.find_element(*AdminnPageLocators.KOD_SMS_IN_ADMINKA).text
        print("kod = ",kod)
        first_window = self.browser.window_handles[0]  # запоминаем название первой вкладки
        self.browser.switch_to.window(first_window)  # переключаемся на нее
        time.sleep(3)
        self.browser.find_element(*LoginPageLocators.POLE_KOD_SMS).click()
        self.browser.find_element(*LoginPageLocators.POLE_KOD_SMS).send_keys(kod)
        time.sleep(3)
        self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN_ON_PHONE).click()
        time.sleep(3)