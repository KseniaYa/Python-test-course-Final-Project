import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
product_links = [f"{base_link}/?promo=offer{i}" for i in [0, 1, 2, 3, 4, 5, 6, 8, 9]]
bugged_link = [pytest.param(f"{base_link}/?promo=offer7", marks=pytest.mark.xfail)]
product_links += bugged_link

@pytest.mark.skip
@pytest.mark.parametrize('product_link', product_links)
def test_guest_can_add_product_to_basket(browser, product_link):
    #product_link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_add_to_basket_success_product_name_is_correct()
    product_page.should_be_message_add_to_basket_success_product_cost_is_correct()
    
@pytest.mark.skip(raison = "Succes message is attended")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()
    
  
def test_guest_cant_see_success_message(browser):
    product_link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.skip  
def test_message_disappeared_after_adding_product_to_basket (browser):
    product_link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    product_link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
    
    
    
    
    