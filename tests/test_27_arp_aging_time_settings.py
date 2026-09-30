# test_27_arp_aging_time_settings.py

import allure
import pytest
import asyncio
import os
from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("arp_aging_time_settings")
class TestArpAgingTimeSettings:

    def test_check_header(self, arp_aging_time_settings_page):
        result = arp_aging_time_settings_page.get_page_header_text()
        expected_val = "ARP Aging Time Settings"

        assert expected_val == result

    def test_check_arp_aging_time_settings_tier2_header(self, arp_aging_time_settings_page):
        result = arp_aging_time_settings_page.get_arp_aging_time_settings_tier2_header_text()
        expected_val = "ARP Aging Time Settings"

        assert expected_val == result

    def test_check_arp_aging_time_title_and_value(self, arp_aging_time_settings_page):
        title, value = arp_aging_time_settings_page.get_arp_aging_time_title_and_value()
        expected_title = "ARP Aging Time (0-65535)"
        expected_value = "5"

        assert expected_title == title
        assert expected_value == value

    def test_check_get_arp_aging_time_button_text(self, arp_aging_time_settings_page):
        result = arp_aging_time_settings_page.get_get_arp_aging_time_button_text()
        expected_val = "Apply"

        assert expected_val == result
