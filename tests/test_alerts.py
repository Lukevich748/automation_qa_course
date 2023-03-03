import time

from pages.allerts_page import AlertsPage


def test_alerts(driver):
    alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
    alerts_page.open()
    alerts_page.click_alert_button()