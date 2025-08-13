from controllers.base import BaseController

class HomeController(BaseController):
    search_input = 'input[placeholder="Search for a city"]'
    search_suggestion_first = 'ul[role="listbox"] li:first-child'
    celsius_button = 'button[title="Celsius"]'
    fahrenheit_button = 'button[title="Fahrenheit"]'

    def search_city(self, city: str):
        self.fill(self.search_input, city)
        self.page.wait_for_selector(self.search_suggestion_first)
        self.click(self.search_suggestion_first)

    def switch_to_fahrenheit(self):
        self.click(self.fahrenheit_button)

    def switch_to_celsius(self):
        self.click(self.celsius_button)
