from .base_page import BasePage
from .locators import LkProfilePageLocators, LoginPageLocators, LkMenuLocators
from .input_data import TestUser, RandomUserData
import time

class CheckChangeDataLkProfile(BasePage):
    def login_in_lk(self,browser):
        self.browser.find_element(*LoginPageLocators.POLE_PHONE).click()
        self.browser.find_element(*LoginPageLocators.POLE_PHONE).send_keys(*TestUser.user1)
        self.browser.find_element(*LoginPageLocators.BUTTON_SEND_KOD_SMS).click()
        self.browser.execute_script("window.open();")
        new_window = self.browser.window_handles[1]  # запоминаем название второй вкладки
        self.browser.switch_to.window(new_window)  # переключаемся на нее

    def input_error_city(self,browser):
        self.browser.find_element(*LkMenuLocators.PROFILE).click()
        self.browser.find_element(*LkProfilePageLocators.POLE_CITY).click()
        self.browser.find_element(*LkProfilePageLocators.POLE_CITY).send_keys("Kiev")
        try:
            self.browser.find_element(*LkProfilePageLocators.ERROR_MESSAGE_CITY)
        except:
            print("допустим ввод латиницы в поле город")
        self.browser.find_element(*LkProfilePageLocators.POLE_CITY).clear()
        self.browser.find_element(*LkProfilePageLocators.POLE_CITY).send_keys("Киев")

    def input_error_adress(self, browser):
        self.browser.find_element(*LkProfilePageLocators.POLE_ADRES).click()
        self.browser.find_element(*LkProfilePageLocators.POLE_ADRES).send_keys("street ")
        try:
            self.browser.find_element(*LkProfilePageLocators.ERROR_MESSAGE_ADRES)
        except:
            print("\nдопустим ввод латиницы в поле адрес")
        self.browser.find_element(*LkProfilePageLocators.POLE_ADRES).clear()
        self.browser.find_element(*LkProfilePageLocators.POLE_ADRES).send_keys("улица такая-то ")

    def input_error_email(self,browser):
        self.browser.find_element(*LkProfilePageLocators.POLE_EMAIL).click()
        self.browser.find_element(*LkProfilePageLocators.POLE_EMAIL).send_keys("lkjsdf")
        self.browser.find_element(*LkProfilePageLocators.POLE_ADRES).click()
        try:
            eror = self.browser.find_element(*LkProfilePageLocators.ERROR_EMAIL).text
            print("\neror email = ", eror)
        except:
            print("\nдопустим ввод емэйла в неправильном формате")
        self.browser.find_element(*LkProfilePageLocators.POLE_EMAIL).clear()
        em = RandomUserData.email
        print("\nemail = ",em)
        self.browser.find_element(*LkProfilePageLocators.POLE_EMAIL).send_keys(em)


    def input_different_password(self,browser):
        try:
            self.browser.find_element(*LkProfilePageLocators.POLE_PASWORD1).click()
            self.browser.find_element(*LkProfilePageLocators.POLE_PASWORD1).send_keys(123123)
            self.browser.find_element(*LkProfilePageLocators.POLE_PASWORD2).click()
            self.browser.find_element(*LkProfilePageLocators.POLE_PASWORD2).send_keys(321321)
            try:
                eror = self.browser.find_element(*LkProfilePageLocators.ERROR_DIFFERENT_PASSWORD).text
                print("\neror password = ", eror)
            except:
                print("\nнет уведомления о вводе разных паролей")
            self.browser.find_element(*LkProfilePageLocators.POLE_PASWORD2).clear()
            self.browser.find_element(*LkProfilePageLocators.POLE_PASWORD2).send_keys(123123)


        except:
            print("Юзер не новый, поэтому пароль проверить нельзя")
        self.browser.find_element(*LkProfilePageLocators.BUTTON).click()
        try:
            self.browser.find_element(*LkProfilePageLocators.SUCCESS_MESSAGE)
        except:
            print("Данные профиля не были сохранены либо нет уведомления об успешном сохранении")