from .pages.lk_main_page import MainLkPage
from .pages.login_page import LoginPage
import pytest

class TestMainPageLk():
    def test_profile_login(self, browser):
        link = "https://dev.adva.org.ua/ru/login"
        page = LoginPage(browser, link)
        page.open()
        page.login_with_phone(browser)

        link = "https://admin.dev.advoservice.com.ua/login/?next=/confirmation/confirmationcode/"
        page2 = LoginPage(browser, link)
        page2.open()
        page2.get_sms_kod(browser)