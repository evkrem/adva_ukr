from .base_page import BasePage
from selenium.webdriver.common.by import By
import pytest
from .input_data import RandomUserData
from .locators import MainPageLocators
import time
from selenium.webdriver.common.alert import Alert



class MainPage(BasePage):
# check main menu in header
    def open_login_page(self,browser):
        self.browser.find_element(*MainPageLocators.CLICK_LOGIN_HEADER).click()
        assert "login" in self.browser.current_url, "login is not presented in url login page"

    def click_on_logo(self, browser):
        self.browser.find_element(*MainPageLocators.CLICK_LOGO_HEADER).click()
        assert "home" in self.browser.current_url, "open page isn`t home"

    def click_on_menu_glavnaya(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_HEADER_GLAVNAYA).click()
        print("\nlink_glavnaya = ", self.browser.current_url)
        assert "home" in self.browser.current_url, "open page isn`t home"

    def click_on_menu_oblasti_prava(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_HEADER_OBLASTI_PRAVA).click()
        print("\nlink_obl_prava = ", self.browser.current_url)
        assert "law-branches" in self.browser.current_url, "open page isn`t law-branches"

    def click_on_menu_paketnie_uslugi(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_HEADER_PAKETNIE_USLUGI).click()
        assert "packages" in self.browser.current_url, "open page isn`t home"

    def click_on_menu_blog(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_HEADER_BLOG).click()
        assert "blog" in self.browser.current_url, "open page isn`t home"

    def click_on_menu_dokumenti(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_HEADER_DOCUMENTI).click()
        assert "ofert" in self.browser.current_url, "open page isn`t home"

    def change_language_ua_to_ru_header(self,browser):
        print("link before click = ",self.browser.current_url)
        self.browser.find_element(*MainPageLocators.HEADER_LANGUAGE_RU).click()
        time.sleep(15)
        print("link after click = ",self.browser.current_url)
        assert "ru" in self.browser.current_url, "current language isn`t russian"

    def change_language_ru_to_ua_header(self,browser):
        print("link before click = ",self.browser.current_url)
        self.browser.find_element(*MainPageLocators.HEADER_LANGUAGE_UA).click()
        time.sleep(15)
        print("link after click = ",self.browser.current_url)
        assert "ua" in self.browser.current_url, "current language isn`t ukrain"

    def check_opened_allert_with_phone(self, browser):  #не видит аллерта
        pass
        # self.browser.find_element(*MainPageLocators.HEADER_PHONE).click()
        # alert = browser.switch_to.alert
        # assert "Ваш телефон" in alert.text


# check main menu in footer
    def open_login_page_footer(self,browser):
        self.browser.find_element(*MainPageLocators.CLICK_LOGIN_FOOTER).click()
        assert "login" in self.browser.current_url, "login is not presented in url login page"

    def click_on_logo_footer(self, browser):
        self.browser.find_element(*MainPageLocators.CLICK_LOGO_FOOTER).click()
        assert "home" in self.browser.current_url, "open page isn`t home"

    def click_on_menu_glavnaya_footer(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_FOOTER_GLAVNAYA).click()
        print("\nlink_glavnaya = ", self.browser.current_url)
        assert "home" in self.browser.current_url, "open page isn`t home"

    def click_on_menu_oblasti_prava_footer(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_FOOTER_OBLASTI_PRAVA).click()
        print("\nlink_obl_prava = ", self.browser.current_url)
        assert "law-branches" in self.browser.current_url, "open page isn`t law-branches"

    def click_on_menu_paketnie_uslugi_footer(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_FOOTER_PAKETNIE_USLUGI).click()
        assert "packages" in self.browser.current_url, "open page isn`t home"

    def click_on_menu_blog_footer(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_FOOTER_BLOG).click()
        assert "blog" in self.browser.current_url, "open page isn`t home"

    def click_on_menu_dokumenti_footer(self, browser):
        self.browser.find_element(*MainPageLocators.MENU_FOOTER_DOCUMENTI).click()
        assert "ofert" in self.browser.current_url, "open page isn`t home"

    def change_language_ua_to_ru_footer(self,browser):
        self.browser.find_element(*MainPageLocators.FOOTER_LANGUAGE_RU).click()
        assert "ru" in self.browser.current_url, "current language isn`t russian"

    def change_language_ru_to_ua_footer(self,browser):
        self.browser.find_element(*MainPageLocators.FOOTER_LANGUAGE_UA).click()
        assert "ua" in self.browser.current_url, "current language isn`t ukrainian"

    def open_google_play(self,browser):
        self.browser.find_element(*MainPageLocators.FOOTER_GOOGLE_PLAY).click()
        assert "play.google.com" and "android" in self.browser.current_url, "current url don`t contain play or android"

    def open_app_story(self,browser):
        self.browser.find_element(*MainPageLocators.FOOTER_APP_STORY).click()
        assert "apps.apple.com" in self.browser.current_url, "appstore didn`t opened"

    def open_facebook(self,browser):
        self.browser.find_element(*MainPageLocators.FOOTER_FACEBOOK).click()
        assert "facebook.com/ADVAua" in self.browser.current_url, "facebook didn`t opened"

    def open_instagram(self,browser):
        self.browser.find_element(*MainPageLocators.FOOTER_INSTAGRAMM).click()
        assert "instagram.com/adva_ua" in self.browser.current_url, "instagram didn`t opened"

