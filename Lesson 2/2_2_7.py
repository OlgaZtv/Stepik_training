import os
import time
from selenium import webdriver


try:
    link: str = "http://suninjuly.github.io/file_input.html"
    wd = webdriver.Chrome()
    wd.get(link)

    y_element = wd.find_element_by_name("firstname").send_keys("Ivan")
    x_element = wd.find_element_by_name("lastname").send_keys("Ivanov")
    z_element = wd.find_element_by_name("email").send_keys("test@test.ru")

    current_dir = os.path.abspath(os.path.dirname("D:/Teach/Stepik_local/"))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = wd.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)

    button = wd.find_element_by_xpath("//button[contains(text(), 'Submit')]").click()
    time.sleep(10)

finally:
    wd.quit()