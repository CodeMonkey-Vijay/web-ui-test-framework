from controllers.base import BaseController

class SearchController(BaseController):
    city_name_label = 'h1'

    def get_city_name(self):
        return self.get_text(self.city_name_label)
