from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProgressBarPage(BasePage):

    START_BUTTON = (By.XPATH, "//button[@id='startStopButton']")
    PROGRESS_BAR = (By.XPATH, "//div[@id='progressBar']//div")

    def click_start_button(self):
        self.element_is_visible(self.START_BUTTON).click()

    def check_progress_bar_value(self, age):
        progress_bar = self.element_is_visible(self.PROGRESS_BAR)
        while int(progress_bar.get_attribute("aria-valuenow")) < 100:
            if int(progress_bar.get_attribute("aria-valuenow")) == age:
                self.element_is_visible(self.START_BUTTON).click()
                break
        return int(progress_bar.get_attribute("aria-valuenow"))

    def get_progress_bar_value(self):
        progress_bar = self.element_is_visible(self.PROGRESS_BAR)
        progress_bar.get_attribute("aria-valuenow")
        return int(progress_bar.get_attribute("aria-valuenow"))