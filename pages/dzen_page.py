import allure

from pages.base_page import BasePage
from data import Url
from selenium.webdriver.common.by import By


class DzenPage(BasePage):
    dzen_logo = [By.XPATH, "//a[@aria-label='Логотип Бренда']"]  # Логотип Дзен

    @allure.step('Проверка, что текущая страница - Дзен')
    def check_dzen_page(self):
        assert self.get_current_url() == Url.DZEN_URL

    @allure.step('Ожидание появления логотипа Дзен')
    def wait_for_dzen_logo(self):
        self.wait_for_visibility_of_element(self.dzen_logo)