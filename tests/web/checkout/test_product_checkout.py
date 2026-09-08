import pytest
import json
import os

from pageObjects.web.login_page import LoginPage
from pageObjects.web.dashboard_page import DashboardPage
from pageObjects.web.cart_page import CartPage
from pageObjects.web.orders_review_page import OrdersReviewPage
from pageObjects.web.orders_history_page import OrdersHistoryPage
from pageObjects.web.common_scenario import CommonScenario

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

def test_product_checkout(page, request):
    # TestRail ID: C95
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    
    # Initialize Page Objects directly in the test
    login_page = LoginPage(page, scenario)
    dashboard_page = DashboardPage(page, scenario)
    cart_page = CartPage(page, scenario)
    orders_review_page = OrdersReviewPage(page, scenario)
    orders_history_page = OrdersHistoryPage(page, scenario)
    
    login_page.go_to()
    login_page.valid_login(test_data["username"], test_data["password"])

    dashboard_page.search_product_add_cart("Zara Coat 3")
    dashboard_page.navigate_to_cart()

    cart_page.verify_product_is_displayed("Zara Coat 3")
    cart_page.click_checkout()

    orders_review_page.search_country_and_select("ind", "India")
    orders_review_page.submit_and_get_order_id()
    
    order_id = scenario.get_value("orderId")
    assert order_id is not None, "Order ID should be generated after submission"

    dashboard_page.navigate_to_orders()
    orders_history_page.search_order_and_select()
    
    history_order_id = orders_history_page.get_order_id()
    assert order_id in history_order_id, f"Expected Order ID {order_id} in history, but got {history_order_id}"
