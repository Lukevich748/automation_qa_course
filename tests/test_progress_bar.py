import random
from pages.progress_bar_page import ProgressBarPage


def test_progress_bar(driver):
    progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
    progress_bar_page.open()
    progress_bar_page.click_start_button()
    input_value = progress_bar_page.check_progress_bar_value(random.randint(1, 100))
    output_value = progress_bar_page.get_progress_bar_value()
    assert input_value == output_value, "Values are not equal"
