# test_24_snmp_trap_settings.py

import allure
import pytest
import asyncio
import os
from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("snmp_trap_settings.trap_settings")
class TestSNMPTrapSettings:

    def test_check_header(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_page_header_text()
        expected_val = "SNMP Trap Settings"

        assert expected_val == result

    def test_check_snmp_trap_settings_tier2_header(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_snmp_trap_settings_tier2_header_text()
        expected_val = "Trap Settings"

        assert expected_val == result

    def test_check_snmp_authentication_traps_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_snmp_authentication_traps_title_and_value()
        expected_title = "  SNMP Authentication Traps"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_system_coldstart_traps_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_system_coldstart_traps_title_and_value()
        expected_title = "  System Coldstart Traps"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_system_warmstart_traps_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_system_warmstart_traps_title_and_value()
        expected_title = "  System Warmstart Traps"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_port_link_up_and_link_down_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_port_link_up_and_link_down_title_and_value()
        expected_title = "  Port Link Up / Link Down"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_rstp_port_state_change_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_rstp_port_state_change_title_and_value()
        expected_title = "  RSTP Port State Change"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_firmware_upgrade_state_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_firmware_upgrade_state_title_and_value()
        expected_title = "  Firmware Upgrade State"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_port_security_violation_state_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_port_security_violation_state_title_and_value()
        expected_title = "  Port Security violation state"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_impb_violation_state_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_impb_violation_state_title_and_value()
        expected_title = "  IMPB Violation"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_loopback_detection_occuring_and_recovery_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_loopback_detection_occuring_and_recovery_title_and_value()
        expected_title = "  Loopback Detection occuring / recovery"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_dhcp_server_screening_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_dhcp_server_screening_title_and_value()
        expected_title = "  DHCP Server Screening"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_duplicate_ip_detected_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_duplicate_ip_detected_title_and_value()
        expected_title = "  Duplicate IP Detected"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_dhcpv6_server_screening_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_dhcpv6_server_screening_title_and_value()
        expected_title = "  DHCPv6 Server Screening"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_icmpv6_ra_all_node_filter_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_icmpv6_ra_all_node_filter_title_and_value()
        expected_title = "  ICMPv6 RA All Node Filter"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_login_and_logout_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_login_and_logout_title_and_value()
        expected_title = "  Login / Logout"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_duld_traps_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_duld_traps_title_and_value()
        expected_title = "  DULD Traps"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_rps_traps_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_rps_traps_title_and_value()
        expected_title = "  RPS Traps"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_dying_gasp_traps_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_dying_gasp_traps_title_and_value()
        expected_title = "  DyingGasp Traps"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_802_1x_traps_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_802_1x_traps_title_and_value()
        expected_title = "  802.1x Traps"
        expected_val = False

        assert expected_title == title
        assert expected_val == value

    def test_check_dying_gasp_traps_types_title_and_value(self, snmp_trap_settings_page):
        title, value = snmp_trap_settings_page.get_dying_gasp_traps_types_title_and_value()
        expected_title = "DyingGasp Traps Types"
        expected_val = "both"

        assert expected_title == title
        assert expected_val == value

    def test_check_trap_settings_button_text(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_trap_settings_button_text()
        expected_val = "Apply"

        assert expected_val == result


@allure.title("snmp_trap_settings.snmp_link_change_trap_port")
class TestSnmpLinkChangeTrapPort:

    def test_check_snmp_link_change_trap_port_table_header(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_snmp_link_change_trap_port_table_header()
        expected_val = "Snmp LinkChange Trap Port"

        assert expected_val == result

    def test_check_linkchange_trap_port_select_all_button_text(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_linkchange_trap_port_select_all_button_text()
        expected_val = "Select All"

        assert expected_val == result

    def test_check_linkchange_trap_port_clear_button_text(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_linkchange_trap_port_clear_button_text()
        expected_val = "Clear"

        assert expected_val == result

    def test_check_linkchange_trap_port_apply_button_text(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_linkchange_trap_port_apply_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_linkchange_port_num_title(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_linkchange_port_num_title()
        expected_val = [str(i) for i in range(1, 53)]

        assert expected_val == result

    def test_check_linkchange_port_default_status(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_linkchange_port_default_status()
        expected_val = [str(i) for i in range(1, 53)]

        assert expected_val == result


@allure.title("snmp_trap_settings.snmp_sending_trap_port")
class TestSnmpSendingTrapPort:

    def test_check_snmp_sending_trap_port_table_header(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_snmp_sending_trap_port_table_header()
        expected_val = "Snmp Sending Trap Port"

        assert expected_val == result

    def test_check_sending_trap_port_select_all_button_text(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_snmp_sending_trap_port_select_all_button_text()
        expected_val = "Select All"

        assert expected_val == result

    def test_check_sending_trap_port_clear_button_text(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_snmp_sending_trap_port_clear_button_text()
        expected_val = "Clear"

        assert expected_val == result

    def test_check_sending_trap_port_apply_button_text(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_snmp_sending_trap_port_apply_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_sending_trap_port_num_title(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_snmp_sending_trap_port_num_title()
        expected_val = [str(i) for i in range(1, 53)]

        assert expected_val == result

    def test_check_sending_trap_port_default_status(self, snmp_trap_settings_page):
        result = snmp_trap_settings_page.get_snmp_sending_trap_port_default_status()
        expected_val = [str(i) for i in range(1, 53)]

        assert expected_val == result
