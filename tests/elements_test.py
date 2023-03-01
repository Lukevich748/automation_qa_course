import random
import time

from conftest import driver
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ProgressBarPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, "The full name does not match"
            assert email == output_email, "The email does not match"
            assert current_address == output_current_address, "The current address does not match"
            assert permanent_address == output_permanent_address, "The permanent address does not match"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            data = check_box_page.get_checked_checkbox()
            output_data = check_box_page.get_output_result()
            assert data == output_data

    class TestRadioButton:

        def test_radio_button(self,  driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            web_table_page.click_add_button()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_add_new_person()
            assert new_person in table_result, "The person was not added"

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            web_table_page.click_add_button()
            data_list = web_table_page.add_new_person()
            firstname = data_list[0]
            web_table_page.search_some_person(firstname)
            search_result = web_table_page.check_search_person()
            assert data_list == search_result, "The person was not found"

        def test_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            web_table_page.click_add_button()
            data_list = web_table_page.add_new_person()
            firstname = data_list[0]
            web_table_page.search_some_person(firstname)
            web_table_page.delete_person(firstname)
            delete_result = web_table_page.check_delete_person()
            assert  delete_result == True, "The element was not deleted"

    class TestProgressBar:

        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            input_value = 43
            progress_bar_page.click_start_button(input_value)
            output_value = progress_bar_page.get_progress_bar_value()
            assert input_value == output_value - 1, "Values are not equal"