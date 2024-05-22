import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.name_field, name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self, last_name):
        self.send_keys(OrderPageLocators.last_name_field, last_name)

    @allure.step('Заполнить поле "Адресс"')
    def set_adress(self, adress):
        self.send_keys(OrderPageLocators.adress_field, adress)

    @allure.step('Выбрать станцию "Сокольники"')
    def select_station_metro(self):
        self.click_on_element(OrderPageLocators.station_select)
        self.click_on_element(OrderPageLocators.sokolniki_station)

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.phone_field, phone)

    @allure.step('Клик по кнопке "Далее" в форме заказа "Для кого самокат"')
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.next_button)

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_form_for_whom(self, user):
        self.set_name(user[1])
        self.set_last_name(user[2])
        self.set_adress(user[3])
        self.select_station_metro()
        self.set_phone(user[4])
        self.click_next_button()

    @allure.step('Ожидание загрузки формы "Про аренду"')
    def wait_for_form_about_rent(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.date_field)

    @allure.step('Заполнить поле "Когда привезти самокат"')
    def set_date(self, date):
        self.send_keys(OrderPageLocators.date_field, date)
        self.click_on_element(OrderPageLocators.selected_delivery_day)

    @allure.step('Заполнить поле "Срок аренды"')
    def set_rental_period(self):
        self.click_on_element(OrderPageLocators.rental_period_field)
        self.click_on_element(OrderPageLocators.selected_rent_day)

    @allure.step('Выбрать черный цвет самоката')
    def select_color(self):
        self.click_on_element(OrderPageLocators.selected_black_color)

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.comment_field, comment)

    @allure.step('Клик по кнопке "Заказать" после заполнения формы')
    def click_on_order_button(self):
        self.click_on_element(OrderPageLocators.order_button)

    @allure.step('Заполнение формы "Про аренду"')
    def fill_form_about_rent(self, user):
        self.set_date(user[5])
        self.set_rental_period()
        self.select_color()
        self.set_comment(user[6])
        self.click_on_order_button()

    @allure.step('Клик по кнопке "Да" во всплывающем окне подтверждения заказа')
    def click_yes_button(self):
        self.click_on_element(OrderPageLocators.popup_yes_button)

    @allure.step('Получить текст во всплывающем окне подтверждения заказа')
    def get_text_order_popup(self):
        self.wait_for_visibility_of_element(OrderPageLocators.popup_order_status)
        return self.get_text(OrderPageLocators.popup_order_status)




