from .base_page import BasePage
from .locators import BlogPagesLocators
import time

class BlogPage(BasePage):
    def check_existence_articles(self,browser):
        print("\nvsego statey = ",len(self.browser.find_elements(*BlogPagesLocators.NAME_ARTICLE)))
        assert len(self.browser.find_elements(*BlogPagesLocators.NAME_ARTICLE)) > 1,"articles is not"

    def check_existence_img(self,browser):
        assert len(self.browser.find_elements(*BlogPagesLocators.IMG)) == len(self.browser.find_elements(
            *BlogPagesLocators.NAME_ARTICLE)),"number pictures isn`t equally number articles"
