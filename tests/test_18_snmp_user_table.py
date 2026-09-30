# test_18_snmp_user_table.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("snmp_user_table")
class TestSNMPUserTable:

    def test_check_header(self, snmp_user_table_page):
        result = snmp_user_table_page.get_page_header_text()
        expected_val = "SNMP User Table"

        assert expected_val == result

    def test_check_snmp_user_table_tier2_header(self, snmp_user_table_page):
        result = snmp_user_table_page.get_snmp_user_table_tier2_header_text()
        expected_val = "SNMP User Table"

        assert expected_val == result

    def test_check_user_name_title_and_value(self, snmp_user_table_page):
        title, value = snmp_user_table_page.get_user_name_title_and_value()
        expected_title = "User Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_group_name_title_and_value(self, snmp_user_table_page):
        title, value = snmp_user_table_page.get_group_name_title_and_value()
        expected_title = "Group Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_snmp_version_title_and_value(self, snmp_user_table_page):
        title, value = snmp_user_table_page.get_snmp_version_title_and_value()
        expected_title = "SNMP Version"
        expected_val = "v1"

        assert expected_title == title
        assert expected_val == value

    def test_check_auth_protocol_title_and_value(self, snmp_user_table_page):
        title, value = snmp_user_table_page.get_auth_protocol_title_and_value()
        expected_title = "Auth-Protocol"
        expected_val = "MD5"

        assert expected_title == title
        assert expected_val == value

    def test_check_auth_protocol_password_title_and_value(self, snmp_user_table_page):
        title, value = snmp_user_table_page.get_auth_protocol_password_title_and_value()
        expected_title = "Password"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_priv_protocol_title_and_value(self, snmp_user_table_page):
        title, value = snmp_user_table_page.get_priv_protocol_title_and_value()
        expected_title = "Priv-Protocol"
        expected_val = "DES"

        assert expected_title == title
        assert expected_val == value

    def test_check_priv_protocol_password_title_and_value(self, snmp_user_table_page):
        title, value = snmp_user_table_page.get_priv_protocol_password_title_and_value()
        expected_title = "Password"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_snmp_user_table_button_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_snmp_user_table_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_total_entries_title(self, snmp_user_table_page):
        title= snmp_user_table_page.get_total_entries_title()
        expected_title = "Total Entries : 4"

        assert expected_title == title

    def test_check_table_title(self, snmp_user_table_page):
        result = snmp_user_table_page.get_table_title()
        expected_val = ["User Name", "Group Name", "SNMP Version", "Auth Protocol", "Priv-Protocol", "Auth ByKey", "Priv ByKey", "Delete"]

        assert expected_val == result

    def test_check_readonly_v1_table_value(self, snmp_user_table_page):
        result = snmp_user_table_page.get_readonly_v1_table_value()
        expected_val = ["ReadOnly", "ReadOnly", "v1", "NONE", "NONE", "NONE", "NONE", ""]

        assert expected_val == result
    
    def test_check_readonly_v1_table_button_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_readonly_v1_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_readonly_v2c_table_value(self, snmp_user_table_page):
        result = snmp_user_table_page.get_readonly_v2c_table_value()
        expected_val = ["ReadOnly", "ReadOnly", "v2c", "NONE", "NONE", "NONE", "NONE", ""]

        assert expected_val == result
    
    def test_check_readonly_v2c_table_button_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_readonly_v2c_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_readwrite_v1_table_value(self, snmp_user_table_page):
        result = snmp_user_table_page.get_read_write_v1_table_value()
        expected_val = ["ReadWrite", "ReadWrite", "v1", "NONE", "NONE", "NONE", "NONE", ""]

        assert expected_val == result
    
    def test_check_readwrite_v1_table_button_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_read_write_v1_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_readwrite_v2c_table_value(self, snmp_user_table_page):
        result = snmp_user_table_page.get_read_write_v2c_table_value()
        expected_val = ["ReadWrite", "ReadWrite", "v2c", "NONE", "NONE", "NONE", "NONE", ""]

        assert expected_val == result
    
    def test_check_readwrite_v2c_table_button_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_read_write_v2c_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_user_table_page_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_user_table_page_text()
        expected_val = "1 / 1"

        assert expected_val == result

    def test_check_user_table_page_button1_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_user_table_page_button1_text()
        expected_val = "|<"

        assert expected_val == result

    def test_check_user_table_page_button2_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_user_table_page_button2_text()
        expected_val = "<"

        assert expected_val == result

    def test_check_user_table_page_button3_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_user_table_page_button3_text()
        expected_val = "1"

        assert expected_val == result

    def test_check_user_table_page_button4_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_user_table_page_button4_text()
        expected_val = ">"

        assert expected_val == result

    def test_check_user_table_page_button5_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_user_table_page_button5_text()
        expected_val = ">|"

        assert expected_val == result

    def test_check_user_table_page_value(self, snmp_user_table_page):
        result = snmp_user_table_page.get_user_table_page_value()
        expected_val = ""

        assert expected_val == result

    def test_check_user_table_page_button6_text(self, snmp_user_table_page):
        result = snmp_user_table_page.get_user_table_page_button6_text()
        expected_val = "Go"

        assert expected_val == result


