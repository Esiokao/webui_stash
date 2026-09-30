# test_40_ieee802.3az_eee_settings.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("ieee802.3az_eee_settings")
class TestIEEE8023azEEEsettings:

    def test_check_header(self, ieee802_3az_eee_settings_page):
        result = ieee802_3az_eee_settings_page.get_page_header_text()
        expected_val = "IEEE802.3az EEE settings"

        assert expected_val == result

    def test_check_global_settings_tier2_header(self, ieee802_3az_eee_settings_page):
        result = ieee802_3az_eee_settings_page.get_ieee802_3az_eee_settings_header_text()
        expected_val = "IEEE802.3az EEE settings"

        assert expected_val == result

    def test_check_from_port_title_and_value(self, ieee802_3az_eee_settings_page):
        title, value = ieee802_3az_eee_settings_page.get_from_port_title_and_value()
        expected_title = "From Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_to_port_title_and_value(self, ieee802_3az_eee_settings_page):
        title, value = ieee802_3az_eee_settings_page.get_to_port_title_and_value()
        expected_title = "To Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_state_title_and_value(self, ieee802_3az_eee_settings_page):
        title, value = ieee802_3az_eee_settings_page.get_state_title_and_value()
        expected_title = "State"
        expected_val = "Disabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_button_text(self, ieee802_3az_eee_settings_page):
        result = ieee802_3az_eee_settings_page.get_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_title_table(self, ieee802_3az_eee_settings_page):
        result = ieee802_3az_eee_settings_page.get_title_table()
        expected_val = ["Port", "State"]

        assert expected_val == result

    def test_check_port1_table_value(self, ieee802_3az_eee_settings_page):
        result = ieee802_3az_eee_settings_page.get_port1_table_value()
        expected_val = ["1", "Disabled"]

        assert expected_val == result
