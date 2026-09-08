import pytest
import json
import os
from playwright.sync_api import expect

from pageObjects.web.login_page import LoginPage
from pageObjects.web.common_scenario import CommonScenario

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

def test_invalid_login(page, request):
    # TestRail ID: C96
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    login_page = LoginPage(page, scenario)
    
    login_page.go_to()
    # Using invalid credentials
    login_page.valid_login("invalid_user@play.com", "WrongPassword123")
    
    # Asserting error message appears (assuming the locator exists, standard for these apps)
    error_message = page.locator("[class*='toast-message']")
    error_message.wait_for(state="visible")
    assert error_message.is_visible(), "Error message should be displayed for invalid login"
