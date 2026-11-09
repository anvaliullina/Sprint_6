"""Форма оформления заказа самоката."""

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Далее']")

    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_TITLE = (By.XPATH, "//*[normalize-space()='Про аренду']")
    RENTAL_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']",
    )
    CONFIRM_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]//button[text()='Да']",
    )
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    @allure.step("Заполнить первую страницу заказа")
    def fill_first_step(self, name, surname, address, metro, phone):
        self.type_text(self.FIRST_NAME, name)
        self.type_text(self.LAST_NAME, surname)
        self.type_text(self.ADDRESS, address)
        self.type_text(self.METRO, metro)

        metro_option = (
            By.XPATH,
            f"//button[.//*[normalize-space()='{metro}']]",
        )
        self.click(metro_option)
        self.type_text(self.PHONE, phone)

    @allure.step("Перейти ко второй странице заказа")
    def click_next(self):
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнить вторую страницу заказа")
    def fill_second_step(self, date, rental_period, color, comment):
        self.type_text(self.DELIVERY_DATE, date)
        # Календарь перекрывает список аренды, если его не закрыть.
        self.click(self.RENTAL_TITLE)
        self.click(self.RENTAL_DROPDOWN)

        rental_option = (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-option') and text()='{rental_period}']",
        )
        self.click(rental_option)
        self.click((By.ID, color))
        self.type_text(self.COMMENT, comment)

    @allure.step("Нажать Заказать на второй странице")
    def click_order(self):
        self.click(self.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Получить сообщение об оформлении заказа")
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
