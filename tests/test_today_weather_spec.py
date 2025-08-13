from controllers.home import HomeController
from utils.config_loader import load_config
from playwright.sync_api import sync_playwright

def test_today_weather():
    config = load_config()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        home = HomeController(page, config.base_url)
        home.goto()
        assert page.locator("text=Today").is_visible()
        assert "°C" in page.inner_text("body") or "°F" in page.inner_text("body")

        context.close()
        browser.close()
