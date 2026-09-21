from playwright.sync_api import Page,expect

class Navigationpage:
    def __init__(self,page:Page):
        self.page=page


    def homepagenavigation(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button", name="Dismiss").click()

