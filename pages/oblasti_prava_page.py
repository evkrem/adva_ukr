from .base_page import BasePage
from .locators import OblastPravaPageLocators
import time

class OblastiPravaPage(BasePage):
    def campare_name_link1_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_1).click()
        # link_name_article = self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text
        time.sleep(1)
        self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
        # name_article = self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text
        assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
               self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"




