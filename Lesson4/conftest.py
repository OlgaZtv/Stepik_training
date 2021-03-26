from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture(autouse=True)
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield [user_language, browser]
    print("n\quit browser...")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose language: en or fr")