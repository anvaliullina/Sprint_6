
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    project_dir = Path(__file__).resolve().parent.parent
    driver_path = project_dir / "geckodriver.exe"

    service = Service(
        executable_path=str(driver_path),
        log_output=str(project_dir / "geckodriver.log"),
        service_args=["--log", "debug"]
    )

    browser = webdriver.Firefox(service=service)
    browser.maximize_window()

    yield browser

    browser.quit()
