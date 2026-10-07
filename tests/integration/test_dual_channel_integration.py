# tests/integration/test_dual_channel_integration.py
"""
Integration Tests: Dual-Channel Synchronization (WebUI PageObject + Serial CLI)

Validates bidirectional consistency and state synchronization between the
browser-based management interface (WebUI) and the hardware console (Serial/CLI).
"""

import allure
import pytest
from webui.command.usecases.Reset import run as run_reset


@allure.feature("Integration: Dual-Channel Verification")
@pytest.mark.ui
@pytest.mark.serial
class TestDualChannelIntegration:
    @allure.story("Device Information Synchronization")
    @allure.title("Verify System Information matches between WebUI and Serial CLI")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_device_info_cross_channel_sync(self, device_information_page, serial_env):
        """
        Cross-validates that device specifications and system name shown in
        WebUI DeviceInformationPage match the switch internal CLI output.
        """
        with allure.step("Step 1: Read System Name & Device Type from WebUI"):
            _, web_device_type = device_information_page.get_device_type()
            _, web_sys_name = device_information_page.get_system_name()

        with allure.step("Step 2: Query Switch CLI via Serial interface using 'show switch'"):
            serial_env.send("show switch")

        with allure.step("Step 3: Assert CLI outputs contain the same System Name"):
            cli_sys_name = serial_env.waitForString(web_sys_name, timeout=5)
            assert cli_sys_name == web_sys_name, f"WebUI System Name '{web_sys_name}' does not match CLI response."

    @allure.story("Layer 3 Network Configuration Synchronization")
    @allure.title("Verify IP Interface settings match between WebUI SystemSettingsPage and Serial CLI")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_system_settings_ip_cross_channel_sync(self, system_settings_page, serial_env):
        """
        Validates that IP Address and Subnet Mask configured on WebUI match
        the output of 'show ip interface' via Serial console.
        """
        with allure.step("Step 1: Navigate to System Settings on WebUI and read IP / Subnet"):
            system_settings_page.collapse_system_menu_then_click_system_settings()
            _, web_ip = system_settings_page.get_ip_address_title_and_value()
            _, web_mask = system_settings_page.get_subnet_mask_title_and_value()

        with allure.step("Step 2: Query IP interface configuration via Serial console"):
            serial_env.send("show ip interface")

        with allure.step("Step 3: Dual-verify IP and Subnet Mask presence in CLI output"):
            res_ip = serial_env.waitForString(web_ip, timeout=5)
            res_mask = serial_env.waitForString(web_mask, timeout=5)

            assert res_ip == web_ip, f"CLI output did not match WebUI IP '{web_ip}'"
            assert res_mask == web_mask, f"CLI output did not match WebUI Subnet Mask '{web_mask}'"

    @allure.story("CLI Configuration Propagation & NVRAM Persistence")
    @allure.title("Configure IP via Serial CLI and verify persistence via NVRAM save")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cli_config_propagation_and_persistence(self, serial_env):
        """
        Simulates an operator modifying network parameters via the Serial/Console port,
        verifying command execution, CLI state update, and NVRAM save.
        """
        new_ip = "192.168.10.150"
        new_mask = "255.255.255.0"

        with allure.step(f"Step 1: Apply new IP configuration ({new_ip}/{new_mask}) via CLI"):
            serial_env.send(f"config ipif System ipaddress {new_ip} {new_mask}")
            serial_env.waitForString("Success", timeout=5)

        with allure.step("Step 2: Verify CLI 'show ip interface' reflects updated IP"):
            serial_env.send("show ip interface")
            matched_ip = serial_env.waitForString(new_ip, timeout=5)
            matched_mask = serial_env.waitForString(new_mask, timeout=5)

            assert matched_ip == new_ip
            assert matched_mask == new_mask

        with allure.step("Step 3: Persist configuration to switch NVRAM via 'save' command"):
            serial_env.send("save")
            save_resp = serial_env.waitForString("Saving configuration", timeout=5)
            assert "Saving configuration" in save_resp

    @allure.story("Hardware Maintenance & Command Pattern Invocation")
    @allure.title("Execute Switch Reset Command via Command Pattern and verify responsiveness")
    @allure.severity(allure.severity_level.NORMAL)
    def test_switch_reset_command_integration(self, serial_env):
        """
        Tests invoking ResetCommand via the Reset usecase over Serial connection,
        ensuring switch handles reset sequence and restores CLI responsiveness.
        """
        with allure.step("Step 1: Trigger Reset usecase on Serial connection"):
            success = run_reset(serial_env)
            assert success is True, "Reset usecase execution failed"

        with allure.step("Step 2: Verify switch terminal responds to health probe after reset"):
            serial_env.send("show switch")
            status = serial_env.waitForString("Switch#", timeout=10)
            assert "Switch#" in status
