import time
from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, "https://demoqa.com/text-box")
    page.open()
