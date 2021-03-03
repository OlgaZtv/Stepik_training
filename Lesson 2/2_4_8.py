import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link: str = "http://suninjuly.github.io/explicit_wait2.html"
    wd = webdriver.Chrome()
    wd.get(link)

    text = WebDriverWait(wd, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = wd.find_element_by_id("book").click()

    x = wd.find_element_by_id("input_value").text
    y = calc(x)

    y_element = wd.find_element_by_css_selector("#answer").send_keys(str(y))
    button2 = wd.find_element_by_id("solve").click()
    time.sleep(10)

finally:
    wd.quit()