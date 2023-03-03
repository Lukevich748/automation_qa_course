from pages.check_box_page import CheckBoxPage


def test_check_box(driver):

    check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
    check_box_page.open()
    check_box_page.click_expand_all_button()
    check_box_page.click_random_checkbox()
    data = check_box_page.get_checked_checkbox()
    output_data = check_box_page.get_output_result()
    assert data == output_data
