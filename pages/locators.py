from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LINK = "http://selenium1py.pythonanywhere.com/"

class LoginPageLocators():
    LINK = "http://selenium1py.pythonanywhere.com/fr/accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    
