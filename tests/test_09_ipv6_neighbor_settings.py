# test_9_ipv6_neighbor_settings.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("ipv6_neighbor_settings.ipv6_neighbor_settings")
class TestIPv6NeighborSettings:

    def test_check_header(self, ipv6_neighbor_settings_page):
        result = ipv6_neighbor_settings_page.get_page_header_text()
        expected_val = "IPv6 Neighbor Settings"

        assert expected_val == result

    def test_check_v6_neighbor_settings_tier2_header(self, ipv6_neighbor_settings_page):
        result = ipv6_neighbor_settings_page.get_v6_neighbor_settings_tier2_header_text()
        expected_val = "IPv6 Neighbor Settings"

        assert expected_val == result

    def test_check_interface_name_title_and_value(self, ipv6_neighbor_settings_page):
        title, value = ipv6_neighbor_settings_page.get_interface_name_title_and_value()
        expected_title = "Interface Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_Neighbor_IPv6_Address_title_and_value(self, ipv6_neighbor_settings_page):
        title, value = ipv6_neighbor_settings_page.get_Neighbor_IPv6_Address_title_and_value()
        expected_title = "Neighbor IPv6 Address"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_Link_Layer_MAC_Address_title_and_value(self, ipv6_neighbor_settings_page):
        title, value = ipv6_neighbor_settings_page.get_Link_Layer_MAC_Address_title_and_value()
        expected_title = "Link Layer MAC Address"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_ipv6_neighbor_settings_button_text(self, ipv6_neighbor_settings_page):
        result = ipv6_neighbor_settings_page.get_ipv6_neighbor_settings_button_text()
        expected_val = "Apply"

        assert expected_val == result

@allure.title("ipv6_neighbor_settings.IPv6_Neighbor_Table")
class TestIPv6NeighborTable:

    def test_check_ipv6_neighbor_Table_header(self, ipv6_neighbor_settings_page):
        result = ipv6_neighbor_settings_page.get_ipv6_neighbor_Table_header_text()
        expected_val = "IPv6 Neighbor Table"

        assert expected_val == result

    def test_check_Neighbor_Table_interface_name_title_and_value(self, ipv6_neighbor_settings_page):
        title, value = ipv6_neighbor_settings_page.get_Neighbor_Table_interface_name_title_and_value()
        expected_title = "Interface Name"
        expected_val = ""
        
        assert expected_title == title
        assert expected_val == value

    def test_check__state_title_and_value(self, ipv6_neighbor_settings_page):
        title, value1, value2 = ipv6_neighbor_settings_page.get_state_title_and_value()
        expected_title = "State"
        expected_val1 = "All"
        expected_val2 = ""

        assert expected_title == title
        assert expected_val1 == value1
        assert expected_val2 == value2

    def test_check__total_entries_title(self, ipv6_neighbor_settings_page):
        title= ipv6_neighbor_settings_page.get_total_entries_title()
        expected_title = "Total Entries : 0"

        assert expected_title == title

    def test_check_table_title(self, ipv6_neighbor_settings_page):
        result = ipv6_neighbor_settings_page.get_table_title()
        expected_val = ["Neighbor", "Link Layer Address", "Interface Name", "State"]

        assert expected_val == result

    def test_check_ipv6_neighbor_table_button1_text(self, ipv6_neighbor_settings_page):
        result = ipv6_neighbor_settings_page.get_ipv6_neighbor_table_button1_text()
        expected_val = "Find"

        assert expected_val == result

    def test_check_ipv6_neighbor_table_button2_text(self, ipv6_neighbor_settings_page):
        result = ipv6_neighbor_settings_page.get_ipv6_neighbor_table_button2_text()
        expected_val = "Clear"

        assert expected_val == result

    def test_check_table_default_is_empty(self, ipv6_neighbor_settings_page):
        result = ipv6_neighbor_settings_page.get_table_default_is_empty()

        assert result