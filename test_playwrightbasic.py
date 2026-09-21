import time
from playwright.sync_api import Playwright,expect
from homepage import HomePage
from navigationpage import Navigationpage

def test_basicwithplay(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
   # browser = playwright.chromium.launch()
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.amazon.com/",wait_until="load")
   # page.on("dialog", lambda dialog: dialog.accept())
    #page.get_by_role("button", name="Dismiss").click()
    navigationpage=Navigationpage(page)
    navigationpage.homepagenavigation()
    homepage=HomePage(page)
    homepage.homepagevalidation()
    page.screenshot(path="amazonhomepage.png", full_page=True)


    #Click on All menu and verify the page having the text based on selection
    page.locator("#nav-main").get_by_role("button",name="All").click()
    expect(page.locator("#hmenu-content").get_by_text("Digital Content & Devices").nth(0)).to_be_visible()
    page.locator("#hmenu-content").get_by_role("button").filter(has_text="Amazon Music").click()
    expect(page.locator("#hmenu-content").locator("a").filter(has_text="Podcasts").nth(0)).to_be_visible(timeout=5000)
    page.locator("#hmenu-content").locator("a").filter(has_text="Podcasts").nth(1).click()
    expect(page.locator("#nav-subnav").get_by_role("link",name="Podcasts")).to_be_visible()
    page.screenshot(path="amazonallmenupage.png", full_page=True)

    #search teh product and validate the prodcut name
    page.get_by_placeholder("Search Amazon").fill("samsung phone")
    page.get_by_role("row").nth(0).click()
    expect(page.get_by_text("Check each product page for other buying options.")).to_be_visible(timeout=10000)
    expect(page.locator(".puisg-row").get_by_text("Samsung").nth(1)).to_be_visible()
    page.screenshot(path="searchproductpage.png", full_page=True)

    time.sleep(10)
    print("pass")
    browser.close()


