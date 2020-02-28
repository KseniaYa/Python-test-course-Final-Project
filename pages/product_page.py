from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):  
    def add_to_basket(self):
        self.product_name, self.product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_FORM)\
                                                .text.split('\n')[0:2]
        add_to_basket_form = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        add_to_basket_form.click()
        
    def should_be_message_add_to_basket_success_product_name_is_correct(self):
        self.is_element_correct_message(*ProductPageLocators.ADD_PRODUCT_NAME_SUCCESS,self.product_name)
                                        
    def should_be_message_add_to_basket_success_product_cost_is_correct(self):
        self.is_element_correct_message(*ProductPageLocators.ADD_PRODUCT_COST_SUCCESS,self.product_cost)
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
                                            "Success message is presented, but should not be"
                                        
                                        
