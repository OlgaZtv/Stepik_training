from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


class TestItems():

    def test_item(self, browser):
        self.browser.get(link)
        button = len(browser.find_elements_by_css_selector("#add_to_basket_form > button"))
        assert button > 0, '!!!НЕ НАШЕЛ!!!'
