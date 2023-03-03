from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ButtonsPage(BasePage):

    # buttons
    DOUBLE_CLICK_ME_BUTTON = (By.XPATH, "//button[@ID='doubleClickBtn']")
    RIGHT_CLICK_ME_BUTTON = (By.XPATH, "//button[@ID='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")

    # output result
    OUTPUT_RESULT_DOUBLE_CLICK = (By.XPATH, "//p[@ID='doubleClickMessage']")
    OUTPUT_RESULT_RIGHT_CLICK = (By.XPATH, "//p[@ID='rightClickMessage']")
    OUTPUT_RESULT_CLICK = (By.XPATH, "//p[@ID='dynamicClickMessage']")

    def click_double_click_me_button(self):
        self.action_double_click(self.element_is_visible(self.DOUBLE_CLICK_ME_BUTTON))

    def click_right_click_me_button(self):
        self.action_right_click(self.element_is_visible(self.RIGHT_CLICK_ME_BUTTON))

    def click_click_me_button(self):
        self.element_is_visible(self.CLICK_ME_BUTTON).click()

    def get_output_result_double_click(self):
        output = self.element_is_visible(self.OUTPUT_RESULT_DOUBLE_CLICK).text
        return output

    def get_output_result_right_click(self):
        output = self.element_is_visible(self.OUTPUT_RESULT_RIGHT_CLICK).text
        return output

    def get_output_result_click(self):
        output = self.element_is_visible(self.OUTPUT_RESULT_CLICK).text
        return output