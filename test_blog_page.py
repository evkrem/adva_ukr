from .pages.base_page import BasePage
from .pages.blog_page import BlogPage
import pytest

class TestBlogPage():
    def test_check_existence_articles(self,browser):
        link = "https://dev.adva.org.ua/ru/blog"
        page = BlogPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.check_existence_articles(browser)

    def test_check_existence_img(self,browser):
        link = "https://dev.adva.org.ua/ru/blog"
        page = BlogPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.check_existence_img(browser)
