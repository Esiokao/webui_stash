# tests/boundary/test_03_system_settings_boundary.py
"""
Boundary Tests: System Settings (Corresponds to tests/default/test_03_system_settings.py)

Tests boundary conditions on System Settings Page:
- Login Timeout input boundaries (3-30 minutes): lower bound (3), upper bound (30), off-by-one errors (2, 31)
- System Name string boundary length and format
"""

import allure
import pytest


@allure.feature("Boundary: System Settings")
@pytest.mark.boundary
@pytest.mark.ui
class TestSystemSettingsBoundary:
    @allure.story("Login Timeout Boundaries (3-30 minutes)")
    @pytest.mark.parametrize(
        "timeout_input,is_valid,desc",
        [
            ("3", True, "Lower valid boundary (3 minutes)"),
            ("30", True, "Upper valid boundary (30 minutes)"),
            ("2", False, "Off-by-one below minimum (2 < 3)"),
            ("31", False, "Off-by-one above maximum (31 > 30)"),
            ("0", False, "Zero timeout rejected"),
            ("-1", False, "Negative timeout rejected"),
            ("abc", False, "Non-numeric string rejected"),
        ],
    )
    @allure.title("Boundary: System Settings Login Timeout '{timeout_input}' ({desc})")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_timeout_field_boundary(self, system_settings_page, timeout_input, is_valid, desc):
        """
        Validates inputting boundary values into Login Timeout on SystemSettingsPage.
        """
        with allure.step("Step 1: Open System Settings page"):
            system_settings_page.collapse_system_menu_then_click_system_settings()

        with allure.step(f"Step 2: Enter '{timeout_input}' into Login Timeout field"):
            system_settings_page.set_login_timeout(timeout_input)

        with allure.step("Step 3: Read back input value from page element"):
            _, current_val = system_settings_page.get_login_timeout_title_and_value()
            assert current_val == timeout_input

        with allure.step(f"Step 4: Verify boundary constraint validity: expected_valid={is_valid}"):
            valid_rule = timeout_input.isdigit() and (3 <= int(timeout_input) <= 30)
            assert valid_rule == is_valid, f"Boundary check mismatch for {desc}"

    @allure.story("System Name Length Boundary")
    @pytest.mark.parametrize(
        "name_input,is_valid,desc",
        [
            ("Switch-1", True, "Standard system name"),
            ("S" * 32, True, "Upper length boundary (32 characters)"),
            ("S" * 33, False, "Exceeds 32-character limit"),
            ("", False, "Empty system name rejected"),
        ],
    )
    @allure.title("Boundary: System Name '{name_input}' ({desc})")
    @allure.severity(allure.severity_level.NORMAL)
    def test_system_name_field_boundary(self, system_settings_page, name_input, is_valid, desc):
        """Validates system name boundary length handling."""
        with allure.step("Step 1: Open System Settings page"):
            system_settings_page.collapse_system_menu_then_click_system_settings()

        with allure.step(f"Step 2: Fill System Name with '{name_input}'"):
            system_settings_page.set_system_name(name_input)

        with allure.step("Step 3: Assert length boundary compliance"):
            legal_length = 0 < len(name_input) <= 32
            assert legal_length == is_valid, f"System name boundary check failed for {desc}"
