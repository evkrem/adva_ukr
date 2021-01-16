from .pages.base_page import BasePage
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
import time
import pytest


class TestHeaderMenuOnMainPage():
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
    def test_logo_header(self,browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_oblasti_prava(browser)  # click on menu oblastiprava
        page.click_on_logo(browser) # click on logo "adva" on homepage

    # @pytest.mark.skip
    def test_buton_login_header(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.open_login_page(browser) # открываем страницу логина

    # @pytest.mark.run
    # @pytest.mark.skip
    def test_change_language_ua_to_ru_headder(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        # page.click_on_menu_oblasti_prava_footer(browser)  # click on menu oblastiprava
        page.change_language_ua_to_ru_header(browser)

    # @pytest.mark.skip
    def test_change_language_ru_to_ua_headder(self, browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        # page.click_on_menu_oblasti_prava_footer(browser)  # click on menu oblastiprava
        page.change_language_ru_to_ua_header(browser)

    def test_check_opened_allert_with_phone(self,browser):
        pass


    def test_open_google_play(self,browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.open_google_play(browser)

    # @pytest.mark.run
    def test_open_facebook(self,browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.open_facebook(browser)

    def test_open_instagram(self,browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.open_instagram(browser)

class TestFooterMenuOnMainPage():
    def test_open_menu_footer_glavnaya(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_oblasti_prava_footer(browser)  # click on menu oblastiprava
        page.click_on_menu_glavnaya_footer(browser)  # open glavnaya

    def test_open_menu_footer_oblasti_prava(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_oblasti_prava_footer(browser)  # click on menu oblastiprava

    def test_open_menu_footer_paketnie_uslugi(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_paketnie_uslugi_footer(browser)  #

    def test_open_menu_footer_blog(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_blog_footer(browser)  #

    def test_open_menu_footer_dokumenti(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_dokumenti_footer(browser)  # click on menu oblastiprava

    def test_logo_footer(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.click_on_menu_oblasti_prava_footer(browser)  # click on menu oblastiprava
        page.click_on_logo_footer(browser)  # click on logo "adva" on homepage

    def test_buton_login_footer(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.open_login_page_footer(browser)  # открываем страницу логина

    def test_change_language_ru_to_ua_footer(self, browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.change_language_ru_to_ua_footer(browser)

    # @pytest.mark.run
    def test_change_language_ua_to_ru_footer(self, browser):
        link = "https://dev.adva.org.ua/ua/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.change_language_ua_to_ru_footer(browser)

class TestOpenMessendgers():
    def test_open_telegram(self,browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.open_telegram(browser)

    def test_open_viber(self,browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.open_viber(browser)

@pytest.mark.skip
class TestPayOneService():
    def test_order_one_service(self,browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.pay_one_service(browser)

# @pytest.mark.xfail(reason="он и должен был упасть, т,к, был введен неправильный промокод")
class TestPayPaket():
    # @pytest.mark.skip(reason="этот тест просто пропускаем")
    def test_buy_paket1(self,browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.pay_paket(browser)

    @pytest.mark.xfail(reason="этот тест просто пропускаем")
    def test_check_promocode_false(self, browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.check_promocode_false(browser)

    @pytest.mark.run
    def test_check_promocode_true(self, browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.check_promocode_true(browser)

# @pytest.mark.run
class TestBlockOtzivi():
    def test_open_page_with_all_otzivi(self,browser):
        link = "https://dev.adva.org.ua/ru/home"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.open_page_all_otzivi(browser)


