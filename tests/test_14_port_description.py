# test_14_port_description.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("port_description")
class TestPortDescription:

    def test_check_header(self, port_description_page):
        result = port_description_page.get_page_header_text()
        expected_val = "Port Description"

        assert expected_val == result

    def test_check_port_description_tier2_header(self, port_description_page):
        result = port_description_page.get_port_description_tier2_header_text()
        expected_val = "Port Description"

        assert expected_val == result

    def test_check_from_port_title_and_value(self, port_description_page):
        title, value = port_description_page.get_from_port_title_and_value()
        expected_title = "From Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_to_port_title_and_value(self, port_description_page):
        title, value = port_description_page.get_to_port_title_and_value()
        expected_title = "To Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_medium_type_title_and_value(self, port_description_page):
        title, value = port_description_page.get_medium_type_title_and_value()
        expected_title = "Medium Type"
        expected_val = "Copper"

        assert expected_title == title
        assert expected_val == value

    def test_check_description_title_and_value(self, port_description_page):
        title, value = port_description_page.get_description_title_and_value()
        expected_title = "Description"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value
        
    def test_check_table_title(self, port_description_page):
        result = port_description_page.get_table_title()
        expected_val = ["Port", "Description"]

        assert expected_val == result

    def test_check_table_value(self, port_description_page):
        result = port_description_page.get_table_value()
        expected_val = ["1"]

        assert expected_val == result

    def test_check_port_description_button(self, port_description_page):
        result = port_description_page.get_port_description_button_value()
        expected_val = "Apply"

        assert expected_val == result
    
    
