# test_22_snmp_host_table.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("snmp_host_table")
class TestSNMPHostTable:

    def test_check_header(self, snmp_host_table_page):
        result = snmp_host_table_page.get_page_header_text()
        expected_val = "SNMP Host Table"

        assert expected_val == result

    def test_check_snmp_host_table_tier2_header(self, snmp_host_table_page):
        result = snmp_host_table_page.get_snmp_host_table_tier2_header_text()
        expected_val = "SNMP Host Table"

        assert expected_val == result
    
    def test_check_host_ip_address_title_and_v4_value_v6_value(self, snmp_host_table_page):
        title, value_v4, value_v6 = snmp_host_table_page.get_host_ip_address_title_and_v4_value_v6_value()
        expected_title = "Host IP Address"
        expected_val_v4 = "..."
        expected_val_v6 = ""

        assert expected_title == title
        assert expected_val_v4 == value_v4
        assert expected_val_v6 == value_v6

    def test_check_v4_and_v6_mode_options(self, snmp_host_table_page):
        option_one = snmp_host_table_page.get_v4_mode_option_text()
        option_two = snmp_host_table_page.get_v6_mode_option_text()
        expected_val_one = ".\n.\n.\nIPv4"
        expected_val_two = "IPv6"

        assert expected_val_one == option_one
        assert expected_val_two == option_two

    def test_check_v4_mode_default_options(self, snmp_host_table_page):
        assert snmp_host_table_page.get_checked_v4_mode_option() == True

    def test_check_v6_mode_default_options(self, snmp_host_table_page):
        assert snmp_host_table_page.get_checked_v6_mode_option() == False

    def test_check_snmp_version_title_and_value(self, snmp_host_table_page):
        title, value = snmp_host_table_page.get_snmp_version_title_and_value()
        expected_title = "SNMP Version"
        expected_val = "V1"

        assert expected_title == title
        assert expected_val == value

    def test_check_community_string_snmpv3_user_name_title_and_value(self, snmp_host_table_page):
        title, value = snmp_host_table_page.get_community_string_snmpv3_user_name_title_and_value()
        expected_title = "Community Name/SNMPv3 User Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_button_text(self, snmp_host_table_page):
        result = snmp_host_table_page.get_button_text()
        expected_val = "Apply"

        assert expected_val == result
        
    def test_check_total_entries_title(self, snmp_host_table_page):
        result = snmp_host_table_page.get_total_entries_title()
        expected_val = "Total Entries : 0"

        assert expected_val == result
        
    def test_check_table_title(self, snmp_host_table_page):
        result = snmp_host_table_page.get_table_title()
        expected_val = ["Host IP Address", "SNMP Version", "Community Name/SNMPv3 User Name", "Delete"]

        assert expected_val == result

    def test_check_table_default_is_empty(self, snmp_host_table_page):
        assert snmp_host_table_page.get_table_default_is_empty() == True


