# test_15_port_error_disabled.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("port_error_disabled")
class TestPortErrorDisabled:

    def test_check_header(self, port_error_disabled_page):
        result = port_error_disabled_page.get_page_header_text()
        expected_val = "Port Error Disabled"

        assert expected_val == result

    def test_check_port_error_disabled_tier2_header(self, port_error_disabled_page):
        result = port_error_disabled_page.get_port_error_disabled_tier2_header_text()
        expected_val = "Port Error Disabled"

        assert expected_val == result

    def test_check_table_title(self, port_error_disabled_page):
        result = port_error_disabled_page.get_table_title()
        expected_val = ["Port", "Port State", "Connection Status", "Reason"]

        assert expected_val == result

    def test_check_table_default_is_empty(self, port_error_disabled_page):
        result = port_error_disabled_page.get_table_default_is_empty()

        assert result