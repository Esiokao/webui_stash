# test_19_snmp_group_table.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("snmp_group_table")
class TestSNMPGroupTable:

    def test_check_header(self, snmp_group_table_page):
        result = snmp_group_table_page.get_page_header_text()
        expected_val = "SNMP Group Table"

        assert expected_val == result

    def test_check_snmp_group_table_tier2_header(self, snmp_group_table_page):
        result = snmp_group_table_page.get_snmp_group_table_tier2_header_text()
        expected_val = "SNMP Group Table"

        assert expected_val == result

    def test_check_group_name_title_and_value(self, snmp_group_table_page):
        title, value = snmp_group_table_page.get_group_name_title_and_value()
        expected_title = "Group Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_read_view_name_title_and_value(self, snmp_group_table_page):
        title, value = snmp_group_table_page.get_read_view_name_title_and_value()
        expected_title = "Read View Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_write_view_name_title_and_value(self, snmp_group_table_page):
        title, value = snmp_group_table_page.get_write_view_name_title_and_value()
        expected_title = "Write View Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_security_model_title(self, snmp_group_table_page):
        title, value = snmp_group_table_page.get_security_model_title_and_value()
        expected_title = "Security Model"
        expected_val = "v1"

        assert expected_title == title
        assert expected_val == value

    def test_check_security_level_title(self, snmp_group_table_page):
        title, value = snmp_group_table_page.get_security_level_title_and_value()
        expected_title = "Security Level"
        expected_val = "NoAuthNoPriv"

        assert expected_title == title
        assert expected_val == value

    def test_check_notify_view_name_title(self, snmp_group_table_page):
        title, value = snmp_group_table_page.get_notify_view_name_title_and_value()
        expected_title = "Notify View Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_snmp_group_table_button_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_snmp_group_table_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_total_entries_title(self, snmp_group_table_page):
        result = snmp_group_table_page.get_total_entries_title()
        expected_val = "Total Entries : 4"

        assert expected_val == result

    def test_check_table_title(self, snmp_group_table_page):
        result = snmp_group_table_page.get_table_title()
        expected_val = ["Group Name", "Read View", "Write View", "Notify View", "Security Model", "Security Level", "Delete"]

        assert expected_val == result

    def test_check_readonly_v1_table_value(self, snmp_group_table_page):
        result = snmp_group_table_page.get_readonly_v1_table_value()
        expected_val = ["ReadOnly", "ReadWrite", "ReadWrite", "v1", "NoAuthNoPriv", ""]

        assert expected_val == result

    def test_check_readonly_v1_table_button_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_readonly_v1_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_readonly_v2c_table_value(self, snmp_group_table_page):
        result = snmp_group_table_page.get_readonly_v2c_table_value()
        expected_val = ["ReadOnly", "ReadWrite", "ReadWrite", "v2c", "NoAuthNoPriv", ""]

        assert expected_val == result

    def test_check_readonly_v2c_table_button_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_readonly_v2c_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_read_write_v1_table_value(self, snmp_group_table_page):
        result = snmp_group_table_page.get_read_write_v1_table_value()
        expected_val = ["ReadWrite", "ReadWrite", "ReadWrite", "ReadWrite", "v1", "NoAuthNoPriv", ""]

        assert expected_val == result

    def test_check_read_write_v1_table_button_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_read_write_v1_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_read_write_v2c_table_value(self, snmp_group_table_page):
        result = snmp_group_table_page.get_read_write_v2c_table_value()
        expected_val = ["ReadWrite", "ReadWrite", "ReadWrite", "ReadWrite", "v2c", "NoAuthNoPriv", ""]

        assert expected_val == result

    def test_check_read_write_v2c_table_button_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_read_write_v2c_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_group_table_page_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_group_table_page_text()
        expected_val = "1 / 1"

        assert expected_val == result

    def test_check_group_table_page_button1_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_group_table_page_button1_text()
        expected_val = "|<"

        assert expected_val == result

    def test_check_group_table_page_button2_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_group_table_page_button2_text()
        expected_val = "<"

        assert expected_val == result

    def test_check_group_table_page_button3_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_group_table_page_button3_text()
        expected_val = "1"

        assert expected_val == result

    def test_check_group_table_page_button4_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_group_table_page_button4_text()
        expected_val = ">"

        assert expected_val == result

    def test_check_group_table_page_button5_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_group_table_page_button5_text()
        expected_val = ">|"

        assert expected_val == result

    def test_check_group_table_page_value(self, snmp_group_table_page):
        result = snmp_group_table_page.get_group_table_page_value()
        expected_val = ""

        assert expected_val == result

    def test_check_group_table_page_button6_text(self, snmp_group_table_page):
        result = snmp_group_table_page.get_group_table_page_button6_text()
        expected_val = "Go"

        assert expected_val == result