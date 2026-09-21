from playwright.sync_api import Page,expect

class HomePage:
    def __init__(self,page:Page):
        self.page=page

    def homepagevalidation(self):
        expect(self.page.get_by_placeholder("Search Amazon")).to_be_visible(timeout=5000)
