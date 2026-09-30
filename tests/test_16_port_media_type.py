# test_16_port_media_type.py

import allure
import pytest
import asyncio

from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("port_media_type")
class TestPortMediaType:

    def test_check_header(self, port_media_type_page):
        result = port_media_type_page.get_page_header_text()
        expected_val = "Port Media Type"

        assert expected_val == result

    def test_check_port_media_type_tier2_header(self, port_media_type_page):
        result = port_media_type_page.get_port_media_type_tier2_header_text()
        expected_val = "Port Media Type"

        assert expected_val == result

    def test_check_table_title(self, port_media_type_page):
        result = port_media_type_page.get_table_title()
        expected_val = ["Port", "Type", "Vendor Name", "OUI", "PN", "Rev", "SN", "Date Code"]

        assert expected_val == result

    def test_check_table_value(self, port_media_type_page):
        result = port_media_type_page.get_table_value()
        expected_val = ["1", "1000MBASE-T", "-", "-", "-", "-", "-", "-"]

        assert expected_val == result