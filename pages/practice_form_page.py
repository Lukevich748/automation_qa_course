import random
import time

from selenium.webdriver import Keys
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
    SUBJECT = (By.XPATH, "//input[@id='subjectsInput']")
    HOBBIES = (By.XPATH, f"//label[@for='hobbies-checkbox-{random.randint(1, 3)}']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    SUBMIT = (By.XPATH, "//div/button[@id='submit']")
    RESULT = (By.XPATH, "//td[text()][2]")

    @staticmethod
    def get_day_locator(key):
        xpath = f"//div[text()='{key}']"
        day = (By.XPATH, xpath)
        return day

    # fill fields
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

    def fill_subjects(self):
        subject = self.element_is_visible(self.SUBJECT)
        subject.send_keys("English")
        subject.send_keys(Keys.RETURN)

    def click_hobbies_check_box(self):
        self.element_is_visible(self.HOBBIES).click()

    def fill_current_address(self, current_address):
        self.element_is_visible(self.CURRENT_ADDRESS).send_keys(current_address)

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script('document.getElementById("fixedban").style.display="none"')

    def click_submit(self):
        self.element_is_visible(self.SUBMIT).click()

    def get_result(self):
        result_list = self.elements_are_visible(self.RESULT)
        result = [i.text for i in result_list]
        return result

    # required fields
    def check_first_name_field(self):
        time.sleep(0.05)
        element = self.element_is_visible(self.FIRST_NAME)
        border_color = element.value_of_css_property("border-color")
        return border_color

    def check_last_name_field(self):
        time.sleep(0.05)
        element = self.element_is_visible(self.LAST_NAME)
        border_color = element.value_of_css_property("border-color")
        return border_color