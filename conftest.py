import pytest
from _pytest import scope
from playwright.sync_api import Playwright

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser to be taken from command line"
    )
    parser.addoption(
        "--url_name", action="store", default="https://www.amazon.com/", help="url to be taken from command line"
    )


@pytest.fixture(scope="session")
def browserInstance(playwright,request):
    browser_name=request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        print(f"Error: '{browser_name}' is not a supported browser.")
        return

    context = browser.new_context()
    page = context.new_page()
    page.goto(url_name,wait_until="load")

    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def ret_data(request):
    return request.param



