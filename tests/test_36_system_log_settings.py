# test_36_system_log_settings.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("system_log_settings.system_log_global_settings")
class TestSystemLogGlobalSettings:

    def test_check_header(self, system_log_settings_page):
        result = system_log_settings_page.get_page_header_text()
        expected_val = "System Log Settings"

        assert expected_val == result

    def test_check_system_log_global_settings_tier2_header(self, system_log_settings_page):
        result = system_log_settings_page.get_system_log_global_settings_tier2_header_text()
        expected_val = "System Log Global Settings"

        assert expected_val == result

    def test_check_system_log_global_settings_option_one_text(self, system_log_settings_page):
        result = system_log_settings_page.get_system_log_global_settings_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_system_log_global_settings_option_two_text(self, system_log_settings_page):
        result = system_log_settings_page.get_system_log_global_settings_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result
    
    def test_default_system_log_global_settings_is_enabled(self, system_log_settings_page):
        opt = system_log_settings_page.get_checked_system_log_global_settings_option()
        expected_val = "Enabled"

        assert expected_val == opt, "default system log global settings is not Enabled"

    def test_check_system_log_global_settings_button_text(self, system_log_settings_page):
        result = system_log_settings_page.get_system_log_global_settings_button_text()
        expected_val = "Apply"

        assert expected_val == result

@allure.title("system_log_settings.system_log_save_mode_settings")
class TestSystemLogSaveModeSettings:

    def test_check_system_log_save_mode_settings_header(self, system_log_settings_page):
        result = system_log_settings_page.get_system_log_save_mode_settings_header_text()
        expected_val = "System Log Save Mode Settings"

        assert expected_val == result

    def test_check_save_mode_title_and_value(self, system_log_settings_page):
        title, value1, value2 = system_log_settings_page.get_save_mode_title_and_value()
        expected_title = "Save Mode"
        expected_value1 = "On Demand"
        expected_value2 = "1800"

        assert expected_title == title
        assert expected_value1 == value1
        assert expected_value2 == value2

    def test_check_save_mode_button_text(self, system_log_settings_page):
        result = system_log_settings_page.get_save_mode_button_text()
        expected_val = "Apply"

        assert expected_val == result

