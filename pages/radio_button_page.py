from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RadioButtonPage(BasePage):

    # radio buttons
    YES_RADIOBUTTON = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[@for='impressiveRadio']")
    NO_RADIOBUTTON = (By.XPATH, "//label[@for='noRadio']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.YES_RADIOBUTTON,
                   'impressive': self.IMPRESSIVE_RADIOBUTTON,
                   'no': self.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.OUTPUT_RESULT).text