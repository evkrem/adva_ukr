from .pages.base_page import BasePage
from .pages.login_page import LoginPage
# from .pages.admin_page import AdminPage
from selenium.webdriver.common.keys import Keys

import pytest

class TestLoginPage():
    def test_check_existence_articles(self, browser):
        link = "https://dev.adva.org.ua/ru/login"
        page = LoginPage(browser,link)
        page.open()
        page.login_with_phone(browser)





        link = "https://admin.dev.advoservice.com.ua/login/?next=/confirmation/confirmationcode/"
        page2 = LoginPage(browser,link)
        page2.open()
        page2.get_sms_kod(browser)


