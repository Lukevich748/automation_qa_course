from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    #form field
    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    #created form
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