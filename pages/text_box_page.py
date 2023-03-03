from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    # form field
    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    # created form
    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")

    # create a new person
    def fill_full_name(self, full_name):
        self.element_is_visible(self.FULL_NAME).send_keys(full_name)

    def fill_email(self, email):
        self.element_is_visible(self.EMAIL).send_keys(email)

    def fill_current_address(self, current_address):
        self.element_is_visible(self.CURRENT_ADDRESS).send_keys(current_address)

    def fill_permanent_address(self, permanent_address):
        self.element_is_visible(self.PERMANENT_ADDRESS).send_keys(permanent_address)

    def click_submit(self):
        self.element_is_visible(self.SUBMIT).click()

    # created person result
    def filled_full_name(self):
        full_name = self.element_is_present(self.CREATED_FULL_NAME).text.split(":")[1]
        return full_name

    def filled_email(self):
        email = self.element_is_present(self.CREATED_EMAIL).text.split(":")[1]
        return email

    def filled_current_address(self):
        current_address = self.element_is_present(self.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        return current_address

    def filled_permanent_address(self):
        permanent_address = self.element_is_present(self.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return permanent_address
