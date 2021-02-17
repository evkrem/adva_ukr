from .pages.login_page import LoginPage

# from .pages.admin_page import AdminPage
from selenium.webdriver.common.keys import Keys

import pytest

class TestLoginPage():
    def test_profile_login(self, browser):
        link = "https://dev.adva.org.ua/ru/login"
        page = LoginPage(browser,link)
        page.open()
        page.login_with_phone(browser)

        link = "https://admin.dev.advoservice.com.ua/login/?next=/confirmation/confirmationcode/"
        page2 = LoginPage(browser,link)
        page2.open()
        page2.get_sms_kod(browser)

        link = "https://dev.adva.org.ua/ua/cabinet/profile"
        page3 = LoginPage(browser, link)
        page3.open()
        page3.fit_out_profile(browser)

