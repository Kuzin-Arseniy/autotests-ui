import pytest  # Импортируем pytest
from playwright.sync_api import Playwright, expect, \
Page  # Импортируем класс страницы, будем использовать его для аннотации типов


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

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()
    registration_email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(username_input).to_be_visible()
    username_input.fill("username")

    # Заполняем поле password
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()
    registration_password_input.fill("password")

    # Кликаем на кнопку "Registration"
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

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
    # После того как управление вернется в блок teardown, браузер автоматически закроется,
    # так как произойдет выход их контекста