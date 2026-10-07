# tests/functional/vlan/test_vlan_list.py
"""
Functional Tests: 802.1Q VLAN Management (PageObject + VlanCommand Integration)

Validates 802.1Q VLAN page elements and tests functional VLAN provisioning
workflows using VlanCommand via Serial CLI and verifying state reflection on WebUI.
"""

import allure
import pytest

from webui.command.commands.VlanCommand import VlanCommand
from webui.command.Invokers.TestInvoker import TestInvoker


@allure.feature("Layer 2 Configuration")
@allure.story("802.1Q VLAN - Functional")
class TestVlanList:
    @allure.title("VLAN List: Verify Page Header is '802.1q'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_check_header(self, vlan_list_page):
        """Verifies that 802.1Q VLAN Page displays the correct header."""
        result = vlan_list_page.get_page_header_text()
        expected_val = "802.1q"
        assert expected_val in result.lower() or result == expected_val, f"Expected header '{expected_val}', got '{result}'"

    @allure.title("VLAN List: Verify Tier-2 Header Text")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_check_vlan_tier2_header(self, vlan_list_page):
        """Verifies that the tier-2 section header corresponds to 802.1Q VLAN Settings."""
        result = vlan_list_page.get_vlan_list_tier2_header_text()
        assert "VLAN" in result or "802.1Q" in result

    @allure.title("VLAN List: Verify Add VLAN and Delete Action Buttons")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_check_vlan_action_buttons(self, vlan_list_page):
        """Validates presence and text of Add VLAN and Delete buttons."""
        add_btn = vlan_list_page.get_add_vlan_button_text()
        del_btn = vlan_list_page.get_delete_vlan_button_text()

        assert "Add" in add_btn, f"Expected Add button, got '{add_btn}'"
        assert "Delete" in del_btn, f"Expected Delete button, got '{del_btn}'"

    @allure.title("VLAN List: Verify Table Column Headers")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_check_table_title(self, vlan_list_page):
        """Validates standard 802.1Q table headers: VID, VLAN Name, Type, Ports."""
        result = vlan_list_page.get_table_title()
        expected_columns = ["VID", "VLAN Name", "Type", "Ports"]

        for col in expected_columns:
            assert any(col.lower() in str(c).lower() for c in result), f"Column '{col}' not found in table headers: {result}"

    @allure.title("Functional: Create VLAN via VlanCommand and verify CLI & WebUI synchronization")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.ui
    @pytest.mark.serial
    def test_create_vlan_command_and_webui_sync(self, vlan_list_page, serial_env):
        """
        End-to-End Functional Test:
        1. Query initial VLAN table on WebUI.
        2. Execute VlanCommand via TestInvoker over serial_env to create VLAN 100.
        3. Verify VLAN 100 appears in switch CLI output ('show vlan').
        4. Refresh WebUI and assert VLAN 100 is reflected in the WebUI VLAN table.
        """
        test_vlan_id = "100"
        test_vlan_name = "vlan100"

        with allure.step("Step 1: Inspect initial state on WebUI"):
            vlan_list_page.refresh_vlan_table()

        with allure.step(f"Step 2: Provision VLAN {test_vlan_id} using VlanCommand"):
            vlan_command = VlanCommand(serial_env)
            vlans = [{"vlanName": test_vlan_name, "vlanID": test_vlan_id}]
            vlan_command.create_vlan(vlans)

            invoker = TestInvoker()
            invoker.addCommand(vlan_command)
            invoker.run()

        with allure.step(f"Step 3: Verify VLAN {test_vlan_id} in Switch CLI ('show vlan')"):
            serial_env.send("show vlan")
            matched_vid = serial_env.waitForString(test_vlan_id, timeout=5)
            assert matched_vid == test_vlan_id, f"VLAN {test_vlan_id} not found in CLI response"

        with allure.step(f"Step 4: Refresh WebUI and assert VLAN {test_vlan_id} appears in table"):
            vlan_list_page.refresh_vlan_table()
            is_present = vlan_list_page.is_vlan_in_table(test_vlan_id)
            assert is_present or test_vlan_id in str(vlan_list_page.get_table_rows()), f"VLAN {test_vlan_id} did not appear on WebUI VLAN table after creation."

    @allure.title("Functional: Batch Create Multiple VLANs via VlanCommand")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.serial
    def test_batch_create_vlans_via_command(self, serial_env):
        """
        Validates batch VLAN provisioning using VlanCommand with multiple entries.
        """
        batch_vlans = [
            {"vlanName": "vlan10", "vlanID": "10"},
            {"vlanName": "vlan20", "vlanID": "20"},
            {"vlanName": "vlan30", "vlanID": "30"},
        ]

        with allure.step(f"Step 1: Execute batch VLAN provisioning for {len(batch_vlans)} VLANs"):
            vlan_command = VlanCommand(serial_env)
            vlan_command.create_vlan(batch_vlans)

            invoker = TestInvoker()
            invoker.addCommand(vlan_command)
            invoker.run()

        with allure.step("Step 2: Query CLI table and assert all batch VLAN IDs exist"):
            serial_env.send("show vlan")
            for item in batch_vlans:
                vid = item["vlanID"]
                res = serial_env.waitForString(vid, timeout=5)
                assert res == vid, f"Batch VLAN ID {vid} not found in CLI"
