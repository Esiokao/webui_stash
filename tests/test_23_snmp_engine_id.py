# test_23_snmp_engine_id.py

import allure
import pytest
import asyncio
import os
from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("snmp_engine_id")
class TestSNMPEngineID:

    def test_check_header(self, snmp_engine_id_page):
        result = snmp_engine_id_page.get_page_header_text()
        expected_val = "SNMP Engine ID"

        assert expected_val == result

    def test_check_snmp_engine_id_tier2_header(self, snmp_engine_id_page):
        result = snmp_engine_id_page.get_snmp_engine_id_tier2_header_text()
        expected_val = "SNMP Engine ID"

        assert expected_val == result

    def test_check_engine_id_title_and_value(self, snmp_engine_id_page):
        title, value = snmp_engine_id_page.get_engine_id_title_and_value()
        expected_title = "Engine ID"
        expected_val = os.getenv("SNMP_ENGINE_ID")

        assert expected_title == title
        assert expected_val == value

    def test_check_button1_text(self, snmp_engine_id_page):
        result = snmp_engine_id_page.get_button1_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_button2_text(self, snmp_engine_id_page):
        result = snmp_engine_id_page.get_button2_text()
        expected_val = "Default"

        assert expected_val == result

    def test_check_note_text(self, snmp_engine_id_page):
        value1, value2 = snmp_engine_id_page.get_note_text()
        expected_val1 = "Note:"
        expected_val2 = "Engine ID length is 10-64, the accepted character is from 0 to F."

        assert expected_val1 == value1
        assert expected_val2 == value2
