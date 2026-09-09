from playwright.sync_api import expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    # Переходим на страницу курсов
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем видимость и текст заголовка "Courses"
    course_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_title).to_be_visible()
    expect(course_title).to_have_text("Courses")

    # Проверяем видимость иконки
    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    # Проверяем видимость и текст блока "There is no results"
    empty_view_title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title_text).to_be_visible()
    expect(empty_view_title_text).to_have_text("There is no results")

    # Проверяем видимость и текст блока "Results from the load test pipeline will be displayed here"
    empty_view_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description_text).to_be_visible()
    expect(empty_view_description_text).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )
