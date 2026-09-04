from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
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

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page() # Создаем страницу в новом контексте с данными авторизации из файла

    # Переходим на страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем видимость и текст заголовка "Courses"
    course_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_title).to_be_visible()
    expect(course_title).to_have_text("Courses")

    # Проверяем видимость иконки
    empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    # Проверяем видимость и текст блока "There is no results"
    empty_view_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title_text).to_be_visible()
    expect(empty_view_title_text).to_have_text("There is no results")

    # Проверяем видимость и текст блока "Results from the load test pipeline will be displayed here"
    empty_view_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description_text).to_be_visible()
    expect(empty_view_description_text).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )
