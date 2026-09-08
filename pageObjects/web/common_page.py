from .common_scenario import CommonScenario

class CommonPage:
    def __init__(self, page, scenario: CommonScenario):
        self.page = page
        self.scenario = scenario

    def get_value(self, key: str):
        return self.scenario.get_value(key)

    def set_value(self, key: str, value: str):
        self.scenario.set_value(key, value)

    def take_screenshot(self, name: str):
        self.scenario.take_screenshot(name)
