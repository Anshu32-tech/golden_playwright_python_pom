class CommonScenario:
    def __init__(self, page, request):
        self.page = page
        self.request = request
        self.my_map = {}

    def take_screenshot(self, name: str):
        # Placeholder for screenshot attachment logic
        pass

    def hooks(self):
        print("hook from the scenario page")

    def set_value(self, key: str, value: str):
        self.my_map[key] = value

    def get_value(self, key: str):
        return self.my_map.get(key)

    def a11y_analysis(self):
        # Placeholder for accessibility analysis
        pass
