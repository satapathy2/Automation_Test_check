import json
import time

import pytest
from playwright.sync_api import Playwright,expect,Page

from menupage import Menupage
from podcast import Podcast
from productsearchpage import Productsearchpage
from homepage import HomePage
from navigationpage import Navigationpage

with open('AutomationAmazon/data.json') as json_data_file:
    test_data = json.load(json_data_file)
    data_ret=test_data['data']
    print(data_ret)

@pytest.mark.parametrize("extract_all_data",data_ret)
def test_basicwithplay(playwright:Playwright,browserInstance,extract_all_data):
    print(extract_all_data)

    homepage=HomePage(browserInstance)
    homepage.home_page_validation()
    nav_page=Navigationpage(browserInstance)
    nav_page.home_page_navigation()
    browserInstance.screenshot(path="amazonhomepage.png", full_page=True)

    nav_page.all_page_navigation(extract_all_data["menu"])
    all_menu_page=Menupage(browserInstance)
    all_menu_page.menu_ele(extract_all_data["menuHeaderTxt"])
    nav_page.all_menu_navigation(extract_all_data["menuOption"])
    #expect(browserInstance.locator(".category-section").get_by_text("Stream Music").nth(0)).to_be_visible()
    all_menu_page.validate_submenu_txt(extract_all_data["subMenuHeader"])
    all_menu_page.submenu_ele(extract_all_data["subMenu"])
    nav_page.sub_menu_navigation(extract_all_data["subMenu"])
    pod_cast_page=Podcast(browserInstance)
    pod_cast_page.verify_podcast()
    browserInstance.screenshot(path="amazonallmenupage.png", full_page=True)

    nav_page.search_txt(extract_all_data["searchTxt"])
    nav_page.search_results_sel()
    prd_search_page=Productsearchpage(browserInstance,extract_all_data["displayTxt"])
    prd_search_page.display_txt()
    browserInstance.screenshot(path="searchproductpage.png", full_page=True)

    time.sleep(10)
    print("pass")



