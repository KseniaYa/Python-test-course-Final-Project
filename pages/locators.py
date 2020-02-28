from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LINK = "http://selenium1py.pythonanywhere.com/"

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    
class ProductPageLocators():
    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/fr/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_FORM = (By.CSS_SELECTOR, ".col-sm-6.product_main")
    ADD_TO_BASKET_FORM = (By.ID, "add_to_basket_form")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    ADD_PRODUCT_NAME_SUCCESS = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    ADD_PRODUCT_COST_SUCCESS = (By.CSS_SELECTOR, ".alert-info strong")

    