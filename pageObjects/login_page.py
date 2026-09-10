import json
import os
from playwright.sync_api import expect
from .common_page import CommonPage

def load_locator(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    locator_path = os.path.join(base_dir, "locators", "web", filename)
    with open(locator_path) as f:
        return json.load(f)

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

class LoginPage(CommonPage):
    flow_name = "login_page"
    
    def __init__(self, page, scenario):
        """Initialize the LoginPage with page and scenario objects.
        
        Args:
            page: Playwright page object for browser interactions.
            scenario: Scenario object for test context and utilities.
        """
        super().__init__(page, scenario)
        self.locators = load_locator("login_page.json")
        self.test_data = load_test_data()
    
    def go_to(self):
        """Navigate to the login page and verify key elements are visible.
        
        Navigates to the login page URL, waits for the page to load completely,
        and verifies that username field, password field, and login button are displayed.
        Performs accessibility analysis after page load.
        """
        self.page.goto(self.test_data["qa"])
        self.page.wait_for_load_state("domcontentloaded")
        self.scenario.a11y_analysis()
        
        username_element = self.page.locator(self.locators["username_field"])
        username_element.wait_for(state="visible")
        expect(username_element).to_be_visible()
        
        password_element = self.page.locator(self.locators["password_field"])
        password_element.wait_for(state="visible")
        expect(password_element).to_be_visible()
        
        login_button_element = self.page.locator(self.locators["login_button"])
        login_button_element.wait_for(state="visible")
        expect(login_button_element).to_be_visible()
    
    def input_username(self, username):
        """Input username into the username field.
        
        Locates the username input field, clears any existing text, inputs the provided
        username, and verifies the text was entered successfully.
        
        Args:
            username (str): The username to input into the field.
        """
        username_element = self.page.locator(self.locators["username_field"])
        username_element.wait_for(state="visible")
        username_element.wait_for(state="attached")
        
        username_element.clear()
        username_element.fill(username)
        
        entered_value = username_element.input_value()
        assert entered_value == username, f"Expected username '{username}' but got '{entered_value}'"
    
    def click_login_button(self):
        """Click the login button and wait for page transition.
        
        Locates the login button, waits for it to be clickable, performs a click action,
        and waits for any loading indicators to disappear and page transition to complete.
        """
        login_button_element = self.page.locator(self.locators["login_button"])
        login_button_element.wait_for(state="visible")
        expect(login_button_element).to_be_enabled()
        
        login_button_element.click()
        
        try:
            loading_indicator = self.page.locator(self.locators["loading_indicator"])
            loading_indicator.wait_for(state="hidden", timeout=5000)
        except:
            pass
        
        self.page.wait_for_load_state("networkidle")