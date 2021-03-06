from selenium.webdriver.common.by import By
class SafeModeLocators():
    BUTTON_FOR_ENTRANCE_IN_SAFE_MODE = (By.ID,"details-button")
    BUTTON_FOR_ENTRANCE_ON_SITE = (By.ID,"proceed-link")

class MainPageLocators():
    CLICK_LOGIN_HEADER = (By.CSS_SELECTOR,".join.mr-md-4.mr-0.align-items-center")
    CLICK_LOGO_HEADER = (By.CSS_SELECTOR, ".brand.d-lg-block.d-none.col-md-2.col-3 img")
    MENU_HEADER_GLAVNAYA = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(1)")
    MENU_HEADER_OBLASTI_PRAVA = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(2)")
    MENU_HEADER_PAKETNIE_USLUGI = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(3)")
    MENU_HEADER_BLOG = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(4)")
    MENU_HEADER_DOCUMENTI = (By.CSS_SELECTOR,".main-menu.col-8.d-none.d-lg-block .menu-list li:nth-child(5)")
    HEADER_LANGUAGE_RU = (By.CSS_SELECTOR,".translate.d-flex :nth-child(1).ng-star-inserted")
    HEADER_LANGUAGE_UA = (By.CSS_SELECTOR,".translate.d-flex :nth-child(2).ng-star-inserted")
    HEADER_PHONE = (By.CSS_SELECTOR,".contact.d-lg-flex.d-none.w-100")

    CLICK_LOGIN_FOOTER = (By.CSS_SELECTOR,".login-wrapper.ng-star-inserted img")
    CLICK_LOGO_FOOTER = (By.ID, "logo-img")
    MENU_FOOTER_GLAVNAYA = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(1)")
    MENU_FOOTER_OBLASTI_PRAVA = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(2)")
    MENU_FOOTER_PAKETNIE_USLUGI = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(3)")
    MENU_FOOTER_BLOG = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(4)")
    MENU_FOOTER_DOCUMENTI = (By.CSS_SELECTOR,".menu-list.d-none.d-lg-flex li:nth-child(5)")
    FOOTER_LANGUAGE_RU = (By.CSS_SELECTOR,".translate.pt-5 button:nth-child(1)")
    FOOTER_LANGUAGE_UA = (By.CSS_SELECTOR,".translate.pt-5 button:nth-child(2)")
    FOOTER_GOOGLE_PLAY = (By.CSS_SELECTOR,".d-md-block .mobile-apps a:nth-child(1)")
    FOOTER_APP_STORY = (By.CSS_SELECTOR,".d-md-block .mobile-apps a:nth-child(2)")
    FOOTER_FACEBOOK = (By.CSS_SELECTOR,".social-net.pt-3 a:nth-child(1) img")
    FOOTER_INSTAGRAMM = (By.CSS_SELECTOR,".social-net.pt-3 a:nth-child(2) img")

    TELEGRAM = (By.CSS_SELECTOR,".flex-wrap div:nth-child(1).contact-item.d-flex a")
    VIBER = (By.CSS_SELECTOR,".flex-wrap div:nth-child(2).contact-item.d-flex a")
    WATSAP = (By.CSS_SELECTOR,".flex-wrap div:nth-child(4).contact-item.d-flex a")
    MESSENDGER = (By.CSS_SELECTOR,".flex-wrap div:nth-child(5).contact-item.d-flex a")
    PHONE = (By.CSS_SELECTOR,".flex-wrap div:nth-child(6).contact-item.d-flex a")
    EMAIL = (By.CSS_SELECTOR,"..flex-wrap div:nth-child(7).contact-item.d-md-flex a")

    ONE_USLUGA_1 = (By.CSS_SELECTOR, ".services-list li:nth-child(1) .radio-wrapper .radio-checked")
    ONE_USLUGA_2 = (By.CSS_SELECTOR, ".services-list li:nth-child(2) .radio-wrapper .radio-checked")
    ONE_USLUGA_3 = (By.CSS_SELECTOR, ".services-list li:nth-child(3) .radio-wrapper .radio-checked")

    CHOOSE_LEVEL_FREELANSERA_USLUGA2_FREE_1 = (By.CSS_SELECTOR,"#executor-level-list li:nth-child(1)")
    CHOOSE_LEVEL_FREELANSERA_USLUGA2_FREE_2 = (By.CSS_SELECTOR,"#executor-level-list li:nth-child(2)")
    CHOOSE_LEVEL_FREELANSERA_USLUGA2_FREE_3 = (By.CSS_SELECTOR,"#executor-level-list li:nth-child(3)")
    BUTTON_PAY_ONE_USLUGA = (By.CSS_SELECTOR, ".buy-btn-wrp button.btn-fb-green")

    POLE_PHONE_ON_ORDER_MODALKA = (By.ID,"userPhoneServiced")
    POLE_NAME_ON_ORDER_MODALKA = (By.CSS_SELECTOR,"#wnid_checkout_service .modal-content div:nth-child(2) div:nth-child(2) .form__input.ng-untouched.ng-pristine.ng-invalid")
    POLE_SURNAME_ON_ORDER_MODALKA = (By.CSS_SELECTOR,"#wnid_checkout_service .modal-content div:nth-child(2) div:nth-child(3) .form__input.ng-untouched.ng-pristine.ng-invalid")
    POLE_FOR_INPUT_QUESTION_ON_ORDER_MODALKA = (By.CSS_SELECTOR,"#wnid_checkout_service .modal-content div:nth-child(2) div:nth-child(4) .form__input.ng-untouched.ng-pristine.ng-invalid")
    BUTTON_ON_ORDER_MODALKA = (By.ID,"btid_checkout")

    BUTTON_ORDER_PAKET1 = (By.CSS_SELECTOR,".packages.ng-star-inserted .row div:nth-child(1) .row button")
    BUTTON_ORDER_PAKET2 = (By.CSS_SELECTOR,".packages.ng-star-inserted .row div:nth-child(2) .row button")
    BUTTON_ORDER_PAKET3 = (By.CSS_SELECTOR,".packages.ng-star-inserted .row div:nth-child(3) .row button")
    BUTTON_ORDER_PAKET4 = (By.CSS_SELECTOR,".packages.ng-star-inserted .row div:nth-child(4) .row button")
    BUTTON_ORDER_PAKET5 = (By.CSS_SELECTOR,".packages.ng-star-inserted .row div:nth-child(5) .row button")
    BUTTON_ORDER_PAKET6 = (By.CSS_SELECTOR,".packages.ng-star-inserted .row div:nth-child(6) .row button")


    POLE_PHONE_ON_ORDER_MODALKA_BUY_PAKET = (By.CSS_SELECTOR,"input#userPhonePackage")
    TEMP_HHH = (By.CSS_SELECTOR,"#wnidCheckout .modal-header.flex-wrap.justify-content-center.text-center")

    POLE_NAME_ON_ORDER_MODALKA_BUY_PAKET = (By.CSS_SELECTOR,"app-packages input#userFirstName")
    POLE_SURNAME_ON_ORDER_MODALKA_BUY_PAKET = (By.CSS_SELECTOR,"app-packages input#userLastName")
    LINK_ON_PROMOKOD_IN_ORDER_MODALKA_BUY_PAKET = (By.CSS_SELECTOR,"app-packages a")
    POLE_FOR_PROMOKOD_IN_ORDER_MODALKA_BUY_PAKET = (By.CSS_SELECTOR,"app-packages .form-group div div input")
    BUTTON_AKTIVATSII_PROMOKODA_IN_ORDER_MODALKA_BUY_PAKET = (By.CSS_SELECTOR,"app-packages .form-group div div button")
    TEXT_EROR_FALSE_PROMOKOD = (By.CSS_SELECTOR,"app-packages .form-group div div:nth-child(3)")
    BUTTON_PAY_ON_ORDER_MODALKA_BUY_PAKET = (By.CSS_SELECTOR,".packages.ng-star-inserted .modal-footer.pt-0 button")

    ALL_OTZIVI = (By.CSS_SELECTOR,"#reviev-wrapper a")

