from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random


class CheckBoxPage(BasePage):

    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@aria-label='Expand all']")
    ITEM_LIST = (By.XPATH, "//span[@class='rct-title']")
    CHECKED_ITEM = (By.XPATH, "//*[@class='rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, "//*[@class='rct-icon rct-icon-check']//ancestor::span//span[@class='rct-title']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")

    def click_expand_all_button(self):
        self.element_is_visible(self.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.ITEM_LIST)
        item = item_list[random.randint(1, 15)]
        self.go_to_element(item)
        item.click()

    def get_checked_checkbox(self):
        checked_item = self.elements_are_present(self.TITLE_ITEM)
        data = []
        for item in checked_item:
            data.append(item.text.lower().replace(' ', '').replace('doc', '').replace('.', ''))
        return data

    def get_output_result(self):
        result_list = self.elements_are_present(self.OUTPUT_RESULT)
        output_data = []
        for item in result_list:
            output_data.append(item.text.lower().replace(' ', ''))
        return output_data