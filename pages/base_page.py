import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def check_element_displayed(self, locator):
        self.wait_for_visibility_of_element(*locator).is_displayed()

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


