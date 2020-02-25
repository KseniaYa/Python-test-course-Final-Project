from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators, LoginPageLocators



def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_url(browser):
    link = LoginPageLocators.LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    
def test_guest_should_see_login_form(browser):
    link = LoginPageLocators.LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
def test_guest_should_see_register_form(browser):
    link = LoginPageLocators.LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
    