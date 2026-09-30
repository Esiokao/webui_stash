from selenium.webdriver.common.by import By
import json
import os

class LocatorManager:
    def __init__(self, config_file=None):
        self.config_file = config_file or os.path.join(
            os.path.dirname(__file__), 
            "..", 
            "config",
            "locators.json"
        )
        self.locators = self._load_locators()

    def _load_locators(self):
        """Load locators from JSON configuration file"""
        with open(self.config_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _convert_to_by(self, by_string):
        """Convert string representation to By class attribute"""
        by_map = {
            "id": By.ID,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "tag": By.TAG_NAME,
            "link": By.LINK_TEXT,
            "partial": By.PARTIAL_LINK_TEXT
        }
        return by_map.get(by_string.lower(), By.XPATH)

    def get_locator(self, *path):
        """
        Get a locator tuple (By, value) from the configuration
        Example: get_locator("system_settings", "menu", "system")
        """
        current = self.locators
        for key in path:
            if key not in current:
                raise KeyError(f"Locator path {path} not found")
            current = current[key]

        if isinstance(current, dict) and "by" in current and "value" in current:
            return (self._convert_to_by(current["by"]), current["value"])
        raise ValueError(f"Invalid locator format at path {path}")

    def update_locator(self, new_value, *path):
        """Update a locator value in the configuration"""
        current = self.locators
        for key in path[:-1]:
            current = current[key]
        
        if isinstance(new_value, tuple):
            by_str = {v: k for k, v in self._convert_to_by.__defaults__[0].items()}
            current[path[-1]] = {
                "by": by_str.get(new_value[0], "xpath"),
                "value": new_value[1]
            }
        else:
            current[path[-1]] = new_value

        self._save_locators()

    def _save_locators(self):
        """Save locators back to JSON file"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.locators, f, indent=2)

    def get_all_locators(self, prefix=()):
        """
        Recursively get all locators with their full paths
        Returns: dict of path tuples to locator tuples
        """
        result = {}
        
        def _recurse(current, current_prefix):
            for key, value in current.items():
                new_prefix = current_prefix + (key,)
                if isinstance(value, dict):
                    if "by" in value and "value" in value:
                        result[new_prefix] = (
                            self._convert_to_by(value["by"]),
                            value["value"]
                        )
                    else:
                        _recurse(value, new_prefix)
                        
        _recurse(self.locators, prefix)
        return result 