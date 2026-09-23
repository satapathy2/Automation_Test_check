from playwright.sync_api import Page,expect


class Podcast:
    def __init__(self,page:Page):
        self.page = page
        self.podcast_ele=page.locator("#nav-subnav").get_by_role("link", name="Podcasts")

    def verify_podcast(self):
        expect(self.podcast_ele).to_be_visible()