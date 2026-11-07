
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_question(self, index):
        locator = (By.ID, f"accordion__heading-{index}")
        question = self.driver.find_element(*locator)
        question.location_once_scrolled_into_view

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_answer_text(self, index):
        locator = (By.ID, f"accordion__panel-{index}")

        answer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return answer.text

    def click_order_button(self, position):
        buttons = self.driver.find_elements(
            By.XPATH, "//button[normalize-space()='Заказать']"
        )

        if position == "top":
            button = buttons[0]
        else:
            button = buttons[-1]

        button.location_once_scrolled_into_view
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button)
        ).click()


    def click_scooter_logo(self):
        logo = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(logo)
        ).click()

    def click_yandex_logo(self):
        logo = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(logo)
        ).click()
