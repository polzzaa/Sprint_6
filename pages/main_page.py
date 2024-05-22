import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Url


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_question_button(self, button):
        self.scroll(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, answer):
        self.wait_for_visibility_of_element(answer)
        act_text = self.get_text(answer)
        return act_text

    @allure.step('Клик на кнопку "Заказать" в хедере')
    def click_order_button_header(self):
        self.click_on_element(MainPageLocators.order_button_header)

    @allure.step('Клик на нижнюю кнопку "Заказать"')
    def click_order_button_down(self):
        self.scroll(MainPageLocators.order_button_down)
        self.click_on_element(MainPageLocators.order_button_down)

    @allure.step('Принять куки во всплывающем окне')
    def accept_coockie(self):
        self.wait_for_visibility_of_element(MainPageLocators.accept_coockie)
        self.click_on_element(MainPageLocators.accept_coockie)

    @allure.step('Клик на кнопку "Самокат" в хедере')
    def click_on_scooter_button(self):
        self.click_on_element(MainPageLocators.scooter_button)

    @allure.step('Проверка открытия страницы Самокат при клике на кнопку Самокат')
    def check_scooters_page_open(self):
        self.click_on_scooter_button()
        self.wait_for_visibility_of_element(MainPageLocators.scooter_button)
        assert self.get_current_url() == Url.BASE_URL

    @allure.step('Клик на логотип "Яндекс"')
    def click_on_yandex_logo(self):
        self.click_on_element(MainPageLocators.yandex_button)













