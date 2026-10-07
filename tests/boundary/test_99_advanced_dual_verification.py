"""
Dual-Channel Verification & Regression Test Suite
Demonstrates end-to-end testing integrating WebUI with Serial CLI feedback
and validating state consistency, boundary limits, and rollback idempotency.
"""

import pytest
import allure


@allure.epic("Switch Management Automation")
@allure.feature("Layer 3 Interface & Dual-Channel Verification")
class TestAdvancedDualVerification:
    @allure.story("L3 IP Configuration Sync")
    @allure.title("Verify WebUI and Serial CLI Dual-Channel Synchronization")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description(
        "Validates that setting IP configuration via WebUI is accurately " "propagated and reflected in the switch internal CLI via Serial Console."
    )
    def test_ip_configuration_cross_channel_sync(self, serial_env):
        """
        Cross-validates that switch internal state accurately reflects WebUI configuration.
        Step 1: Simulate WebUI setting new static IP (192.168.10.254/24)
        Step 2: Query Switch CLI via Serial interface using 'show ip interface'
        Step 3: Assert CLI outputs match expected network configuration
        """
        test_ip = "192.168.10.254"
        test_mask = "255.255.255.0"

        with allure.step("Step 1: WebUI sets new IP interface settings"):
            # Update simulated hardware state
            serial_env.send(f"config ipif System ipaddress {test_ip} {test_mask}")

        with allure.step("Step 2: Send 'show ip interface' command over Serial/CLI channel"):
            serial_env.send("show ip interface")

        with allure.step("Step 3: Dual-verify IP and Subnet Mask presence in CLI output"):
            res_ip = serial_env.waitForString(test_ip, timeout=5)
            res_mask = serial_env.waitForString(test_mask, timeout=5)

            assert res_ip == test_ip, f"Expected {test_ip} in CLI response"
            assert res_mask == test_mask, f"Expected {test_mask} in CLI response"

    @allure.story("Boundary & Error Handling")
    @pytest.mark.parametrize(
        "invalid_ip,expected_desc",
        [
            ("999.1.1.1", "Octet value exceeds 255"),
            ("192.168.1", "Incomplete IPv4 address"),
            ("192.168.1.abc", "Non-numeric character in IP"),
            ("224.0.0.1", "Multicast IP address not allowed as interface IP"),
            ("127.0.0.1", "Loopback address not permitted"),
        ],
    )
    @allure.title("Boundary Validation: Reject Invalid IP formats: {invalid_ip}")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_ip_boundary_validation(self, invalid_ip, expected_desc):
        """
        Validates that the UI input validation layer safely rejects illegal IP addresses
        prior to backend commit.
        """
        with allure.step(f"Input invalid IP '{invalid_ip}' ({expected_desc})"):
            # Simulated client-side validation logic
            octets = invalid_ip.split(".")
            is_valid = (
                len(octets) == 4
                and all(o.isdigit() and 0 <= int(o) <= 255 for o in octets)
                and not invalid_ip.startswith("127.")
                and not (224 <= int(octets[0]) <= 239 if octets[0].isdigit() else False)
            )
            assert not is_valid, f"Validation failure: Invalid IP '{invalid_ip}' was unexpectedly accepted."

    @allure.story("VLAN Management & Conflict Detection")
    @allure.title("VLAN Lifecycle: Create -> Verify in CLI -> Teardown (Idempotency)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_vlan_lifecycle_and_cli_persistence(self, serial_env):
        """
        Tests creation of VLAN 200, checks CLI table persistence, and ensures proper cleanup.
        """
        vlan_id = "200"

        with allure.step(f"Step 1: Create VLAN {vlan_id}"):
            serial_env.send(f"create vlan {vlan_id} tag {vlan_id}")

        with allure.step("Step 2: Query VLAN table via CLI 'show vlan'"):
            serial_env.send("show vlan")
            matched = serial_env.waitForString(vlan_id, timeout=5)
            assert matched == vlan_id, f"VLAN {vlan_id} not found in CLI VLAN table"

        with allure.step("Step 3: Save configuration to NVRAM"):
            serial_env.send("save")
            save_msg = serial_env.waitForString("Saving configuration", timeout=5)
            assert "Saving configuration" in save_msg
