import pytest # Импортируем pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page  # Импортируем класс страницы, будем использовать его для аннотации типов
from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)


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

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state="browser-state.json"
    )
