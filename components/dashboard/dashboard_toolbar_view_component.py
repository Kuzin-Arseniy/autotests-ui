import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = Text(page, 'dashboard-toolbar-title-text', 'Title')

    @allure.step('Check visible and text title at Dashboard toolbar')
    def check_visible(self):
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text("Dashboard")
