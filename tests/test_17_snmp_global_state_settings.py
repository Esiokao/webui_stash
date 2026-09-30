# test_17_snmp_global_state_settings.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("snmp_global_state_settings")
class TestSNMPGlobalStateSettings:

    def test_check_header(self, snmp_global_state_settings_page):
        result = snmp_global_state_settings_page.get_page_header_text()
        expected_val = "SNMP Global State Settings"

        assert expected_val == result

    def test_check_snmp_global_state_settings_tier2_header(self, snmp_global_state_settings_page):
        result = snmp_global_state_settings_page.get_snmp_global_state_settings_tier2_header_text()
        expected_val = "SNMP Global State Settings"

        assert expected_val == result

    def test_check_snmp_global_state_settings_title(self, snmp_global_state_settings_page):
        result = snmp_global_state_settings_page.get_snmp_global_state_settings_title_text()
        expected_val = "SNMP Global State:"

        assert expected_val == result

    def test_check_snmp_global_state_settings_option_one_text(self, snmp_global_state_settings_page):
        result = snmp_global_state_settings_page.get_snmp_global_state_settings_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_snmp_global_state_settings_option_two_text(self, snmp_global_state_settings_page):
        result = snmp_global_state_settings_page.get_snmp_global_state_settings_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result
    
    def test_default_snmp_global_state_settings_is_disabled(self, snmp_global_state_settings_page):
        opt = snmp_global_state_settings_page.get_checked_snmp_global_state_settings_option()
        expected_val = "Disabled"

        assert opt == expected_val, "default snmp global state settings is not Disabled"

    def test_check_snmp_global_state_settings_button(self, snmp_global_state_settings_page):
        result = snmp_global_state_settings_page.get_snmp_global_state_settings_button_text()
        expected_val = "Apply"

        assert expected_val == result


