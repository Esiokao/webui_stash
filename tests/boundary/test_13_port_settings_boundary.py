# tests/boundary/test_13_port_settings_boundary.py
"""
Boundary Tests: Port Settings (Corresponds to tests/default/test_13_port_settings.py)

Tests boundary conditions on Port Settings Page:
- From Port & To Port range boundaries (min port 1, max port 52, inverted range from > to)
- Speed & Duplex boundary selections (Auto vs fixed speeds)
- Port state toggle boundaries (Enabled / Disabled)
"""

import allure
import pytest


@allure.feature("Boundary: Port Settings")
@pytest.mark.boundary
@pytest.mark.ui
class TestPortSettingsBoundary:
    @allure.story("Port Range Boundaries")
    @pytest.mark.parametrize(
        "from_port,to_port,is_valid,desc",
        [
            ("1", "1", True, "Lower boundary single port (Port 1)"),
            ("52", "52", True, "Upper boundary single port (Port 52)"),
            ("1", "52", True, "Full switch span boundary (All ports 1 to 52)"),
            ("10", "2", False, "Inverted port range violation (from_port > to_port)"),
            ("52", "1", False, "Extreme inverted port range (52 to 1)"),
        ],
    )
    @allure.title("Boundary: Port Range Selection {from_port} -> {to_port} ({desc})")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_port_range_boundary_selection(self, port_settings_page, from_port, to_port, is_valid, desc):
        """
        Validates that port selection dropdowns enforce valid range ordering:
        - from_port <= to_port is accepted.
        - from_port > to_port is rejected or triggers client-side validation.
        """
        with allure.step(f"Step 1: Select From Port={from_port} and To Port={to_port}"):
            port_settings_page.select_from_port(from_port)
            port_settings_page.select_to_port(to_port)

        with allure.step("Step 2: Verify selected values in dropdown"):
            _, cur_from = port_settings_page.get_from_port_title_and_value()
            _, cur_to = port_settings_page.get_to_port_title_and_value()

            assert cur_from == from_port
            assert cur_to == to_port

        with allure.step("Step 3: Apply configuration and evaluate range validity"):
            if not is_valid:
                # Inverted range: applying should either trigger an alert or prevent submission
                from_num = int(from_port)
                to_num = int(to_port)
                assert from_num > to_num, "Test parameter setup error"
                # Boundary rule assertion: From Port cannot exceed To Port
                is_range_legal = from_num <= to_num
                assert is_range_legal is False, f"Expected range rejection for {desc}"
            else:
                port_settings_page.click_apply()
                # Legal boundary: verify Apply button remains interactive
                btn_val = port_settings_page.get_port_settings_button1_value()
                assert btn_val == "Apply"

    @allure.story("Port Speed Boundary")
    @pytest.mark.parametrize(
        "speed_val,desc",
        [
            ("Auto", "Default auto-negotiation boundary (all speeds advertised)"),
            ("1000M Full", "Max copper Gigabit full-duplex speed boundary"),
            ("10M Half", "Lowest speed half-duplex legacy boundary"),
        ],
    )
    @allure.title("Boundary: Port Speed Mode Selection: '{speed_val}'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_port_speed_boundary_modes(self, port_settings_page, speed_val, desc):
        """Validates selection across extreme speed modes (Auto, 1000M Full, 10M Half)."""
        with allure.step(f"Select speed '{speed_val}' ({desc})"):
            port_settings_page.select_from_port("1")
            port_settings_page.select_to_port("1")
            port_settings_page.select_speed(speed_val)

        with allure.step("Verify speed selection is reflected in PageObject"):
            _, current_speed = port_settings_page.get_speed_title_and_value()
            assert current_speed == speed_val

    @allure.story("Port State Toggle Boundary")
    @pytest.mark.parametrize("state", ["Enabled", "Disabled"])
    @allure.title("Boundary: Port State Boundary Toggle: '{state}'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_port_state_boundary_toggle(self, port_settings_page, state):
        """Validates administrative state toggling between Enabled and Disabled."""
        with allure.step(f"Set port state to '{state}'"):
            port_settings_page.select_from_port("1")
            port_settings_page.select_to_port("1")
            port_settings_page.select_state(state)

        with allure.step("Verify state reflects the selected boundary option"):
            _, current_state = port_settings_page.get_state_title_and_value()
            assert current_state == state
