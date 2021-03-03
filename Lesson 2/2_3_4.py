import time
import math

from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link: str = "http://suninjuly.github.io/alert_accept.html"
    wd = webdriver.Chrome()
    wd.get(link)

    button = wd.find_element_by_tag_name("button").click()
    confirm = wd.switch_to.alert
    confirm.accept()

    x = wd.find_element_by_id("input_value").text
    y = calc(x)

    y_element = wd.find_element_by_css_selector("#answer").send_keys(str(y))
    button = wd.find_element_by_xpath("//button[contains(text(), 'Submit')]").click()

    time.sleep(10)

finally:
    wd.quit()