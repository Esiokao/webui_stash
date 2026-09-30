# test_13_port_settings.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("port_settings")
class TestPortSettings:

    def test_check_header(self, port_settings_page):
        result = port_settings_page.get_page_header_text()
        expected_val = "Port Settings"

        assert expected_val == result

    def test_check_port_settings_tier2_header(self, port_settings_page):
        result = port_settings_page.get_port_settings_tier2_header_text()
        expected_val = "Port Settings"

        assert expected_val == result

    def test_check_from_port_title_and_value(self, port_settings_page):
        title, value = port_settings_page.get_from_port_title_and_value()
        expected_title = "From Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_to_port_title_and_value(self, port_settings_page):
        title, value = port_settings_page.get_to_port_title_and_value()
        expected_title = "To Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value
    
    def test_check_media_title_and_value(self, port_settings_page):
        title, value = port_settings_page.get_media_title_and_value()
        expected_title = "Media"
        expected_val = "Copper"

        assert expected_title == title
        assert expected_val == value

    def test_check_state_title_and_value(self, port_settings_page):
        title, value = port_settings_page.get_state_title_and_value()
        expected_title = "State"
        expected_val = "Enabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_speed_title_and_value(self, port_settings_page):
        title, value = port_settings_page.get_speed_title_and_value()
        expected_title = "Speed"
        expected_val = "Auto"

        assert expected_title == title
        assert expected_val == value

    def test_check_mdi_mdix_title_and_value(self, port_settings_page):
        title, value = port_settings_page.get_mdi_mdix_title_and_value()
        expected_title = "MDI/MDIX"
        expected_val = "Auto"

        assert expected_title == title
        assert expected_val == value

    def test_check_flow_control_title_and_value(self, port_settings_page):
        title, value = port_settings_page.get_flow_control_title_and_value()
        expected_title = "Flow Control"
        expected_val = "Disabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_auto_downgrade_title_and_value(self, port_settings_page):
        title, value = port_settings_page.get_auto_downgrade_title_and_value()
        expected_title = "Auto Downgrade"
        expected_val = "Disabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_10_half_text(self, port_settings_page):
        result = port_settings_page.get_10_half_text()
        expected_val = " 10_half"

        assert expected_val == result

    def test_check_10_full_text(self, port_settings_page):
        result = port_settings_page.get_10_full_text()
        expected_val = " 10_full"

        assert expected_val == result

    def test_check_100_half_text(self, port_settings_page):
        result = port_settings_page.get_100_half_text()
        expected_val = " 100_half"

        assert expected_val == result

    def test_check_100_full_text(self, port_settings_page):
        result = port_settings_page.get_100_full_text()
        expected_val = " 100_full"

        assert expected_val == result

    def test_check_1000_full_text(self, port_settings_page):
        result = port_settings_page.get_1000_full_text()
        expected_val = " 1000full"

        assert expected_val == result

    def test_check_table_title(self, port_settings_page):
        result = port_settings_page.get_table_title()
        expected_val = ["Port", "Link Status", "State", "Speed", "MDI/MDIX", "Flow Control", "Auto Downgrade", "Capability Advertised"]

        assert expected_val == result
    
    def test_check_table_value(self, port_settings_page):
        result = port_settings_page.get_table_value()
        expected_val = ["1", "Down", "Enabled", "Auto", "Auto", "Disabled", "Disabled", "10_half 10_full 100_half 100_full 1000_full"]

        assert expected_val == result

    def test_check_port_settings_button1(self, port_settings_page):
        result = port_settings_page.get_port_settings_button1_value()
        expected_result = "Apply"

        assert expected_result == result

    def test_check_port_settings_button2(self, port_settings_page):
        result = port_settings_page.get_port_settings_button2_value()
        expected_result = "Refresh"

        assert expected_result == result
    
    def test_default_port_speed(self, port_settings_page):
        opt = port_settings_page.get_port_speed_checkbox_value()
        expected_val = ["10_half", "10_full", "100_half", "100_full", "1000full"]

        assert opt == expected_val
