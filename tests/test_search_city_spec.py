import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controllers.home import HomeController
from controllers.search import SearchController
from utils.config_loader import load_config
from playwright.sync_api import sync_playwright

def test_search_city():
    config = load_config()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        home = HomeController(page, config.base_url)
        home.goto()
        home.search_city(config.default_city)

        search = SearchController(page, config.base_url)
        city = search.get_city_name()

        assert config.default_city.lower() in city.lower()

        context.close()
        browser.close()
