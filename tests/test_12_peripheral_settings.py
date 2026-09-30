# test_12_peripheral_settings.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("peripheral_settings.fan_settings")
class TestFanSettings:

    def test_check_header(self, peripheral_settings_page):
        result = peripheral_settings_page.get_page_header_text()
        expected_val = "Peripheral Settings"

        assert expected_val == result

    def test_check_fan_settings_tier2_header(self, peripheral_settings_page):
        result = peripheral_settings_page.get_fan_settings_tier2_header_text()
        expected_val = "Fan Settings"

        assert expected_val == result

    def test_check_fan_trap_title(self, peripheral_settings_page):
        result = peripheral_settings_page.get_fan_trap_title_text()
        expected_val = "Fan Trap"

        assert expected_val == result

    def test_check_fan_trap_option_one_text(self, peripheral_settings_page):
        result = peripheral_settings_page.get_fan_trap_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_fan_trap_option_two_text(self, peripheral_settings_page):
        result = peripheral_settings_page.get_fan_trap_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_fan_trap_is_disabled(self, peripheral_settings_page):
        opt = peripheral_settings_page.get_checked_fan_trap_option()
        expected_val = "Disabled"

        assert opt == expected_val, "default fan trap is not Disabled"

    def test_check_fan_mode_title_and_value(self, peripheral_settings_page):
        title, value = peripheral_settings_page.get_fan_mode_title_and_value()
        expected_title = "Fan Mode"
        expected_val = "Normal"

        assert expected_title == title
        assert expected_val == value

    def test_check_fan_settings_button(self, peripheral_settings_page):
        result = peripheral_settings_page.get_fan_settings_button_value()
        expected_result = "Apply"

        assert expected_result == result


@allure.title("peripheral_settings.environment_temperature_settings")
class TestEnvironmentTemperatureSettings:

    def test_check_environment_temperature_settings_tier2_header(self, peripheral_settings_page):
        result = peripheral_settings_page.get_environment_temperature_settings_tier2_header_text()
        expected_val = "Environment Temperature Settings"

        assert expected_val == result

    def test_check_temperature_trap_title(self, peripheral_settings_page):
        result = peripheral_settings_page.get_temperature_trap_title_text()
        expected_val = "Temperature Trap"

        assert expected_val == result

    def test_check_temperature_trap_option_one_text(self, peripheral_settings_page):
        result = peripheral_settings_page.get_temperature_trap_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_temperature_trap_option_two_text(self, peripheral_settings_page):
        result = peripheral_settings_page.get_temperature_trap_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_temperature_trap_is_disabled(self, peripheral_settings_page):
        opt = peripheral_settings_page.get_checked_temperature_trap_option()
        expected_val = "Disabled"

        assert opt == expected_val, "default temperature trap is not Disabled"

    def test_check_high_threshold_title_and_value(self, peripheral_settings_page):
        title, value = peripheral_settings_page.get_high_threshold_title_and_value()
        expected_title = "High Threshold (-100-200)"
        expected_val = "50"

        assert expected_title == title
        assert expected_val == value

    def test_check_high_threshold_option_text(self, peripheral_settings_page):
        result = peripheral_settings_page.get_high_threshold_option_text()
        expected_val = "Default"

        assert expected_val == result

    def test_check_low_threshold_title_and_value(self, peripheral_settings_page):
        title, value = peripheral_settings_page.get_low_threshold_title_and_value()
        expected_title = "Low Threshold (-100-200)"
        expected_val = "10"

        assert expected_title == title
        assert expected_val == value

    def test_check_low_threshold_option_text(self, peripheral_settings_page):
        result = peripheral_settings_page.get_low_threshold_option_text()
        expected_val = "Default"

        assert expected_val == result

    def test_check_environment_temperature_settings_button(self, peripheral_settings_page):
        result = peripheral_settings_page.get_environment_temperature_settings_button_value()
        expected_result = "Apply"

        assert expected_result == result
