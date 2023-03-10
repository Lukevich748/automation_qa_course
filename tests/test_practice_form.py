import random
import time

from generator.generator import generated_person
from pages.practice_form_page import PracticeFormPage


def test_practice_form(driver):
    practice_form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
    practice_form_page.open()
    practice_form_page.remove_footer()
    person_info = next(generated_person())
    first_name = person_info.firstname
    last_name = person_info.lastname
    email = person_info.email
    phone_number = person_info.phone_number
    current_address = person_info.current_address
    practice_form_page.fill_first_name(first_name)
    practice_form_page.fill_last_name(last_name)
    practice_form_page.fill_email(email)
    practice_form_page.click_gender_radio_button()
    practice_form_page.fill_phone_number(phone_number)
    date = practice_form_page.date_picker()
    day = date[random.randint(1, len(date))]
    practice_form_page.choose_date(day)
    practice_form_page.fill_subjects()
    practice_form_page.click_hobbies_check_box()
    practice_form_page.fill_current_address(current_address)
    practice_form_page.click_submit()
    result = practice_form_page.get_result()
    assert f'{first_name} {last_name}' == result[0], "The form has not been filled"
    assert email == result[1], "The form has not been filled"
    assert phone_number == result[3], "The form has not been filled"
    assert current_address == result[7], "The form has not been filled"

def test_required_fields(driver):
    practice_form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
    practice_form_page.open()
    practice_form_page.remove_footer()
    practice_form_page.click_submit()
    practice_form_page.check_first_name_field()
    assert practice_form_page.check_first_name_field() == "rgb(220, 53, 69)", 'This field is not required'
    practice_form_page.check_last_name_field()
    assert practice_form_page.check_last_name_field() == "rgb(220, 53, 69)", 'This field is not required'