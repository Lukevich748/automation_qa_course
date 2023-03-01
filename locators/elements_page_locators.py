from selenium.webdriver.common.by import By


class TextBoxPageLocators:
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


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@aria-label='Expand all']")
    ITEM_LIST = (By.XPATH, "//span[@class='rct-title']")
    CHECKED_ITEM = (By.XPATH, "//*[@class='rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, "//*[@class='rct-icon rct-icon-check']//ancestor::span//span[@class='rct-title']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")


class RadioButtonPageLocators:
    # radio buttons
    YES_RADIOBUTTON = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[@for='impressiveRadio']")
    NO_RADIOBUTTON = (By.XPATH, "//label[@for='noRadio']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")


class WebTablePageLocators:
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