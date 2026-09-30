# test_26_mac_address_aging_time.py

import allure
import pytest
import asyncio
import os
from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("mac_address_aging_time")
class TestMacAddressAgingTime:

    def test_check_header(self, mac_address_aging_time_page):
        result = mac_address_aging_time_page.get_page_header_text()
        expected_val = "MAC Address Aging Time"

        assert expected_val == result

    def test_check_user_accounts_tier2_header(self, mac_address_aging_time_page):
        result = mac_address_aging_time_page.get_mac_address_aging_time_tier2_header_text()
        expected_val = "MAC Address Aging Time Settings"

        assert expected_val == result

    def test_check_mac_address_aging_time_title_and_value(self, mac_address_aging_time_page):
        title, value = mac_address_aging_time_page.get_mac_address_aging_time_title_and_value()
        expected_title = "MAC Address Aging Time (3-377)"
        expected_value = "300"

        assert expected_title == title
        assert expected_value == value

    def test_check_get_mac_address_aging_time_button_text(self, mac_address_aging_time_page):
        result = mac_address_aging_time_page.get_get_mac_address_aging_time_button_text()
        expected_val = "Apply"

        assert expected_val == result
