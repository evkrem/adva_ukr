from .base_page import BasePage
from .locators import OblastPravaPageLocators
import time
from selenium.common.exceptions import NoSuchElementException

class OblastiPravaPage(BasePage):
    def campare_name_link1_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_1).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_1).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link2_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_2).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_2).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link3_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_3).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_3).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link4_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_4).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_4).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link5_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_5).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_5).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link6_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_6).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_6).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link7_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_7).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_7).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link8_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_8).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_8).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link9_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_9).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_9).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link10_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_10).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_10).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link11_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_11).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_11).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return

    def campare_name_link12_with_name_article(self,browser):
        self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_12).click()
        time.sleep(1)
        try:
            print(self.browser.find_element(*OblastPravaPageLocators.OBLAST_PRAVA_12).text, "=",
                  len(self.browser.find_elements(*OblastPravaPageLocators.FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA)),
                  " articles")

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_1_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_2_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_3_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_4_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_5_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_6_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_7_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_8_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

            self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).click()
            assert self.browser.find_element(*OblastPravaPageLocators.ARTICLE_9_IN_OBLASTI_PRAVO).text == \
                   self.browser.find_element(*OblastPravaPageLocators.NAME_ARTICLE).text, "link don`t contain a article name"

        except NoSuchElementException:
            return
