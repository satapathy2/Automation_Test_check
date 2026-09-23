from playwright.sync_api import Page,expect
class Menupage:

 def __init__(self,page:Page):
     self.page=page
     self.menu_ele_vis=page.locator("#hmenu-content")
     self.sub_menu_ele=page.locator("#hmenu-content").locator("a")
     self.sub_menu_txt=page.locator(".category-section")


 def  menu_ele(self,menu_hed_txt):
      expect(self.menu_ele_vis.get_by_text(f"{menu_hed_txt}").nth(0)).to_be_visible()

 def  submenu_ele(self,sub_menu):
      expect(self.sub_menu_ele.filter(has_text=f"{sub_menu}").nth(0)).to_be_visible(timeout=5000)

 def  validate_submenu_txt(self,sub_menu_hed):
      expect(self.page.locator(".category-section").get_by_text(f"{sub_menu_hed}").nth(0)).to_be_visible()
     # expect(self.sub_menu_txt.get_by_text("Stream Music").nth(0)).to_be_visible()