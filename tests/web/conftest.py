import pytest
from playwright.sync_api import sync_playwright

import sys
import os
# Add the root directory so pageObjects can be imported properly
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

@pytest.fixture(scope="function")
def context_creation(page):
    # This acts as a base fixture if any global browser config is needed.
    # Playwright's native `page` fixture is usually sufficient.
    yield page
