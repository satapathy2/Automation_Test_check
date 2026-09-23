from playwright.sync_api import Page,expect

class HomePage:
    def __init__(self,page:Page):
        self.page=page
        self.search_key_word=page.get_by_placeholder("Search Amazon")

    def home_page_validation(self):
        expect(self.search_key_word).to_be_visible(timeout=5000)
