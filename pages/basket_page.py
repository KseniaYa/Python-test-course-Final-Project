from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
                                            "Empty basket message is not presented"
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
                                            "Basket is not empty"


