import time

from generator.generator import generated_person
from pages.allerts_page import AlertsPage


def test_alerts(driver):
    alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
    alerts_page.open()
    person_info = next(generated_person())
    first_name = person_info.firstname
    alerts_page.click_alert_button()
    alert_text = alerts_page.get_alert_text()
    assert alert_text == "You clicked a button"
    alerts_page.accept_alert()
    alerts_page.click_time_alert_button()
    appear_alert_text = alerts_page.get_alert_text()
    assert appear_alert_text == "This alert appeared after 5 seconds"
    alerts_page.accept_alert()
    alerts_page.click_confirm_alert_button()
    confirm_alert_text = alerts_page.get_alert_text()
    assert confirm_alert_text == "Do you confirm action?"
    alerts_page.accept_alert()
    ok_confirm_result = alerts_page.get_confirm_alert_button_result()
    assert ok_confirm_result == "You selected Ok"
    alerts_page.click_confirm_alert_button()
    alerts_page.dismiss_alert()
    cancel_confirm_result = alerts_page.get_confirm_alert_button_result()
    assert cancel_confirm_result == "You selected Cancel"
    alerts_page.click_prompt_alert_button()
    alerts_page.input_text_in_alert(first_name)
    alerts_page.accept_alert()
    prompt_alert_button_result = alerts_page.get_prompt_alert_button_result()
    assert "You entered " + first_name == prompt_alert_button_result
