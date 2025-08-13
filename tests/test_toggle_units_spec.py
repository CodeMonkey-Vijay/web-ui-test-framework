import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controllers.home import HomeController
from utils.config_loader import load_config
from playwright.sync_api import sync_playwright

def test_toggle_units():
    config = load_config()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        home = HomeController(page, config.base_url)
        home.goto()
        current_temperature_unit = home.getCurrentTemperatureUnit()
        home.switch_to_fahrenheit()
        assert "°F" in current_temperature_unit

        context.close()
        browser.close()
