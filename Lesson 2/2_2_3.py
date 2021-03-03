import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

try:
    link: str = "http://suninjuly.github.io/selects1.html"
    wd = webdriver.Chrome()
    wd.get(link)

    x = wd.find_element_by_id("num1").text
    y = wd.find_element_by_id("num2").text
    num1 = int(x)
    num2 = int(y)
    sum_el = num1 + num2
    print(sum_el)
    sum_el2: str = str(sum_el)

    select = Select(wd.find_element_by_tag_name("select"))
    select.select_by_value(value=sum_el2)

    button = wd.find_element_by_xpath("//button[contains(text(), 'Submit')]").click()
    time.sleep(10)

finally:
    wd.quit()
