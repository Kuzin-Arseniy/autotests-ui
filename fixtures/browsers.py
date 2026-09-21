import pytest  # Импортируем pytest
from playwright.sync_api import Playwright, expect, \
Page  # Импортируем класс страницы, будем использовать его для аннотации типов

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Ниже идет инициализация и открытие новой страницы.
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)

    # Передаем страницу для использования в тесте
    yield browser.new_page()

    # Закрываем браузер после выполнения тестов
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch() # Если явно не указывать, headless=True используется по умолчанию
    context = browser.new_context()  # Создание контекста
    page = context.new_page()  # Создание страницы

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()

    # Сохраняем состояние браузера
    context.storage_state(path="browser-state.json")

    # Закрываем браузер в текущем контексте
    browser.close()

@pytest.fixture # Область видимости "function" используется по умолчанию
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    # Блок setup. Создаем страницу в новом контексте с использованием browser-state.json (данные авторизации)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    yield context.new_page() # Передаем поток с готовым контекстом
    browser.close()
    # Закрываем браузер после каждого теста, так как браузер открывается внутри данной фикстуры для каждого теста.
    # У встроенной фикстуры playwright нет browser.close() + она имеет scope="session"