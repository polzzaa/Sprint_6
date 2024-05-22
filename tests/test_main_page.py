import allure
import pytest
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from data import AnswersList
from locators.main_page_locators import MainPageLocators

class TestMainPage:

    @allure.title('Проверка, что в выпадающем списке разедла "Вопросы о важном" открывается соответствующий текст')
    @allure.description('Ищем вопросы раздела "Вопросы о важном" > Клик на стрелку > Проверяем появление текста ответа')
    @pytest.mark.parametrize('button, answer, expected_text', [
        [MainPageLocators.question_button_1, MainPageLocators.answer_1, AnswersList.answer_text_1],
        [MainPageLocators.question_button_2, MainPageLocators.answer_2, AnswersList.answer_text_2],
        [MainPageLocators.question_button_3, MainPageLocators.answer_3, AnswersList.answer_text_3],
        [MainPageLocators.question_button_4, MainPageLocators.answer_4, AnswersList.answer_text_4],
        [MainPageLocators.question_button_5, MainPageLocators.answer_5, AnswersList.answer_text_5],
        [MainPageLocators.question_button_6, MainPageLocators.answer_6, AnswersList.answer_text_6],
        [MainPageLocators.question_button_7, MainPageLocators.answer_7, AnswersList.answer_text_7],
        [MainPageLocators.question_button_8, MainPageLocators.answer_8, AnswersList.answer_text_8]
                             ])
    def test_answer_text(self, driver, button, answer, expected_text):

        main_page = MainPage(driver)

        main_page.click_question_button(button)
        act_text = main_page.get_answer_text(answer)

        assert act_text == expected_text

    @allure.title('Тест перехода на страницу "Самокат"')
    @allure.description('Переходим на страницу заказа > Клик на лого "Самокат" > Переходим на главную страницу "Самокат"')
    def test_click_on_scooter_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        main_page.check_scooters_page_open()

    @allure.title('Тест перехода на страницу "Дзен"')
    @allure.description('Клик на лого "Яндекс" > Переходим на главную страницу "Дзен"')
    def test_click_on_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo()
        main_page.switch_to_window()

        dzen_page = DzenPage(driver)
        dzen_page.wait_for_dzen_logo()
        dzen_page.check_dzen_page()











