# tests/test_3_system_settings.py

import time
import allure
import sys
import os
import pytest
from webui.utils.all_exist_in_order import all_exist_in_order
from webui.mixins.TestUtils import ValueCheckMixins

@allure.title("System Settings.IPInformation")
class TestIPInformation():
    def test_check_ip_config_mode_options(self, system_settings_page):
        option_one = system_settings_page.get_ip_config_option_one_text()
        option_two = system_settings_page.get_ip_config_option_two_text()

        assert option_one == "Static", "check failed, option one should be static"
        assert option_two == "DHCP", "check failed, option two should be static"

    def test_check_if_static_is_default_selected(self, system_settings_page):
        select_input_text = system_settings_page.get_selected_ip_config_mode()

        assert select_input_text == "Static"

    def test_check_interface_name(self, system_settings_page):
        title, value = system_settings_page.get_interface_name_title_and_value()

        assert title == "Interface Name"
        assert value == "System"

    def test_check_vlan_name(self, system_settings_page):
        title, value = system_settings_page.get_vlan_name_title_and_value()

        assert title == "Vlan Name"
        assert value == "default"

    def test_check_ip_address(self, system_settings_page):
        title, value = system_settings_page.get_ip_address_title_and_value()

        assert title == "IP Address"
        assert value == "10.90.90.90"

    def test_check_subnet_mask(self, system_settings_page):
        title, value = system_settings_page.get_subnet_mask_title_and_value()
        
        assert title == "Subnet Mask"
        assert value == "255.0.0.0"
        
    def test_check_gateway_title_and_value(self, system_settings_page):
        title, value = system_settings_page.get_gateway_title_and_value()
        
        assert title == "Gateway"
        assert value == "0.0.0.0"

    def test_check_dhcp_option_12_title_and_value(self, system_settings_page):
        title, value = system_settings_page.get_dhcp_option_12_state_title_and_value()

        assert title == "DHCP Option 12 State"
        assert value == "Disabled"

    def test_check_dhcp_option_77_title_and_value(self, system_settings_page):
        title, value = system_settings_page.get_dhcp_option_77_title_and_value()

        assert title == "Dhcp Option77"
        assert value == ""

    def test_check_dhcp_option_77_table_title(self, system_settings_page):
        title_cells = system_settings_page.get_dhcp_option_77_table_title_columns()

        expected_titls = ['Index', 'User Class Info', 'Action']

        assert title_cells == expected_titls

    def test_check_if_dhcp_option_77_table_is_empty(self, system_settings_page):

        assert system_settings_page.check_if_dhcp_option_77_table_is_empty() == True

@allure.title("System Settings.DeviceInformation")
class TestSystemInformation():

    def test_check_system_name(self, system_settings_page):
        title, value = system_settings_page.get_system_name_title_and_value()

        assert title == "System Name"
        assert value == os.getenv("SYSTEM_NAME")

    def test_check_system_location(self, system_settings_page):
        title, value = system_settings_page.get_system_location_title_and_value()

        assert title == "System Location"
        assert value == ""

    def test_check_system_contact(self, system_settings_page):
        title, value = system_settings_page.get_system_contact_title_and_value()

        assert title == "System Contact"
        assert value == ""

    def test_check_login_timeout(self, system_settings_page):
        title, value = system_settings_page.get_login_timeout_title_and_value()

        assert title == "Login Timeout (3-30 minutes)"
        assert value == "3"
