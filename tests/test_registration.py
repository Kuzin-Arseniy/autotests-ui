from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    # Переходим на страницу регистрации
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    registration_email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()
    registration_email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    expect(username_input).to_be_visible()
    username_input.fill("username")

    # Заполняем поле password
    registration_password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()
    registration_password_input.fill("password")

    # Кликаем на кнопку "Registration"
    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Проверяем, что на странице "Dashboard" отображается заголовок "Dashboard"
    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")
