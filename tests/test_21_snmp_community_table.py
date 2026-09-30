# test_21_snmp_community_table.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("snmp_community_table")
class TestSNMPCommunityTable:

    def test_check_header(self, snmp_community_table_page):
        result = snmp_community_table_page.get_page_header_text()
        expected_val = "SNMP Community Table Configuration"

        assert expected_val == result

    def test_check_snmp_community_table_tier2_header(self, snmp_community_table_page):
        result = snmp_community_table_page.get_snmp_community_table_tier2_header_text()
        expected_val = "SNMP Community Table Configuration"

        assert expected_val == result

    def test_check_community_name_title_and_value(self, snmp_community_table_page):
        title, value = snmp_community_table_page.get_community_name_title_and_value()
        expected_title = "Community Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_view_name_title_and_value(self, snmp_community_table_page):
        title, value = snmp_community_table_page.get_view_name_title_and_value()
        expected_title = "View Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_access_right_title_and_value(self, snmp_community_table_page):
        title, value = snmp_community_table_page.get_access_right_title_and_value()
        expected_title = "Access Right (View Policy)"
        expected_val = "ReadOnly"

        assert expected_title == title
        assert expected_val == value

    def test_check_button_text(self, snmp_community_table_page):
        result = snmp_community_table_page.get_button_text()
        expected_val = "Apply"

        assert expected_val == result
        
    def test_check_total_entries_title(self, snmp_community_table_page):
        result = snmp_community_table_page.get_total_entries_title()
        expected_val = "Total Entries : 2"

        assert expected_val == result
        
    def test_check_table_title(self, snmp_community_table_page):
        result = snmp_community_table_page.get_table_title()
        expected_val = ["Community Name", "View Name", "Access Right", "Delete"]

        assert expected_val == result
        
    def test_check_private_table_value(self, snmp_community_table_page):
        result = snmp_community_table_page.get_private_table_value()
        expected_val = ["private", "ReadWrite", "ReadWrite", ""]

        assert expected_val == result
        
    def test_check_private_table_button_text(self, snmp_community_table_page):
        result = snmp_community_table_page.get_private_table_button_text()
        expected_val = "Delete"

        assert expected_val == result
        
    def test_check_public_table_value(self, snmp_community_table_page):
        result = snmp_community_table_page.get_public_table_value()
        expected_val = ["public", "ReadOnly", "ReadOnly", ""]

        assert expected_val == result
        
    def test_check_public_table_button_text(self, snmp_community_table_page):
        result = snmp_community_table_page.get_public_table_button_text()
        expected_val = "Delete"

        assert expected_val == result
        

