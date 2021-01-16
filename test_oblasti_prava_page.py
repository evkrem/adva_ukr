import pytest
from .pages.base_page import BasePage
from .pages.oblasti_prava_page import OblastiPravaPage

class TestCheckContentArticles():
    @pytest.mark.run
    def test_campare_link_with_name_article(self, browser):
        link = "https://dev.adva.org.ua/ru/law-branches"
        page = OblastiPravaPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.campare_name_link1_with_name_article(browser)
        page.campare_name_link2_with_name_article(browser)
        page.campare_name_link3_with_name_article(browser)
        page.campare_name_link4_with_name_article(browser)
        page.campare_name_link5_with_name_article(browser)
        page.campare_name_link6_with_name_article(browser)
        page.campare_name_link7_with_name_article(browser)
        page.campare_name_link8_with_name_article(browser)
        page.campare_name_link9_with_name_article(browser)
        page.campare_name_link10_with_name_article(browser)
        page.campare_name_link11_with_name_article(browser)
        page.campare_name_link12_with_name_article(browser)




