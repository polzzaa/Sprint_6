import allure

from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import User


class TestOrderPage:

    @allure.title('Тест успешного оформления заказа через кнопку "Заказать" в хедере')
    @allure.description(
        'Клик на кнопку "Заказать" в хедере > Заполение форм "Для кого самокат" и "Про аренду" > Подтверждение заказа')
    def test_order_by_button_in_header(self, driver):
        main_page = MainPage(driver)
        main_page.accept_coockie()
        main_page.click_order_button_header()

        order_page = OrderPage(driver)
        order_page.fill_form_for_whom(User.user_1)
        order_page.wait_for_form_about_rent()
        order_page.fill_form_about_rent(User.user_1)
        order_page.click_yes_button()
        text = order_page.get_text_order_popup()
        assert 'Заказ оформлен' in text

    @allure.title('Тест успешного оформления заказа через нижнюю кнопку "Заказать" на главной странице')
    @allure.description(
        'Клик на нижнюю кнопку "Заказать" > Заполение форм "Для кого самокат" и "Про аренду" > Подтверждение заказа')
    def test_order_by_down_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_coockie()
        main_page.click_order_button_down()

        order_page = OrderPage(driver)
        order_page.fill_form_for_whom(User.user_2)
        order_page.wait_for_form_about_rent()
        order_page.fill_form_about_rent(User.user_2)
        order_page.click_yes_button()
        text = order_page.get_text_order_popup()
        assert 'Заказ оформлен' in text




