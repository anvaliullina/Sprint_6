
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:

    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Далее']")

    def __init__(self, driver):
        self.driver = driver

    def fill_first_step(self, name, surname, address, metro, phone):
        self.driver.find_element(*self.FIRST_NAME).send_keys(name)
        self.driver.find_element(*self.LAST_NAME).send_keys(surname)
        self.driver.find_element(*self.ADDRESS).send_keys(address)

        self.driver.find_element(*self.METRO).send_keys(metro)

        metro_option = (
            By.XPATH,
            f"//button[.//*[normalize-space()='{metro}']]"
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(metro_option)
        ).click()

        self.driver.find_element(*self.PHONE).send_keys(phone)

    def click_next(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        ).click()


    
    def fill_second_step(self, date, rental_period, color, comment):
        # Вводим дату доставки
        date_input = self.driver.find_element(
            By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
        )
        date_input.send_keys(date)

        # Закрываем календарь нажатием на заголовок
        self.driver.find_element(
            By.XPATH, "//*[normalize-space()='Про аренду']"
        ).click()

        # Открываем список сроков аренды
        self.driver.find_element(
            By.CLASS_NAME, "Dropdown-control"
        ).click()

        # Выбираем срок аренды
        rental_option = (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-option') and text()='{rental_period}']"
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(rental_option)
        ).click()

        # Выбираем цвет самоката
        self.driver.find_element(By.ID, color).click()

        # Заполняем комментарий для курьера
        self.driver.find_element(
            By.XPATH, "//input[@placeholder='Комментарий для курьера']"
        ).send_keys(comment)


    def click_order(self):
        order_button = (
            By.XPATH,
            "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(order_button)
        ).click()

    def confirm_order(self):
        confirm_button = (
            By.XPATH,
            "//div[contains(@class, 'Order_Modal')]//button[text()='Да']"
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(confirm_button)
        ).click()

    def get_success_message(self):
        success_message = (
            By.XPATH,
            "//div[contains(@class, 'Order_ModalHeader')]"
        )
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(success_message)
        ).text
