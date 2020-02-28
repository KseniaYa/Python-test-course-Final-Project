"""
Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). 
Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.
Нажимаем на кнопку "Добавить в корзину".
*Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code(), 
который приведен ниже. Например, можете добавить его в класс BasePage, чтобы использовать его на любой странице. 
Этот метод нужен только для проверки того, что вы написали тест на Selenium. 
После этого вы получите код, который нужно ввести в качестве ответа на данное задание. 
Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. 
Не забудьте в конце теста добавить проверки на ожидаемый результат.
Ожидаемый результат: 

Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
Тест нужно написать, используя паттерн Page Object. Для этого вам нужно: 

-Добавить новый файл для тест-кейсов, связанных со страницей товара. Назовите файл с тестами test_product_page.py.
-Создать класс Page Object для страницы товара. Опишите его в файле product_page.py в папке pages.
Описать в нем метод для добавления в корзину.
Дописать методы-проверки.
Описать необходимые локаторы к элементам страницы.
Написать сам тест-кейс, используя все вышеописанное. Назовите тест test_guest_can_add_product_to_basket.
"""

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators

def test_guest_can_add_product_to_basket(browser):
    product_link = ProductPageLocators.PRODUCT_LINK
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    
    product_page.should_be_message_add_to_basket_success_product_name_is_correct()
    product_page.should_be_message_add_to_basket_success_product_cost_is_correct()
    
   
    
    
    
    
    
    
    