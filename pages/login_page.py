from .base_page import BasePage
from .locators import LoginPageLocators, AdminnPageLocators, LkProfilePageLocators
from .input_data import RandomUserData
from selenium.common.exceptions import NoSuchElementException
import time

class LoginPage(BasePage):
    def login_with_phone(self,browser):
        # time.sleep(3)
        self.browser.find_element(*LoginPageLocators.POLE_PHONE).click()
        self.browser.find_element(*LoginPageLocators.POLE_PHONE).send_keys(*RandomUserData.phone)
        self.browser.find_element(*LoginPageLocators.BUTTON_SEND_KOD_SMS).click()
        self.browser.execute_script("window.open();")
        new_window = self.browser.window_handles[1]  # запоминаем название второй вкладки
        self.browser.switch_to.window(new_window)  # переключаемся на нее
        # time.sleep(5)

    def get_sms_kod(self,browser): # get kod sms with adminki
        self.browser.find_element(*AdminnPageLocators.POLE_LOGIN_ADMINKA).click()
        self.browser.find_element(*AdminnPageLocators.POLE_LOGIN_ADMINKA).send_keys("siradmin@admin.com")
        self.browser.find_element(*AdminnPageLocators.POLE_PASWORD_ADMINKA).click()
        self.browser.find_element(*AdminnPageLocators.POLE_PASWORD_ADMINKA).send_keys("qweqwe123")
        self.browser.find_element(*AdminnPageLocators.BUTTON_LOGIN_ADMINKA).click()
        kod = self.browser.find_element(*AdminnPageLocators.KOD_SMS_IN_ADMINKA).text
        print("kod = ",kod)
        self.browser.close()
        first_window = self.browser.window_handles[0]  # запоминаем название первой вкладки
        self.browser.switch_to.window(first_window)  # переключаемся на нее
        self.browser.find_element(*LoginPageLocators.POLE_KOD_SMS).click()
        self.browser.find_element(*LoginPageLocators.POLE_KOD_SMS).send_keys(kod)  #input kod sms
        # time.sleep(3)
        self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN_ON_PHONE).click()
        time.sleep(3)
        print("\n curent url1 = ", self.browser.current_url)
        assert "profile" or "dashbord" in self.browser.current_url, "user can`t entranse in cabinet"

    def fit_out_profile(self,browser): #заполняем профиль нового юзера
        try:
            self.browser.find_element(*LkProfilePageLocators.BUTTON).click()
        except:
            print("click on button is not work and it`s good")
        self.browser.find_element(*LkProfilePageLocators.POLE_NAME).click()
        self.browser.find_element(*LkProfilePageLocators.POLE_NAME).send_keys(*RandomUserData.name)
        self.browser.find_element(*LkProfilePageLocators.POLE_LAST_NAME).click()
        self.browser.find_element(*LkProfilePageLocators.POLE_LAST_NAME).send_keys(*RandomUserData.surname)
        self.browser.find_element(*LkProfilePageLocators.BUTTON).click()
        try:
            self.browser.find_element(*LkProfilePageLocators.SUCCESS_MESSAGE)
        except:
            print("Данные профиля не были сохранены либо нет уведомления об успешном сохранении")
        self.browser.find_element(*LkProfilePageLocators.LINK_AUTOCONTINUE_TERM_PAKET).click()
        order_window = self.browser.window_handles[1]  # запоминаем название третьей вкладки
        self.browser.switch_to.window(order_window)  # переключаемся на нее
        time.sleep(3)
        assert ".pdf" in self.browser.current_url, "link with order don`t open"