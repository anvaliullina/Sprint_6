"""Главная страница Яндекс Самоката."""

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    FAQ_QUESTION = "accordion__heading-{}"
    FAQ_ANSWER = "accordion__panel-{}"
    ORDER_TOP_BUTTON = (By.XPATH, "(//button[normalize-space()='Заказать'])[1]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "(//button[normalize-space()='Заказать'])[last()]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.open_url(self.URL)

    @allure.step("Открыть вопрос FAQ с индексом {index}")
    def click_question(self, index):
        locator = (By.ID, self.FAQ_QUESTION.format(index))
        self.scroll_and_click(locator)

    @allure.step("Прочитать ответ FAQ с индексом {index}")
    def get_answer_text(self, index):
        locator = (By.ID, self.FAQ_ANSWER.format(index))
        return self.get_text(locator)

    @allure.step("Нажать кнопку Заказать: {position}")
    def click_order_button(self, position):
        if position == "top":
            locator = self.ORDER_TOP_BUTTON
        elif position == "bottom":
            locator = self.ORDER_BOTTOM_BUTTON
        else:
            raise ValueError("position должен быть 'top' или 'bottom'")
        self.scroll_and_click(locator)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Убедиться, что открылась главная страница Самоката")
    def is_home_page_opened(self):
        return self.wait_for_url(self.URL)

    @allure.step("Нажать на логотип Яндекса и перейти в новую вкладку")
    def click_yandex_logo(self):
        previous_handles = self.get_window_handles()
        self.click(self.YANDEX_LOGO)
        self.switch_to_new_tab(previous_handles)

    @allure.step("Убедиться, что открылась страница Дзена")
    def is_dzen_opened(self):
        return self.wait_for_url_contains("dzen.ru")
