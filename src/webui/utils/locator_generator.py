from selenium.webdriver.common.by import By
import json
import re

class LocatorGenerator:
    @staticmethod
    def generate_stable_xpath(element_path):
        """
        Generate a more stable XPath from a full path
        """
        # Remove position indices where possible
        simplified = re.sub(r'\[\d+\]', '', element_path)
        # Add meaningful attributes if available
        return simplified

    @staticmethod
    def suggest_locator_strategy(element_html):
        """
        Suggest the best locator strategy based on element attributes
        """
        if 'id="' in element_html:
            id_match = re.search(r'id="([^"]*)"', element_html)
            return (By.ID, id_match.group(1))
        elif 'class="' in element_html:
            class_match = re.search(r'class="([^"]*)"', element_html)
            return (By.CLASS_NAME, class_match.group(1))
        elif 'name="' in element_html:
            name_match = re.search(r'name="([^"]*)"', element_html)
            return (By.NAME, name_match.group(1))
        else:
            # Generate a CSS selector as fallback
            return (By.CSS_SELECTOR, "your-css-selector")

    @staticmethod
    def export_locators_to_py(locators_dict, output_file):
        """
        Export locators to a Python file
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("from selenium.webdriver.common.by import By\n\n")
            f.write("class Locators:\n")
            for name, locator in locators_dict.items():
                f.write(f"    {name} = {locator}\n")

    @staticmethod
    def import_from_json(json_file):
        """
        Import locators from a JSON file
        """
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f) 