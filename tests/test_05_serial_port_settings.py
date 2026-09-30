# tests/test_5_serial_port_settings.py
import time
import allure
import sys
import os

from webui.utils.all_exist_in_order import all_exist_in_order
from webui.mixins.TestUtils import ValueCheckMixins


@allure.title("Serial Port Settings")
class TestSerialPortSettings:

    def test_check_header_is_correct(self, serial_port_settings_page):
        res = serial_port_settings_page.get_page_header_text()
        expected_val = "Serial Port Settings"

        assert res == expected_val, "header is not correct"


    def test_check_tier2_header_is_correct(self, serial_port_settings_page):
        res = serial_port_settings_page.get_tier2_header_text()
        expected_val = "Serial Port Settings"

        assert res == expected_val, "header is not correct"

    def test_check_baud_rate_default_value(self, serial_port_settings_page):
        title, value = serial_port_settings_page.get_baud_rate()
        expected_title = "Baud Rate"
        expected_value = "115200"

        assert title == expected_title, "baud rate is not correct"
        assert value == expected_value, "baud rate value is not correct"

    def test_check_auto_logout_default_value(self, serial_port_settings_page):
        title, value = serial_port_settings_page.get_auto_logout()
        expected_title = "Auto Logout"
        expected_value = "10 minutes"

        assert title == expected_title, "auto logout is not correct"
        assert value == expected_value, "auto logout value is not correct"

    def test_check_data_bits_default_value(self, serial_port_settings_page):
        title, value = serial_port_settings_page.get_data_bits()
        expected_title = "Data Bits"
        expected_value = "8"

        assert title == expected_title, "data bits is not correct"
        assert value == expected_value, "data bits value is not correct"

    def test_check_parity_bits_default_value(self, serial_port_settings_page):
        title, value = serial_port_settings_page.get_parity_bits()
        expected_title = "Parity Bits"
        expected_value = "None"

        assert title == expected_title, "parity bits is not correct"
        assert value == expected_value, "parity bits value is not correct"

    def test_stop_bits_default_value(self, serial_port_settings_page):
        title, value = serial_port_settings_page.get_stop_bits()
        expected_title = "Stop Bits"
        expected_value = "1"

        assert title == expected_title, "stop bits is not correct"
        assert value == expected_value, "stop bits value is not correct"



