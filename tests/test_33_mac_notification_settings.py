# test_33_mac_notification_settings.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("mac_notification_settings.mac_notification_global_settings")
class TestMacNotificationGlobalSettings:

    def test_check_header(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_page_header_text()
        expected_val = "MAC Notification Settings"

        assert expected_val == result

    def test_check_mac_notification_settings_tier2_header(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_mac_notification_settings_tier2_header_text()
        expected_val = "MAC Notification Global Settings"

        assert expected_val == result

    def test_check_state_title(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_state_title_text()
        expected_val = "State"

        assert expected_val == result

    def test_check_state_option_one_text(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_state_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_state_option_two_text(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_state_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result
    
    def test_default_state_is_disabled(self, mac_notification_settings_page):
        opt = mac_notification_settings_page.get_checked_state_option()
        expected_val = "Disabled"

        assert opt == expected_val, "default state is not Disabled"

    def test_check_interval_title_and_value(self, mac_notification_settings_page):
        title, value = mac_notification_settings_page.get_interval_title_and_value()
        expected_title = "Interval(1-2147483647 sec)"
        expected_value = "1"

        assert expected_title == title
        assert expected_value == value

    def test_check_history_size_title_and_value(self, mac_notification_settings_page):
        title, value = mac_notification_settings_page.get_history_size_title_and_value()
        expected_title = "History Size (1-500)"
        expected_value = "1"

        assert expected_title == title
        assert expected_value == value

    def test_check_mac_notification_global_settings_button_text(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_mac_notification_global_settings_button_text()
        expected_val = "Apply"

        assert expected_val == result


@allure.title("mac_notification_settings.mac_notification_port_settings")
class TestMacNotificationPortSettings:

    def test_check_MAC_Notification_Port_Settings_Table_header(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_MAC_Notification_Port_Settings_Table_header_text()
        expected_val = "MAC Notification Port Settings"

        assert expected_val == result

    def test_check_from_port_title_and_value(self, mac_notification_settings_page):
        title, value = mac_notification_settings_page.get_from_port_title_and_value()
        expected_title = "From Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_to_port_title_and_value(self, mac_notification_settings_page):
        title, value = mac_notification_settings_page.get_to_port_title_and_value()
        expected_title = "To Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_state_title_and_value(self, mac_notification_settings_page):
        title, value = mac_notification_settings_page.get_state_title_and_value()
        expected_title = "State"
        expected_val = "Disabled"

        assert expected_title == title
        assert expected_val == value
    
    def test_check_MAC_Notification_Port_Settings_Table_button_text(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_MAC_Notification_Port_Settings_Table_button_text()
        expected_val = "Apply"

        assert expected_val == result

@allure.title("mac_notification_settings.MAC_Notification_Port_State_Table")
class TestMacNotificationPortStateTable:

    def test_check_MAC_Notification_Port_State_Table_header(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_MAC_Notification_Port_State_Table_header_text()
        expected_val = "MAC Notification Port State Table"

        assert expected_val == result

    def test_check_MAC_Notification_Port_State_table_title(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_MAC_Notification_Port_State_table_title()
        expected_val = ["Port", "State"]

        assert expected_val == result

    def test_check_MAC_Notification_Port_State_table_value(self, mac_notification_settings_page):
        result = mac_notification_settings_page.get_MAC_Notification_Port_State_table_value()
        expected_val = ["1", "Disabled"]

        assert expected_val == result
        
        
