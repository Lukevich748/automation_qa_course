import time

from generator.generator import generated_person
from pages.practice_form_page import PracticeFormPage


def test_practice_form(driver):
    practice_form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
    practice_form_page.open()
    person_info = next(generated_person())
    first_name = person_info.firstname
    last_name = person_info.lastname
    email = person_info.email
    phone_number = person_info.phone_number
    practice_form_page.fill_first_name(first_name)
    practice_form_page.fill_last_name(last_name)
    practice_form_page.fill_email(email)
    practice_form_page.click_gender_radio_button()
    practice_form_page.fill_phone_number(phone_number)
    practice_form_page.date_picker()
    time.sleep(3)