# test_34_mac_flapping_detection.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("mac_flapping_detection")
class TestMacFlappingDetection:

    def test_check_header(self, mac_flapping_detection_page):
        result = mac_flapping_detection_page.get_page_header_text()
        expected_val = "MAC Flapping Detection"

        assert expected_val == result

    def test_check_mac_flapping_detection_tier2_header(self, mac_flapping_detection_page):
        result = mac_flapping_detection_page.get_mac_flapping_detection_tier2_header_text()
        expected_val = "MAC Flapping Global Settings"

        assert expected_val == result

    def test_check_state_title(self, mac_flapping_detection_page):
        result = mac_flapping_detection_page.get_state_title_text()
        expected_val = "State"

        assert expected_val == result

    def test_check_state_option_one_text(self, mac_flapping_detection_page):
        result = mac_flapping_detection_page.get_state_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_state_option_two_text(self, mac_flapping_detection_page):
        result = mac_flapping_detection_page.get_state_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result
    
    def test_default_state_is_disabled(self, mac_flapping_detection_page):
        opt = mac_flapping_detection_page.get_checked_state_option()
        expected_val = "Disabled"

        assert opt == expected_val, "default state is not Disabled"

    def test_check_interval_title_and_value(self, mac_flapping_detection_page):
        title, value = mac_flapping_detection_page.get_interval_title_and_value()
        expected_title = "Interval(1-3600 sec)"
        expected_value = "1"

        assert expected_title == title
        assert expected_value == value

    def test_check_total_entries_title(self, mac_flapping_detection_page):
        title= mac_flapping_detection_page.get_total_entries_title()
        expected_title = "Total Entries : 0"

        assert expected_title == title

    def test_check_MAC_Flapping_Detection_table_title(self, mac_flapping_detection_page):
        result = mac_flapping_detection_page.get_MAC_Flapping_Detection_table_title()
        expected_val = ["Mac Address", "VID", "Total Time", "Flapped Times", "Port List"]

        assert expected_val == result

    def test_check_table_default_is_empty(self, mac_flapping_detection_page):
        result = mac_flapping_detection_page.get_table_default_is_empty()

        assert result

    def test_check_MAC_Flapping_Detection_button_text(self, mac_flapping_detection_page):
        result = mac_flapping_detection_page.get_MAC_Flapping_Detection_button_text()
        expected_val = "Apply"

        assert expected_val == result
        
