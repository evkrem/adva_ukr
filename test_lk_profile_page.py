from .pages.lk_profile_page import CheckChangeDataLkProfile
from .pages.login_page import LoginPage


class TestLkProfilePage():
    def test_login_in_lk(self, browser):
        link = "https://dev.adva.org.ua/ru/login"
        page = CheckChangeDataLkProfile(browser,link)
        page.open()
        page.login_in_lk(browser)

        link = "https://admin.dev.advoservice.com.ua/login/?next=/confirmation/confirmationcode/"
        page2 = LoginPage(browser, link)
        page2.open()
        page2.get_sms_kod(browser)

    def test_check_change_date_profile(self,browser):
        link = "https://dev.adva.org.ua/ua/cabinet/dashbord"
        page3 = CheckChangeDataLkProfile(browser, link)
        page3.open()
        page3.input_error_city(browser)
        page3.input_error_adress(browser)
        page3.input_error_email(browser)
        page3.input_different_password(browser)

