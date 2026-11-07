
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage


class TestLogos:

    def test_scooter_logo_opens_home_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        # Переходим на страницу заказа
        main_page.click_order_button("top")

        # Нажимаем на логотип Самоката
        main_page.click_scooter_logo()

        # Проверяем возвращение на главную страницу
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == MainPage.URL.rstrip("/")
        )

        assert driver.current_url.rstrip("/") == MainPage.URL.rstrip("/")

    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        # Запоминаем первоначальную вкладку
        original_tab = driver.current_window_handle

        # Нажимаем на логотип Яндекса
        main_page.click_yandex_logo()

        # Ожидаем открытия новой вкладки
        WebDriverWait(driver, 15).until(
            lambda browser: len(browser.window_handles) == 2
        )

        # Переключаемся на новую вкладку
        new_tab = [
            tab for tab in driver.window_handles
            if tab != original_tab
        ][0]

        driver.switch_to.window(new_tab)

        # Проверяем переход на Дзен
        WebDriverWait(driver, 15).until(
            lambda browser: "dzen.ru" in browser.current_url
        )

        assert "dzen.ru" in driver.current_url
