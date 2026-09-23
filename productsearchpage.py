from playwright.sync_api import expect,Page


class Productsearchpage:
    def __init__(self,page:Page,search_cont):
        self.page=page
        self.search_page_ele=page.get_by_text(f"{search_cont}")
        self.search_cont=page.locator(".puisg-row")

    def display_txt(self):
        expect(self.search_page_ele).to_be_visible(timeout=10000)
        expect(self.search_cont.get_by_text("Samsung").nth(1)).to_be_visible()
