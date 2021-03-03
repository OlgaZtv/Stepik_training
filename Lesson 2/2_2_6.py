import time
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link: str = "http://SunInJuly.github.io/execute_script.html"
    wd = webdriver.Chrome()
    wd.get(link)

    x = wd.find_element_by_id("input_value").text
    y = calc(x)

    y_element = wd.find_element_by_css_selector("#answer")
    y_element.send_keys(str(y))

    wd.execute_script("window.scrollBy(0, 100);")

    option1 = wd.find_element_by_id("robotCheckbox").click()
    option2 = wd.find_element_by_id("robotsRule").click()

    button = wd.find_element_by_xpath("//button[contains(text(), 'Submit')]").click()
    time.sleep(5)

finally:
    wd.quit()
