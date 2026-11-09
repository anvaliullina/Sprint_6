# Sprint_6 — UI-автотесты Яндекс Самоката

Автоматизированное UI-тестирование сервиса [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/) на Python с Selenium, pytest, Page Object Model (POM) и Allure.

## Структура проекта

- `pages/base_page.py` — общие действия с WebDriver (открытие URL, ожидания, клики, ввод, вкладки).
- `pages/main_page.py` — действия и локаторы главной страницы, вопросы FAQ и логотипы.
- `pages/order_page.py` — действия и локаторы формы заказа.
- `tests/conftest.py` — фикстура браузера Firefox.
- `tests/test_faq.py` — 8 проверок ответов FAQ.
- `tests/test_order.py` — 2 сценария успешного заказа с разными данными и кнопками.
- `tests/test_logos.py` — 2 проверки логотипов.
- `allure-results/` и `allure-report/` — результаты и HTML-отчёт (если добавлены в репозиторий).

## Установка

Требуются Python 3, Mozilla Firefox и доступ к тестовому стенду.

```bash
python -m pip install -r requirements.txt
```

По умолчанию Selenium Manager находит или скачивает geckodriver автоматически. Если автоматическая загрузка недоступна, можно установить geckodriver отдельно, добавить его в `PATH` либо задать переменную окружения `GECKODRIVER_PATH` с путём к исполняемому файлу. Сам драйвер **не хранится в репозитории**.

Пример для PowerShell (только если драйвер установлен вручную):

```powershell
$env:GECKODRIVER_PATH = "C:\tools\geckodriver.exe"
```

## Запуск тестов

```bash
python -m pytest tests -v
```

## Отчёт Allure

```bash
python -m pytest tests -v --alluredir=allure-results --clean-alluredir
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Всего 12 тест-кейсов. После изменений тесты следует перезапустить и обновить отчёт. **Ветки:** работа в `develop`, PR в `main` без слияния.
