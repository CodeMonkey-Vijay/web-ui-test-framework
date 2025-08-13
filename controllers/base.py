from playwright.sync_api import Page
from utils.logger import logger

class BaseController:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def goto(self, path=""):
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def click(self, selector: str):
        logger.info(f"Clicking {selector}")
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        logger.info(f"Filling {selector} with {text}")
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        text = self.page.locator(selector).inner_text()
        logger.info(f"Text from {selector}: {text}")
        return text
