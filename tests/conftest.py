"""Общая фикстура запуска Firefox."""

import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    # По умолчанию Selenium сам ищет драйвер в окружении.
    # GECKODRIVER_PATH нужен лишь там, где автоматическая загрузка недоступна.
    driver_path = os.getenv("GECKODRIVER_PATH")
    service = Service(executable_path=driver_path) if driver_path else Service()
    browser = webdriver.Firefox(service=service)
    try:
        browser.maximize_window()
        yield browser
    finally:
        browser.quit()