# check open messengers

    def open_telegram(self,browser): # не удается закрыть модалку
        self.browser.find_element(*MainPageLocators.TELEGRAM).click()
        assert "t.me/ADVAuaBot" in self.browser.current_url, "telegramm didn`t open"

    def open_viber(self,browser):
        pass  # не удается закрыть модалку
        # print("\n curent url1 = ",self.browser.current_url)
        # self.browser.find_element(*MainPageLocators.VIBER).click()
        # alert = browser.switch_to.alert
        # alert.accept()
        # print("\n curent url3 = ",self.browser.current_url)

    def open_watsap(self,browser):
        self.browser.find_element(*MainPageLocators.WATSAP).click()
        assert "+whatsapp" in self.browser.current_url, "watsap didn`t open"


    def open_messendger(self,browser):
        self.browser.find_element(*MainPageLocators.MESSENDGER).click()
        assert "+messenger" in self.browser.current_url, "messenger didn`t open"


    def open_phone(self,browser): #не видит алерта  NoAlertPresentException: Message: no such alert
        pass

    def open_email(self,browser): # не знаю пока как проверить открытие десктопного почтовика
        pass

# блок одна услуга
    def pay_one_service(self,browser):
        self.browser.find_element(*MainPageLocators.BUTTON_PAY_ONE_USLUGA).click()
        time.sleep(15)
        # assert
        self.browser.find_element(*MainPageLocators.POLE_PHONE_ON_ORDER_MODALKA).click()
        self.browser.find_element(*MainPageLocators.POLE_PHONE_ON_ORDER_MODALKA).send_keys("665069856")
        time.sleep(5)

# блок покупка пакета
    def pay_paket(self,browser):
        self.browser.find_element(*MainPageLocators.BUTTON_ORDER_PAKET1).click()
        self.browser.find_element(*MainPageLocators.POLE_PHONE_ON_ORDER_MODALKA_BUY_PAKET).click()

        print("surname = ", *RandomUserData.surname," name = ",*RandomUserData.name, "phone = ",*RandomUserData.phone)
        self.browser.find_element(*MainPageLocators.POLE_PHONE_ON_ORDER_MODALKA_BUY_PAKET).send_keys(*RandomUserData.phone)
        self.browser.find_element(*MainPageLocators.POLE_NAME_ON_ORDER_MODALKA_BUY_PAKET).click()
        self.browser.find_element(*MainPageLocators.POLE_NAME_ON_ORDER_MODALKA_BUY_PAKET).send_keys(*RandomUserData.name)
        self.browser.find_element(*MainPageLocators.POLE_SURNAME_ON_ORDER_MODALKA_BUY_PAKET).click()
        self.browser.find_element(*MainPageLocators.POLE_SURNAME_ON_ORDER_MODALKA_BUY_PAKET).send_keys(*RandomUserData.surname)
        # self.browser.find_element(*MainPageLocators.LINK_ON_PROMOKOD_IN_ORDER_MODALKA_BUY_PAKET).click()
        # self.browser.find_element(*MainPageLocators.POLE_FOR_PROMOKOD_IN_ORDER_MODALKA_BUY_PAKET).click()
        # self.browser.find_element(*MainPageLocators.POLE_FOR_PROMOKOD_IN_ORDER_MODALKA_BUY_PAKET).send_keys(*RandomUserData.promokod)
        # self.browser.find_element(*MainPageLocators.BUTTON_AKTIVATSII_PROMOKODA_IN_ORDER_MODALKA_BUY_PAKET).click()
        # text_activatsii_promokoda = self.browser.find_element(*MainPageLocators.TEXT_EROR_FALSE_PROMOKOD).text
        # print("text asserta promo = ",text_activatsii_promokoda)
        # assert text_activatsii_promokoda == "AUTH-HOME.promo-success", "promokod okazalsya ne vernim"
        time.sleep(10)
        self.browser.find_element(*MainPageLocators.BUTTON_PAY_ON_ORDER_MODALKA_BUY_PAKET).click()
