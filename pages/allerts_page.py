from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AlertsPage(BasePage):

    # alerts button
    ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")

    def click_alert_button(self):
        self.element_is_visible(self.ALERT_BUTTON).click()
        self.accept_alert()