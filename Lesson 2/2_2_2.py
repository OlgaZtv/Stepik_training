from selenium import webdriver
import math
import time

def calc(x) -> object:
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link: str = "http://suninjuly.github.io/get_attribute.html"
    wd = webdriver.Chrome()
    wd.get(link)

    x = wd.find_element_by_tag_name('img').get_attribute("valuex")
    y = calc(x)
    print(y)
    y_element = wd.find_element_by_css_selector("#answer")
    y_element.send_keys(y)

    option1 = wd.find_element_by_id("robotCheckbox").click()
    option2 = wd.find_element_by_id("robotsRule").click()

    button = wd.find_element_by_xpath("//button[contains(text(), 'Submit')]").click()
    time.sleep(10)

finally:
    wd.quit()