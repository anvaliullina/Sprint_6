"""Общие методы Selenium для всех Page Object."""

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент на странице")
    def find(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Нажать на элемент")
    def click(self, locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Прокрутить страницу до элемента и нажать на него")
    def scroll_and_click(self, locator):
        element = self.find(locator)
        element.location_once_scrolled_into_view
        self.click(locator)

    @allure.step("Заполнить поле текстом")
    def type_text(self, locator, text):
        self.find(locator).send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        ).text

    @allure.step("Проверить переход на страницу {url}")
    def wait_for_url(self, url):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            lambda browser: browser.current_url.rstrip("/") == url.rstrip("/")
        )

    @allure.step("Получить список открытых вкладок")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self, previous_handles):
        WebDriverWait(self.driver, 15).until(
            lambda browser: len(browser.window_handles) > len(previous_handles)
        )
        new_handles = set(self.driver.window_handles) - set(previous_handles)
        self.driver.switch_to.window(new_handles.pop())

    @allure.step("Проверить, что адрес содержит {text}")
    def wait_for_url_contains(self, text):
        return WebDriverWait(self.driver, 15).until(EC.url_contains(text))
