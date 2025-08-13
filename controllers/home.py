from controllers.base import BaseController

class HomeController(BaseController):
    search_input = "input[data-t*='WeaSearchLocation']"
    search_suggestion_first = '#locationSuggestions_0'
    celsius_button = "div[data-t*='settingCenterMainButton']"
    fahrenheit_button = 'button[data-t="settingCenterCelsius"]'
    getCurrentTemperatureUnitInfo = "span[class*='summaryTemperatureUnit']"

    def search_city(self, city: str):
        self.fill(self.search_input, city)
        self.page.wait_for_selector(self.search_suggestion_first)
        self.click(self.search_suggestion_first)

    def switch_to_fahrenheit(self):
        self.click(self.celsius_button)

    def switch_to_celsius(self):
        self.click(self.fahrenheit_button)

    def getCurrentTemperatureUnit(self):
        return self.page.inner_text(self.getCurrentTemperatureUnitInfo)
