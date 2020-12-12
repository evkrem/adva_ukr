from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators



class MainPage(BasePage):
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