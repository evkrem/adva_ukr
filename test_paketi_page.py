import pytest
from .pages.base_page import BasePage
from .pages.paketi_page import PaketsPage

class TestCampartNamePaketsOnMenuWithPaket():
    def test_campart_names_paket_menu_with_paket(self,browser):
        link = "https://dev.adva.org.ua/ru/packages#test_package"
        page = PaketsPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.campare_names_paket1(browser)
        page.campare_names_paket2(browser)
        page.campare_names_paket3(browser)
        page.campare_names_paket4(browser)
        page.campare_names_paket5(browser)
        page.campare_names_paket6(browser)

    @pytest.mark.run
    def test_check_open_modal_buy(self,browser):
        link = "https://dev.adva.org.ua/ru/packages#test_package"
        page = PaketsPage(browser,
                          link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.check_opening_modal_buy(browser)