class OblastPravaPageLocators():
    OBLAST_PRAVA_1 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(1) button")
    OBLAST_PRAVA_2 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(2) button")
    OBLAST_PRAVA_3 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(3) button")
    OBLAST_PRAVA_4 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(4) button")
    OBLAST_PRAVA_5 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(5) button")
    OBLAST_PRAVA_6 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(6) button")
    OBLAST_PRAVA_7 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(7) button")
    OBLAST_PRAVA_8 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(8) button")
    OBLAST_PRAVA_9 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(9) button")
    OBLAST_PRAVA_10 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(10) button")
    OBLAST_PRAVA_11 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(11) button")
    OBLAST_PRAVA_12 =(By.CSS_SELECTOR,".laws-wrapper.row .col-md-3 ul li:nth-child(12) button")

    ARTICLE_1_IN_OBLASTI_PRAVO = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li:nth-child(1) button")
    ARTICLE_2_IN_OBLASTI_PRAVO = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li:nth-child(2) button")
    ARTICLE_3_IN_OBLASTI_PRAVO = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li:nth-child(3) button")
    ARTICLE_4_IN_OBLASTI_PRAVO = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li:nth-child(4) button")
    ARTICLE_5_IN_OBLASTI_PRAVO = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li:nth-child(5) button")
    ARTICLE_6_IN_OBLASTI_PRAVO = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li:nth-child(6) button")
    ARTICLE_7_IN_OBLASTI_PRAVO = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li:nth-child(7) button")
    ARTICLE_8_IN_OBLASTI_PRAVO = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li:nth-child(8) button")
    ARTICLE_9_IN_OBLASTI_PRAVO = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li:nth-child(9) button")

    FOR_COUNT_ARTICLES_IN_OBLASTI_PRAVA = (By.CSS_SELECTOR,".laws-wrapper.row .col-3 ul li  button")
    NAME_ARTICLE = (By.CSS_SELECTOR,"#anch h3")

