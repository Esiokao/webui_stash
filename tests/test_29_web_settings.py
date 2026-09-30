# test_29_web_settings.py

import allure
import pytest
import asyncio
import os
from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("Web_Settings")
class TestWebSettings:

    def test_check_header(self, web_settings_page):
        result = web_settings_page.get_page_header_text()
        expected_val = "Web Settings"

        assert expected_val == result

    def test_check_web_settings_tier2_header(self, web_settings_page):
        result = web_settings_page.get_web_settings_tier2_header_text()
        expected_val = "Web Settings"

        assert expected_val == result

    def test_check_web_state_title(self, web_settings_page):
        result = web_settings_page.get_web_state_title_text()
        expected_val = "WEB State"

        assert expected_val == result

    def test_check_web_state_option_one_text(self, web_settings_page):
        result = web_settings_page.get_web_state_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_web_state_option_two_text(self, web_settings_page):
        result = web_settings_page.get_web_state_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_web_state_is_enabled(self, web_settings_page):
        opt = web_settings_page.get_checked_web_state_option()
        expected_val = "Enabled"

        assert opt == expected_val, "default web state is not Enabled"

    def test_check_port_title_and_value(self, web_settings_page):
        title, value = web_settings_page.get_port_title_and_value()
        expected_title = "Port (1-65535)"
        expected_value = "80"

        assert expected_title == title
        assert expected_value == value

    def test_check_web_settings_apply_button_text(self, web_settings_page):
        result = web_settings_page.get_web_settings_apply_button_text()
        expected_val = "Apply"

        assert expected_val == result
