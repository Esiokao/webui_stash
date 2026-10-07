# tests/functional/test_ip_interface_functional.py
"""
Functional Tests: IP Interface Settings
Tests write operations, state persistence, and UI interaction flows.
"""

import allure


@allure.feature("Layer 3 Configuration")
@allure.story("IP Interface Settings - Functional")
class TestIPInterfaceFunctional:
    @allure.title("Functional: Switch to DHCP mode disables static IP input fields")
    @allure.severity(allure.severity_level.NORMAL)
    def test_dhcp_mode_disables_static_inputs(self, ip_interface_page):
        """
        Validates that switching to DHCP mode causes the
        static IP / Subnet Mask fields to become read-only or hidden.
        """
        ip_interface_page.init()
        ip_interface_page.click_dhcp_radio()

        assert ip_interface_page.is_static_ip_fields_disabled(), "切換到 DHCP 後，靜態 IP/遮罩輸入框應為 Disabled 狀態"

    @allure.title("Functional: Cancel button discards unsaved changes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_button_discards_changes(self, ip_interface_page):
        """
        Validates that clicking Cancel after editing
        restores all fields to their previous values.
        """
        ip_interface_page.init()
        original = ip_interface_page.get_current_ip_address()

        ip_interface_page.fill_ip_address("10.10.10.10")
        ip_interface_page.click_cancel()

        restored = ip_interface_page.get_current_ip_address()
        assert restored == original, "Cancel 後 IP 應還原為原值"

    @allure.title("Functional: Apply static IP persists after page refresh")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_static_ip_persists_after_refresh(self, ip_interface_page):
        """
        Validates that a valid static IP configuration applied via WebUI
        is persisted and reflected after a full page reload.
        """
        ip_interface_page.init()
        new_ip = "192.168.10.100"

        ip_interface_page.configure_static_ip(new_ip, "255.255.255.0")
        ip_interface_page.click_apply()
        ip_interface_page.refresh_page()

        current_ip = ip_interface_page.get_current_ip_address()
        assert current_ip == new_ip, f"刷新後 IP 應為 {new_ip}，實際為 {current_ip}"
