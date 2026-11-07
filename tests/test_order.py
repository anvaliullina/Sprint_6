
from datetime import datetime, timedelta

import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize(
        "position, name, surname, address, metro, phone, rental, color, comment",
        [
            (
                "top",
                "Мария",
                "Иванова",
                "Москва, улица Ленина, 10",
                "Сокольники",
                "+79991112233",
                "сутки",
                "black",
                "Позвоните за час"
            ),
            (
                "bottom",
                "Анна",
                "Смирнова",
                "Москва, улица Лесная, 15",
                "Черкизовская",
                "+79991112244",
                "двое суток",
                "grey",
                "Позвоните за 15 минут"
            ),
        ],
        ids=["top_button", "bottom_button"]
    )
    def test_successful_order(
        self, driver, position, name, surname,
        address, metro, phone, rental, color, comment
    ):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button(position)

        order_page = OrderPage(driver)

        # Первая страница заказа
        order_page.fill_first_step(
            name, surname, address, metro, phone
        )
        order_page.click_next()

        # Дата доставки через три дня
        delivery_date = (
            datetime.now() + timedelta(days=3)
        ).strftime("%d.%m.%Y")

        # Вторая страница заказа
        order_page.fill_second_step(
            delivery_date, rental, color, comment
        )

        # Подтверждение заказа
        order_page.click_order()
        order_page.confirm_order()

        # Проверка успешного оформления
        message = order_page.get_success_message()
        assert "Заказ оформлен" in message
