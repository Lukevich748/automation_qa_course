import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PracticeFormPage(BasePage):

    # form fields
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    GENDER = (By.XPATH, f"//label[@for='gender-radio-{random.randint(1, 3)}']")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DATE = (By.XPATH, "//input[@id='dateOfBirthInput']")
    DAY_OF_MONTH = (By.XPATH, "//div[@role='option']")

    @staticmethod
    def get_day_locator(key):
        xpath = f"//div[text()='{key}']"
        day = (By.XPATH, xpath)
        return day

    def fill_first_name(self, first_name):
        self.element_is_visible(self.FIRST_NAME).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.element_is_visible(self.LAST_NAME).send_keys(last_name)

    def fill_email(self, email):
        self.element_is_visible(self.EMAIL).send_keys(email)

    def click_gender_radio_button(self):
        self.element_is_visible(self.GENDER).click()

    def fill_phone_number(self, phone_number):
        self.element_is_visible(self.MOBILE).send_keys(phone_number)

    def date_picker(self):
        self.element_is_visible(self.DATE).click()
        day_of_month = self.elements_are_visible(self.DAY_OF_MONTH)
        data = []
        for item in day_of_month:
            data.append(item.text)
        return data

    def choose_date(self, day):
        self.element_is_visible(self.get_day_locator(day)).click()