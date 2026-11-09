"""Проверки переходов по логотипам в шапке сайта."""

import allure

from pages.main_page import MainPage


class TestLogos:
    @allure.title("Логотип Самоката возвращает на главную страницу")
    def test_scooter_logo_opens_home_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button("top")
        main_page.click_scooter_logo()

        assert main_page.is_home_page_opened()

    @allure.title("Логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()

        assert main_page.is_dzen_opened()
