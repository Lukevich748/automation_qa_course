from pages.web_table_page import WebTablePage


def test_web_table_add_person(driver):
    web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
    web_table_page.open()
    web_table_page.click_add_button()
    new_person = web_table_page.add_new_person()
    table_result = web_table_page.check_add_new_person()
    assert new_person in table_result, "The person was not added"


def test_web_table_search_person(driver):
    web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
    web_table_page.open()
    web_table_page.click_add_button()
    data_list = web_table_page.add_new_person()
    firstname = data_list[0]
    web_table_page.search_some_person(firstname)
    search_result = web_table_page.check_search_person()
    assert data_list == search_result, "The person was not found"


def test_delete_person(driver):
    web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
    web_table_page.open()
    web_table_page.click_add_button()
    data_list = web_table_page.add_new_person()
    firstname = data_list[0]
    web_table_page.search_some_person(firstname)
    web_table_page.delete_person(firstname)
    delete_result = web_table_page.check_delete_person()
    assert delete_result == True, "The element was not deleted"
