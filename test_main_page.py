from .pages.base_page import BasePage
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
import time
import pytest


class TestNewUserRegictrashion():
    def test_open_menu_header_glavnaya(self,browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_oblasti_prava(browser) # click on menu oblastiprava
        page.click_on_menu_glavnaya(browser)  # open glavnaya

    # @pytest.mark.skip
    def test_open_menu_header_oblasti_prava(self,browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_oblasti_prava(browser) # click on menu oblastiprava

    # @pytest.mark.skip
    def test_open_menu_header_paketnie_uslugi(self,browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_paketnie_uslugi(browser) #

    # @pytest.mark.skip
    def test_open_menu_header_blog(self,browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_blog(browser) #

    # @pytest.mark.skip
    def test_open_menu_header_dokumenti(self,browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_dokumenti(browser) # click on menu oblastiprava

    # @pytest.mark.skip
    def test_logo(self,browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_oblasti_prava(browser)  # click on menu oblastiprava
        page.click_on_logo(browser) # click on logo "adva" on homepage

    # @pytest.mark.skip
    def test_buton_login(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.open_login_page(browser) # открываем страницу логина




    @pytest.mark.skip
    def test_xxx(self, browser):
        pass


