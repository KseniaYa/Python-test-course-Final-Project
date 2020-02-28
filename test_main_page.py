from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import MainPageLocators


def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()

def test_guest_should_see_login_link(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_form(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()
    
def test_guest_should_see_register_form(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    register_page = LoginPage(browser, browser.current_url)
    register_page.should_be_register_form()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.should_be_message_basket_is_empty()
    