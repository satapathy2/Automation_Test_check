from playwright.sync_api import Page,expect

class Navigationpage:
    def __init__(self,page:Page):
        self.page=page
        self.dismiss_but=page.get_by_role("button", name="Dismiss")
        self.all_menu_but=page.locator("#nav-main")
        self.menu_ele=page.locator("#hmenu-content").get_by_role("button")
        self.sub_menu_ele=page.locator("#hmenu-content").locator("a")
        self.search_cont=page.get_by_placeholder("Search Amazon")
        self.row_rcd=page.get_by_role("row")


    def home_page_navigation(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.dismiss_but.click()

    def all_page_navigation(self,menu):
        self.all_menu_but.get_by_role("button",name=f"{menu}").click()

    def all_menu_navigation(self,menu_opt):
        self.menu_ele.filter(has_text=f"{menu_opt}").click()

    def sub_menu_navigation(self,sub_menu):
        self.sub_menu_ele.filter(has_text=f"{sub_menu}").nth(1).click()

    def search_txt(self,search_txt):
        self.search_cont.fill(f"{search_txt}")

    def search_results_sel(self):
        self.row_rcd.nth(0).click()

