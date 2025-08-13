from controllers.home import HomeController
from utils.config_loader import load_config
from playwright.sync_api import sync_playwright

def test_toggle_units():
    config = load_config()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        home = HomeController(page, config.base_url)
        home.goto()
        home.switch_to_fahrenheit()
        assert "°F" in page.inner_text("body")

        home.switch_to_celsius()
        assert "°C" in page.inner_text("body")

        context.close()
        browser.close()
