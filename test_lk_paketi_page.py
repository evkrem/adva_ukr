from .pages.lk_paketi_page import OrderService
from .pages.login_page import LoginPage

class TestOrderService():
    def test_login_lk(self, browser):
        link = "https://dev.adva.org.ua/ru/login"
        page = LoginPage(browser, link)
        page.open()
        page.login_with_email(browser)

    def test_order_service(self,browser):
        link = "https://dev.adva.org.ua/ua/cabinet/packages/active"
        page = OrderService(browser, link)
        page.open()
        page.order_service(browser)