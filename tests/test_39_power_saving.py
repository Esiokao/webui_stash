# test_39_power_saving.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("power_saving.global_settings")
class TestGlobalSettings:

    def test_check_header(self, power_saving_page):
        result = power_saving_page.get_page_header_text()
        expected_val = "Power Saving"

        assert expected_val == result

    def test_check_global_settings_tier2_header(self, power_saving_page):
        result = power_saving_page.get_global_settings_tier2_header_text()
        expected_val = "Global Settings"

        assert expected_val == result

    def test_check_function_version_title_and_value(self, power_saving_page):
        title, value = power_saving_page.get_function_version_title_and_value()
        expected_title = "Function Version"
        expected_val = "3.0"

        assert expected_title == title
        assert expected_val == value

    def test_check_link_status_detection_version_title(self, power_saving_page):
        title = power_saving_page.get_link_status_detection_version_title()
        expected_title = "Link Status Detection"

        assert expected_title == title

    def test_check_link_status_detection_version_option_one_text(self, power_saving_page):
        result = power_saving_page.get_link_status_detection_version_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_link_status_detection_version_option_two_text(self, power_saving_page):
        result = power_saving_page.get_link_status_detection_version_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result
    
    def test_default_link_status_detection_version_is_disabled(self, power_saving_page):
        opt = power_saving_page.get_checked_link_status_detection_version_option()
        expected_val = "Disabled"

        assert expected_val == opt, "default link status detection version is not Disabled"

    def test_check_Global_Settings_button_text(self, power_saving_page):
        result = power_saving_page.get_Global_Settings_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_advanced_power_saving_settings_port_num_title(self, power_saving_page):
        result = power_saving_page.get_advanced_power_saving_settings_port_num_title()
        expected_val = [str(i) for i in range(1, 53)]

        assert expected_val == result

@allure.title("power_saving.advanced_power_saving_settings")
class TestAdvancedPowerSavingSettings:

    def test_check_advanced_power_saving_settings_title(self, power_saving_page):
        result = power_saving_page.get_advanced_power_saving_settings_title()
        expected_val = "Advanced Power Saving Settings"

        assert expected_val == result

    def test_check_type_title_and_value(self, power_saving_page):
        title, value = power_saving_page.get_type_title_and_value()
        expected_title = "Type"
        expected_val = "LED Shut-off"

        assert expected_title == title
        assert expected_val == value

    def test_check_time_profile_1_title_and_value(self, power_saving_page):
        title, value = power_saving_page.get_time_profile_1_title_and_value()
        expected_title = "Time Profile 1"
        expected_val = "None"

        assert expected_title == title
        assert expected_val == value

    def test_check_state_title_and_value(self, power_saving_page):
        title, value = power_saving_page.get_state_title_and_value()
        expected_title = "State"
        expected_val = "Disabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_time_profile_2_title_and_value(self, power_saving_page):
        title, value = power_saving_page.get_time_profile_2_title_and_value()
        expected_title = "Time Profile 2"
        expected_val = "None"

        assert expected_title == title
        assert expected_val == value

    def test_check_select_all_button_text(self, power_saving_page):
        result = power_saving_page.get_select_all_button_text()
        expected_val = "Select All"

        assert expected_val == result

    def test_check_clear_button_text(self, power_saving_page):
        result = power_saving_page.get_clear_button_text()
        expected_val = "Clear"

        assert expected_val == result
        
    def test_check_apply_button_text(self, power_saving_page):
        result = power_saving_page.get_apply_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_advanced_power_saving_settings_port_num_title(self, power_saving_page):
        result = power_saving_page.get_advanced_power_saving_settings_port_num_title()
        expected_val = [str(i) for i in range(1, 53)]

        assert expected_val == result

@allure.title("power_saving.summary")
class TestSummary:

    def test_check_summary_header(self, power_saving_page):
        result = power_saving_page.get_summary_header_text()
        expected_val = "Summary"

        assert expected_val == result

    def test_table_title(self, power_saving_page):
        result = power_saving_page.get_table_title()
        expected_val = ["Type", "State", "Time Profile 1", "Time Profile 2", "Port"]

        assert expected_val == result

    def test_led_shut_off_table_value(self, power_saving_page):
        result = power_saving_page.get_led_shut_off_table_value()
        expected_val = ["LED Shut-off", "Disabled", "None"]

        assert expected_val == result

    def test_port_shut_off_table_value(self, power_saving_page):
        result = power_saving_page.get_port_shut_off_table_value()
        expected_val = ["Port Shut-off", "Disabled", "None"]

        assert expected_val == result

    def test_system_hibernation_table_value(self, power_saving_page):
        result = power_saving_page.get_system_hibernation_table_value()
        expected_val = ["System Hibernation", "Disabled", "All Port"]

        assert expected_val == result
