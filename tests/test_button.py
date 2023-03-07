from pages.buttons_page import ButtonsPage


def test_buttons(driver):

    buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
    buttons_page.open()
    buttons_page.click_double_click_me_button()
    double_click_output_result = buttons_page.get_output_result_double_click()
    assert double_click_output_result == "You have done a double click", "The double click button was not pressed"
    buttons_page.click_right_click_me_button()
    right_click_output_result = buttons_page.get_output_result_right_click()
    assert right_click_output_result == "You have done a right click", "The right click button was not pressed"
    buttons_page.click_click_me_button()
    one_click_output_result = buttons_page.get_output_result_click()
    assert one_click_output_result == "You have done a dynamic click", "The dynamic click button was not pressed"



