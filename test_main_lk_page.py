from .pages.main_lk_page import MainLkPage
from .pages.login_page import LoginPage
import pytest

class TestMainPageLk():
    def test_login_lk(self, browser):
        link = "https://dev.adva.org.ua/ru/login"
        page = LoginPage(browser, link)
        page.open()
        page.login_with_email(browser)

    def test_buy_paket_in_lk(self,browser):
        link = "https://dev.adva.org.ua/ua/cabinet/dashbord"
        page = MainLkPage(browser,link)
        page.open()
        page.pay_paket()

    def test_check_promocode(self,browser):
        link = "https://dev.adva.org.ua/ua/cabinet/dashbord"
        page = MainLkPage(browser,link)
        page.open()
        page.pay_paket()