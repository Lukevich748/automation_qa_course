import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AlertsPage(BasePage):

    # alerts button
    ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")
    TIME_ALERT_BUTTON = (By.XPATH, "//button[@id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = (By.XPATH, "//button[@id='confirmButton']")
    CONFIRM_ALERT_BUTTON_RESULT = (By.XPATH, "//span[text()='You selected ']")
    PROMPT_ALERT_BUTTON = (By.XPATH, "//button[@id='promtButton']")
    PROMPT_ALERT_BUTTON_RESULT = (By.XPATH, "//span[text()='You entered ']")

    def click_alert_button(self):
        self.element_is_visible(self.ALERT_BUTTON).click()

    def click_time_alert_button(self):
        self.element_is_visible(self.TIME_ALERT_BUTTON).click()
        self.alert_is_present()

    def click_confirm_alert_button(self):
        self.element_is_visible(self.CONFIRM_ALERT_BUTTON).click()

    def click_prompt_alert_button(self):
        self.element_is_visible(self.PROMPT_ALERT_BUTTON).click()

    def get_confirm_alert_button_result(self):
        confirm_result = self.element_is_visible(self.CONFIRM_ALERT_BUTTON_RESULT)
        return confirm_result.text

    def get_prompt_alert_button_result(self):
        prompt_result = self.element_is_visible(self.PROMPT_ALERT_BUTTON_RESULT)
        return prompt_result.text

    def input_text_in_alert(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)