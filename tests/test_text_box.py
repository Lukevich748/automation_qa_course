from generator.generator import generated_person
from pages.text_box_page import TextBoxPage


def test_text_box(driver):
    text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
    text_box_page.open()
    person_info = next(generated_person())
    full_name = person_info.full_name
    email = person_info.email
    current_address = person_info.current_address
    permanent_address = person_info.permanent_address
    text_box_page.fill_full_name(full_name)
    text_box_page.fill_email(email)
    text_box_page.fill_current_address(current_address)
    text_box_page.fill_permanent_address(permanent_address)
    text_box_page.click_submit()
    output_name = text_box_page.filled_full_name()
    output_email = text_box_page.filled_email()
    output_current_address = text_box_page.filled_current_address()
    output_permanent_address = text_box_page.filled_permanent_address()
    assert full_name == output_name, "The full name does not match"
    assert email == output_email, "The email does not match"
    assert current_address == output_current_address, "The current address does not match"
    assert permanent_address == output_permanent_address, "The permanent address does not match"


