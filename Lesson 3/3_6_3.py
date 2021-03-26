import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestPage():

    @pytest.mark.parametrize('number', [str(i) for i in range(236895, 236906)])
    def test(self, browser, number):
        link = f"https://stepik.org/lesson/{number}/step/1"
        browser.get(link)
        answer = math.log(int(time.time() - 0.5))
        y = str(answer)
        browser.find_element_by_tag_name("textarea").send_keys(y)
        browser.find_element_by_css_selector(".submit-submission").click()
        x = browser.find_element_by_css_selector(".smart-hints__hint")
        time.sleep(10)
        print (x)



