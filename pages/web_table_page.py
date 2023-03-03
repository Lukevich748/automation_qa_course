from selenium.webdriver.common.by import By
from generator.generator import generated_person
from pages.base_page import BasePage


class WebTablePage(BasePage):

    # registration person form
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    # person info
    FULL_PEOPLE_LIST = (By.XPATH, "//div[@class='rt-tr-group']")

    # search area
    SEARCH_INPUT = (By.XPATH, "//input[@id='searchBox']")

    # edit buttons
    SEARCH_RESULT = (By.XPATH, "//span[contains(@id, 'delete-record')]//ancestor::div/div[@role='gridcell']")

    # delete person func
    @staticmethod
    def get_delete_button_locator(key):
        xpath = f"//div[text()='{key}']//following-sibling::div//span[@title='Delete']"
        delete_button = (By.XPATH, xpath)
        return delete_button

    NO_ROWS_FOUND = (By.XPATH, "//div[@class='rt-noData']")


    def click_add_button(self):
        add_button = self.element_is_visible(self.ADD_BUTTON)
        add_button.click()

    def add_new_person(self):
        person_info = next(generated_person())
        firstname = person_info.firstname
        lastname = person_info.lastname
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        self.element_is_visible(self.FIRSTNAME_INPUT).send_keys(firstname)
        self.element_is_visible(self.LASTNAME_INPUT).send_keys(lastname)
        self.element_is_visible(self.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.SALARY_INPUT).send_keys(salary)
        self.element_is_visible(self.DEPARTMENT_INPUT).send_keys(department)
        self.element_is_visible(self.SUBMIT).click()
        return [firstname, lastname, str(age), email, str(salary), department]

    def check_add_new_person(self):
        people_list = self.elements_are_present(self.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        search_result = self.elements_are_present(self.SEARCH_RESULT)
        data = []
        for item in search_result:
            data.append(item.text)
        return data[:-1]

    def delete_person(self, key):
        self.element_is_visible(self.get_delete_button_locator(key)).click()

    def check_delete_person(self):
        try:
            self.element_is_visible(self.NO_ROWS_FOUND)
            return True
        except:
            return False