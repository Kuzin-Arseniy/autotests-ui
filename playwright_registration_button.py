from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверяем, что кнопка "Registration" есть, но не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()
    expect(registration_button).to_be_disabled()

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

    # Проверяем, что кнопка "Registration" есть и она активна.
    # Кнопку нашли ранее, поэтому просто проверяем видимость и активность
    expect(registration_button).to_be_visible()
    expect(registration_button).not_to_be_disabled()
