from playwright.sync_api import Page

def test_visit_admin_dashboard(page: Page):
    page.goto("/admin")