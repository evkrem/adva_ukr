from selenium.webdriver.common.by import By

class MainPageLocators():
    CLICK_LOGIN_HEADER = (By.CSS_SELECTOR,".join.mr-md-4.mr-0.align-items-center")
    CLICK_LOGO_HEADER = (By.CSS_SELECTOR, ".brand.d-lg-block.d-none.col-md-2.col-3 img")
    MENU_HEADER_GLAVNAYA = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(1)")
    MENU_HEADER_OBLASTI_PRAVA = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(2)")
    MENU_HEADER_PAKETNIE_USLUGI = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(3)")
    MENU_HEADER_BLOG = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(4)")
    MENU_HEADER_DOCUMENTI = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(5)")


    CLICK_LOGIN_FOOTER = (By.CSS_SELECTOR,".login-wrapper.ng-star-inserted img")
    CLICK_LOGO_FOOTER = (By.ID, "logo-img")
    MENU_FOOTER_GLAVNAYA = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(1)")
    MENU_FOOTER_OBLASTI_PRAVA = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(2)")
    MENU_FOOTER_PAKETNIE_USLUGI = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(3)")
    MENU_FOOTER_BLOG = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(4)")
    MENU_FOOTER_DOCUMENTI = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(5)")












    # BUTTON_ATTENT = (By.ID, "details-button")
    # OPEN_SITE = (By.ID, "proceed-link")
    # SEND_LOAN = (By.ID, "btid_send_loan")
    # # SEND_LOAN = (By.CSS_SELECTOR, "div:nth-child(3) > div.send-btn-mob.d-flex.d-md-none")
    # # SEND_LOAN = ('//body/div[2]/section[1]/section[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[3]/div[2]/span[1]')
    # # SEND_LOAN = ('/html[1]/body[1]/div[2]/section[1]/section[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[3]/div[1]/span[1]')
    # LINK_KREDITY = (By.CSS_SELECTOR, ".main-menu.w-100.d-flex.justify-content-around>li:nth-child(6) a")