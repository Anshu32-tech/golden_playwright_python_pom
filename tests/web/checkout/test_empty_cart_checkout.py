import pytest
import json
import os
from playwright.sync_api import expect

from pageObjects.web.login_page import LoginPage
from pageObjects.web.dashboard_page import DashboardPage
from pageObjects.web.cart_page import CartPage
from pageObjects.web.common_scenario import CommonScenario

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

def test_empty_cart_checkout(page, request):
    # TestRail ID: C98
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    
    login_page = LoginPage(page, scenario)
    dashboard_page = DashboardPage(page, scenario)
    cart_page = CartPage(page, scenario)
    
    login_page.go_to()
    login_page.valid_login(test_data["username"], test_data["password"])

    # Navigate directly to cart without adding products
    dashboard_page.navigate_to_cart()
    
    # Assert cart is empty
    no_products_message = page.locator("text=No Products in Your Cart !")
    assert no_products_message.is_visible(), "Cart should be empty"
    
    # Try to checkout
    checkout_button = page.get_by_role("button", name="Checkout❯")
    assert not checkout_button.is_enabled() or not checkout_button.is_visible(), "Checkout should be blocked for an empty cart"
