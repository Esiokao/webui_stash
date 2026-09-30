# test_32_ping_test.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("ping_test")
class TestPingTest:

    def test_check_header(self, ping_test_page):
        result = ping_test_page.get_page_header_text()
        expected_val = "Ping Test"

        assert expected_val == result

    def test_check_ping_test_tier2_header(self, ping_test_page):
        result = ping_test_page.get_ping_test_tier2_header_text()
        expected_val = "Ping Test"

        assert expected_val == result
    
    def test_check_target_ip_address_title_and_v4_value_v6_value(self, ping_test_page):
        title, value_v4, value_v6 = ping_test_page.get_target_ip_address_title_and_v4_value_v6_value()
        expected_title = "Target IP Address"
        expected_val_v4 = "..."
        expected_val_v6 = ""

        assert expected_title == title
        assert expected_val_v4 == value_v4
        assert expected_val_v6 == value_v6

    def test_check_v4_and_v6_mode_options(self, ping_test_page):
        option_one = ping_test_page.get_v4_mode_option_text()
        option_two = ping_test_page.get_v6_mode_option_text()
        expected_val_one = ".\n.\n.\nIPv4"
        expected_val_two = "IPv6"

        assert expected_val_one == option_one
        assert expected_val_two == option_two

    def test_check_v4_mode_default_options(self, ping_test_page):
        assert ping_test_page.get_checked_v4_mode_option() == True

    def test_check_v6_mode_default_options(self, ping_test_page):
        assert ping_test_page.get_checked_v6_mode_option() == False

    def test_check_repeat_pinging_for_title(self, ping_test_page):
        result = ping_test_page.get_repeat_pinging_for_title()
        expected_val = "Repeat Pinging for"

        assert expected_val == result

    def test_check_repeat_pinging_for_default_options1_and_text(self, ping_test_page):
        result, text = ping_test_page.get_repeat_pinging_for_options1_and_text()
        expected_val = True
        expected_text = "Infinite Times"

        assert expected_val == result
        assert expected_text == text

    def test_check_repeat_pinging_for_default_options2_and_value(self, ping_test_page):
        result, value = ping_test_page.get_repeat_pinging_for_options2_and_value()
        expected_val = False
        expected_text = ""

        assert expected_val == result
        assert expected_text == value

    def test_check_timeout_title_and_value(self, ping_test_page):
        title, value = ping_test_page.get_timeout_title_and_value()
        expected_title = "Timeout"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_button_text(self, ping_test_page):
        result = ping_test_page.get_button_text()
        expected_val = "Start"

        assert expected_val == result