class PaketPageLocators():
    PAKET1 = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(1) div")
    PAKET2 = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(2) div")
    PAKET3 = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(3) div")
    PAKET4 = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(4) div")
    PAKET5 = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(5) div")
    PAKET6 = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(6) div")

    BUTTON_ON_PAKET = (By.CSS_SELECTOR,".packages-info button")
    BUTTON_ON_MODAL_BUY_PAKET = (By.ID,"btid_checkout")

    PAKET_NAME = (By.CSS_SELECTOR,".packages-info .service-title")
    PAKET_NAME1_ON_MENU = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(1) span span")
    PAKET_NAME2_ON_MENU = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(2) span span")
    PAKET_NAME3_ON_MENU = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(3) span span")
    PAKET_NAME4_ON_MENU = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(4) span span")
    PAKET_NAME5_ON_MENU = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(5) span span")
    PAKET_NAME6_ON_MENU = (By.CSS_SELECTOR,".desctop-tabs.ng-star-inserted li:nth-child(6) span span")

class BlogPagesLocators():
    NAME_ARTICLE = (By.CSS_SELECTOR,".container.blogs  button")
    IMG = (By.CSS_SELECTOR,".container.blogs  img")

class LoginPageLocators():
    LOGIN_PHONE = (By.CSS_SELECTOR,".authorization nav:nth-child(1) div:nth-child(1)")
    POLE_PHONE = (By.CSS_SELECTOR, "form .ng-untouched.ng-pristine.ng-invalid")
    POLE_KOD_SMS = (By.ID, "userCode")
    BUTTON_SEND_KOD_SMS = (By.ID, "get-otp")
    BUTTON_LOGIN_ON_PHONE = (By.CSS_SELECTOR, ".login-wrapper .ml-2")

    LOGIN_SERTIFICAT = (By.CSS_SELECTOR,".authorization nav:nth-child(1) div:nth-child(2)")
    POLE_SERTIFICAT = (By.CSS_SELECTOR,"input[placeholder='сертификат']")
    POLE_PASWORD_ON_SERTIFICAT_AND_EMAIL = (By.CSS_SELECTOR,"input[placeholder='пароль']")
    BUTTON_LOGIN_ON_SERTIFICAT_AND_EMAIL_AND_SENG_PASSWORD_FOR_RESET = (By.CSS_SELECTOR,".login-wrapper button")

    LOGIN_EMAIL = (By.CSS_SELECTOR,".authorization nav:nth-child(1) div:nth-child(3)")
    POLE_EMAIL = (By.CSS_SELECTOR,"input[placeholder='email']")
    FORGOT_PASWORD = (By.CSS_SELECTOR,".authorization .reset-pass")
    POLE_FOR_INPUT_RESET_EMAIL = (By.CSS_SELECTOR,"input[placeholder='Введите емейл']")

