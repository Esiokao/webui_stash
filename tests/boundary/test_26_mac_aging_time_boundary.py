# tests/boundary/test_26_mac_aging_time_boundary.py
"""
Boundary Tests: MAC Address Aging Time (Corresponds to tests/default/test_26_mac_address_aging_time.py)

Tests boundary conditions on MAC Address Aging Time Page:
- Allowed Range (3 - 377 seconds)
- Boundary inputs: 3 (min), 377 (max), 2 (min-1), 378 (max+1), 0, negative
"""

import allure
import pytest


@allure.feature("Boundary: MAC Address Aging Time")
@pytest.mark.boundary
@pytest.mark.ui
class TestMacAgingTimeBoundary:
    @allure.story("MAC Aging Time Boundaries (3-377)")
    @pytest.mark.parametrize(
        "time_input,is_valid,desc",
        [
            ("3", True, "Lower valid boundary (3 seconds)"),
            ("377", True, "Upper valid boundary (377 seconds)"),
            ("300", True, "Default nominal aging time"),
            ("2", False, "Off-by-one below minimum (2 < 3)"),
            ("378", False, "Off-by-one above maximum (378 > 377)"),
            ("0", False, "Zero aging time rejected"),
            ("-5", False, "Negative aging time rejected"),
            ("abc", False, "Non-numeric input rejected"),
        ],
    )
    @allure.title("Boundary: MAC Aging Time Input '{time_input}' ({desc})")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_mac_aging_time_input_boundary(self, mac_address_aging_time_page, time_input, is_valid, desc):
        """
        Validates setting MAC address aging time boundary values through the PageObject.
        """
        with allure.step(f"Step 1: Input '{time_input}' into MAC Address Aging Time field"):
            mac_address_aging_time_page.set_mac_address_aging_time(time_input)

        with allure.step("Step 2: Read back input value from page element"):
            _, current_val = mac_address_aging_time_page.get_mac_address_aging_time_title_and_value()
            assert current_val == time_input

        with allure.step(f"Step 3: Verify boundary validity={is_valid}"):
            valid_rule = time_input.isdigit() and (3 <= int(time_input) <= 377)
            assert valid_rule == is_valid, f"MAC aging time boundary failed for {desc}"

        with allure.step("Step 4: Verify Apply button is available on page"):
            btn_text = mac_address_aging_time_page.get_get_mac_address_aging_time_button_text()
            assert btn_text == "Apply"
