from selenium.webdriver.common.by import By

class BasePageLocators():
    LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages[style="visibility: visible;"]')
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

class MainPageLocators():
    LINK = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators():
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    INPUT_REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    INPUT_REGISTER_PASSWORD = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    CONFIRM_REGISTER_PASSWORD = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    CONFIRM_REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
                                 
class ProductPageLocators():
    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/fr/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_FORM = (By.CSS_SELECTOR, ".col-sm-6.product_main")
    ADD_TO_BASKET_FORM = (By.ID, "add_to_basket_form")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    ADD_PRODUCT_NAME_SUCCESS = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    ADD_PRODUCT_COST_SUCCESS = (By.CSS_SELECTOR, ".alert-info strong")

    