class AdminnPageLocators():
    POLE_LOGIN_ADMINKA = (By.ID,"id_username")
    POLE_PASWORD_ADMINKA = (By.ID,"id_password")
    BUTTON_LOGIN_ADMINKA = (By.CSS_SELECTOR,".submit-row input")
    KOD_SMS_IN_ADMINKA = (By.CSS_SELECTOR,"#result_list .row1 .field-code")

class LkProfilePageLocators():
    POLE_NAME = (By.CSS_SELECTOR,"input[formcontrolname='userFirstName']")
    POLE_LAST_NAME = (By.CSS_SELECTOR,"input[formcontrolname='userLastName']")
    POLE_CITY = (By.CSS_SELECTOR,"input[formcontrolname='userLocality']")
    ERROR_MESSAGE_CITY = (By.CSS_SELECTOR,"form div:nth-child(2)  span:nth-child(2) small")
    POLE_ADRES = (By.CSS_SELECTOR,"input[formcontrolname='userAddress']")
    ERROR_MESSAGE_ADRES = (By.CSS_SELECTOR,"form div:nth-child(2)  span:nth-child(4) small")
    POLE_EMAIL = (By.CSS_SELECTOR,"input[formcontrolname='userEmail']")
    ERROR_EMAIL = (By.CSS_SELECTOR,"form section span:nth-child(2) small")
    POLE_PASWORD1 = (By.CSS_SELECTOR,"form section input:nth-child(3)")
    POLE_PASWORD2 = (By.CSS_SELECTOR,"form section input:nth-child(5)")
    ERROR_DIFFERENT_PASSWORD = (By.CSS_SELECTOR, "form section span:nth-child(6) small")
    LINK_AUTOCONTINUE_TERM_PAKET = (By.CSS_SELECTOR,"div label a")
    BUTTON = (By.CSS_SELECTOR,".buttons-wrapper.w-100 button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".success-massage")

class LkMenuLocators():
    GOLOVNA = (By.CSS_SELECTOR,".menu-list li:nth-child(1)")
    ZAYAVKI = (By.CSS_SELECTOR,".menu-list li:nth-child(2)")
    PAKETI = (By.CSS_SELECTOR,".menu-list li:nth-child(3)")
    DOKUMENTI = (By.CSS_SELECTOR,".menu-list li:nth-child(4)")
    PROFILE = (By.CSS_SELECTOR,".menu-list li:nth-child(5)")

class LkMainLocators():
    BUTTON_ORDER_PAKET_LK_1 = (By.CSS_SELECTOR,".packages .ng-star-inserted .row div:nth-child(2) button")
    BUTTON_BUY_PAKET_IN_MODALKA = (By.CSS_SELECTOR,".wrapp-modal button.btn.btn-success")
    LINK_ON_PROMOKOD_IN_ORDER_MODALKA__LK_BUY_PAKET = (By.CSS_SELECTOR,".wrapp-modal .a-promo")
    POLE_FOR_PROMOKOD_IN_ORDER_MODALKA_LK_BUY_PAKET = (By.CSS_SELECTOR,".wrapp-modal input")
    BUTTON_AKTIVATSII_PROMOKODA_IN_ORDER_MODALKA_LK_BUY_PAKET = (By.CSS_SELECTOR,".wrapp-modal button.btn.btn-info")
    TEXT_EROR_FALSE_PROMOKOD_LK = (By.CSS_SELECTOR,".wrapp-modal .promo-error")

class LkPaketiLocators():
    ORDER_SERVICE = (By.ID,"btn-open-dialog")
    CHOICE_SERVICE = (By.CSS_SELECTOR, "app-auth-modal select")
    CHOICE_SERVICE_IN_LIST = (By.TAG_NAME, "app-auth-modal select option")

