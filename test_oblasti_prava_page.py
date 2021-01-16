import pytest
from .pages.base_page import BasePage
from .pages.oblasti_prava_page import OblastiPravaPage

class TestCheckContentArticles():
    @pytest.mark.run
    def test_campare_link_with_name_article(self, browser):
        link = "https://dev.adva.org.ua/ru/law-branches"
        page = OblastiPravaPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.campare_name_link1_with_name_article(browser)  # click on menu oblastiprava




