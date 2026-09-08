import pytest
import json
import os
from playwright.sync_api import expect

from pageObjects.web.login_page import LoginPage
from pageObjects.web.dashboard_page import DashboardPage
from pageObjects.web.orders_history_page import OrdersHistoryPage
from pageObjects.web.common_scenario import CommonScenario

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

def test_view_order_details(page, request):
    # TestRail ID: C99
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    
    login_page = LoginPage(page, scenario)
    dashboard_page = DashboardPage(page, scenario)
    orders_history_page = OrdersHistoryPage(page, scenario)
    
    login_page.go_to()
    login_page.valid_login(test_data["username"], test_data["password"])

    dashboard_page.navigate_to_orders()
    
    # Just click the first view button available in history
    first_view_button = page.locator("button:has-text('View')").first
    first_view_button.click()
    
    # Assert order details page loaded
    order_summary = page.locator(".email-title")
    order_summary.wait_for(state="visible")
    assert order_summary.is_visible(), "Order Summary details should be visible"
