from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ProgressBarPageLocators
from pages.base_page import BasePage
import random


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        item = item_list[random.randint(1, 15)]
        self.go_to_element(item)
        item.click()

    def get_checked_checkbox(self):
        checked_item = self.elements_are_present(self.locators.TITLE_ITEM)
        data = []
        for item in checked_item:
            data.append(item.text.lower().replace(' ', '').replace('doc', '').replace('.', ''))
        return data

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        output_data = []
        for item in result_list:
            output_data.append(item.text.lower().replace(' ', ''))
        return output_data


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def click_add_button(self):
        add_button = self.element_is_visible(self.locators.ADD_BUTTON)
        add_button.click()

    def add_new_person(self):
        person_info = next(generated_person())
        firstname = person_info.firstname
        lastname = person_info.lastname
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT).click()
        return [firstname, lastname, str(age), email, str(salary), department]

    def check_add_new_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        search_result = self.elements_are_present(self.locators.SEARCH_RESULT)
        data = []
        for item in search_result:
            data.append(item.text)
        return data[:-1]

    def delete_person(self, key):
        self.element_is_visible(self.locators.get_delete_button_locator(key)).click()

    def check_delete_person(self):
        try:
            self.element_is_visible(self.locators.NO_ROWS_FOUND)
            return True
        except:
            return False


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def click_start_button(self, age):
        start_button = self.element_is_visible(self.locators.START_BUTTON)
        start_button.click()
        progress_bar = self.element_is_visible(self.locators.PROGRESS_BAR)
        while int(progress_bar.get_attribute("aria-valuenow")) < 100:
            if int(progress_bar.get_attribute("aria-valuenow")) == age:
                start_button.click()
                break
        return int(progress_bar.get_attribute("aria-valuenow"))

    def get_progress_bar_value(self):
        progress_bar = self.element_is_visible(self.locators.PROGRESS_BAR)
        progress_bar.get_attribute("aria-valuenow")
        return int(progress_bar.get_attribute("aria-valuenow"))