import pytest
from playwright.sync_api import Page, expect
from pageObjects.loginPage import LoginPage


class TestSuite01Scripts:
    """Test Suite 01 Scripts"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup fixture for test initialization"""
        self.page = page
        self.loginPage = LoginPage(page)

    def test_login_flow(self):
        """Test login flow with username input and login button click"""
        # Navigate to the login page
        self.loginPage.go_to()
        
        # Input username
        self.loginPage.input_username()
        
        # Click on the Login button
        self.loginPage.click_login_button()
        
        # Assertion to verify successful login
        expect(self.page).to_have_url(lambda url: "dashboard" in url or "home" in url, timeout=10000)
