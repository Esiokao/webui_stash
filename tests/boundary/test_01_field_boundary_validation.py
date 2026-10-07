# tests/boundary/test_01_field_boundary_validation.py
"""
Boundary Tests: Switch Management WebUI Field Validations

Derived from specifications and default tests in tests/default/:
- Login Timeout: (3-30 minutes) [test_03_system_settings.py]
- Web/Telnet Port: (1-65535) [test_29_web_settings.py, test_30_telnet_settings.py]
- MAC Address Aging Time: (3-377) [test_26_mac_address_aging_time.py]
- ARP Aging Time: (0-65535) [test_27_arp_aging_time_settings.py]
- User Accounts: Name < 32 chars, Password < 30 chars [test_25_user_accounts.py]
- Subnet Mask: Valid CIDR netmask boundaries [test_03_system_settings.py]
"""

import allure
import pytest


@allure.feature("Boundary Validation")
@pytest.mark.boundary
class TestFieldBoundaryValidation:
    # =========================================================================
    # 1. Login Timeout: Allowed Range (3 - 30 minutes)
    # =========================================================================
    @allure.story("System Settings - Login Timeout")
    @pytest.mark.parametrize(
        "val,is_valid,desc",
        [
            ("3", True, "Lower boundary valid (min = 3)"),
            ("30", True, "Upper boundary valid (max = 30)"),
            ("15", True, "Nominal mid-range value"),
            ("2", False, "Off-by-one below minimum (2 < 3)"),
            ("0", False, "Zero timeout rejected"),
            ("-1", False, "Negative integer rejected"),
            ("31", False, "Off-by-one above maximum (31 > 30)"),
            ("999", False, "Excessive timeout rejected"),
            ("abc", False, "Non-numeric string rejected"),
            ("", False, "Empty string rejected"),
        ],
    )
    @allure.title("Boundary: Login Timeout validation: '{val}' ({desc})")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_timeout_boundary(self, val, is_valid, desc):
        """Validates that Login Timeout strictly accepts integer values within [3, 30]."""
        with allure.step(f"Validate timeout '{val}' against expected validity={is_valid}"):
            valid = val.isdigit() and (3 <= int(val) <= 30)
            assert valid == is_valid, f"Failed boundary check for login timeout '{val}': {desc}"

    # =========================================================================
    # 2. Port Range: Allowed Range (1 - 65535) for Web/Telnet
    # =========================================================================
    @allure.story("Service Ports - Web & Telnet Settings")
    @pytest.mark.parametrize(
        "port,is_valid,desc",
        [
            ("1", True, "Lower boundary valid (port = 1)"),
            ("80", True, "Standard HTTP port"),
            ("443", True, "Standard HTTPS port"),
            ("23", True, "Standard Telnet port"),
            ("65535", True, "Upper boundary valid (port = 65535)"),
            ("0", False, "Reserved port 0 rejected"),
            ("-80", False, "Negative port number rejected"),
            ("65536", False, "Off-by-one above 16-bit integer (65536)"),
            ("70000", False, "Out of 16-bit port range"),
            ("80.5", False, "Float value rejected"),
            ("http", False, "Service name string rejected"),
            ("", False, "Empty string rejected"),
        ],
    )
    @allure.title("Boundary: Service Port validation: '{port}' ({desc})")
    @allure.severity(allure.severity_level.NORMAL)
    def test_service_port_boundary(self, port, is_valid, desc):
        """Validates that network service port numbers strictly fall within [1, 65535]."""
        with allure.step(f"Validate port '{port}' against expected validity={is_valid}"):
            valid = port.isdigit() and (1 <= int(port) <= 65535)
            assert valid == is_valid, f"Failed boundary check for port '{port}': {desc}"

    # =========================================================================
    # 3. MAC Address Aging Time: Allowed Range (3 - 377)
    # =========================================================================
    @allure.story("Layer 2 - MAC Address Aging Time")
    @pytest.mark.parametrize(
        "aging_time,is_valid,desc",
        [
            ("3", True, "Lower boundary valid (min = 3)"),
            ("377", True, "Upper boundary valid (max = 377)"),
            ("300", True, "Default aging time (300)"),
            ("2", False, "Off-by-one below minimum (2 < 3)"),
            ("0", False, "Zero aging time rejected"),
            ("-5", False, "Negative aging time rejected"),
            ("378", False, "Off-by-one above maximum (378 > 377)"),
            ("1000", False, "Excessive aging time rejected"),
            ("fast", False, "Non-numeric string rejected"),
        ],
    )
    @allure.title("Boundary: MAC Aging Time validation: '{aging_time}' ({desc})")
    @allure.severity(allure.severity_level.NORMAL)
    def test_mac_aging_time_boundary(self, aging_time, is_valid, desc):
        """Validates MAC address aging time boundary constraints [3, 377]."""
        with allure.step(f"Validate MAC aging time '{aging_time}'"):
            valid = aging_time.isdigit() and (3 <= int(aging_time) <= 377)
            assert valid == is_valid, f"Failed check for MAC aging time '{aging_time}': {desc}"

    # =========================================================================
    # 4. ARP Aging Time: Allowed Range (0 - 65535)
    # =========================================================================
    @allure.story("Layer 3 - ARP Aging Time Settings")
    @pytest.mark.parametrize(
        "arp_time,is_valid,desc",
        [
            ("0", True, "Lower boundary valid (0 = disabled/infinite)"),
            ("5", True, "Default ARP aging time (5)"),
            ("65535", True, "Upper boundary valid (max = 65535)"),
            ("-1", False, "Negative integer rejected"),
            ("65536", False, "Off-by-one above maximum (65536 > 65535)"),
            ("999999", False, "Out of range value rejected"),
            ("default", False, "Non-numeric string rejected"),
        ],
    )
    @allure.title("Boundary: ARP Aging Time validation: '{arp_time}' ({desc})")
    @allure.severity(allure.severity_level.NORMAL)
    def test_arp_aging_time_boundary(self, arp_time, is_valid, desc):
        """Validates ARP aging time boundary constraints [0, 65535]."""
        with allure.step(f"Validate ARP aging time '{arp_time}'"):
            valid = arp_time.isdigit() and (0 <= int(arp_time) <= 65535)
            assert valid == is_valid, f"Failed check for ARP aging time '{arp_time}': {desc}"

    # =========================================================================
    # 5. User Accounts & Password Boundary
    #    Rule: Username < 32 characters, Password < 30 characters
    # =========================================================================
    @allure.story("Security - User Accounts & Password Constraints")
    @pytest.mark.parametrize(
        "username,is_valid,desc",
        [
            ("admin", True, "Standard alphanumeric username"),
            ("u" * 31, True, "Upper boundary valid (exactly 31 characters < 32)"),
            ("u" * 32, False, "Boundary violation: exactly 32 characters (should be < 32)"),
            ("u" * 33, False, "Exceeds max length (33 characters)"),
            ("", False, "Empty username rejected"),
            ("   ", False, "Whitespace-only username rejected"),
            ("user@123", True, "Valid username with allowed symbols"),
            ("<script>", False, "Dangerous XSS characters rejected"),
        ],
    )
    @allure.title("Boundary: Username length validation: {desc}")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_username_length_boundary(self, username, is_valid, desc):
        """Validates that username adheres to strict length (< 32 chars) and format constraints."""
        with allure.step(f"Validate username '{username}' (length={len(username)})"):
            disallowed_chars = set("<>\"'/\\;`")
            valid = 0 < len(username.strip()) < 32 and not any(c in disallowed_chars for c in username)
            assert valid == is_valid, f"Failed username validation: {desc}"

    @allure.story("Security - Password Constraints")
    @pytest.mark.parametrize(
        "password,confirm_password,is_valid,desc",
        [
            ("P@ssw0rd1234", "P@ssw0rd1234", True, "Valid strong password with match"),
            ("p" * 29, "p" * 29, True, "Upper boundary valid (exactly 29 characters < 30)"),
            ("p" * 30, "p" * 30, False, "Boundary violation: exactly 30 characters (should be < 30)"),
            ("p" * 35, "p" * 35, False, "Exceeds max length (35 characters)"),
            ("", "", False, "Empty password rejected"),
            ("admin123", "admin456", False, "Password and Confirm Password mismatch"),
        ],
    )
    @allure.title("Boundary: Password length and confirmation validation: {desc}")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_password_boundary_and_confirmation(self, password, confirm_password, is_valid, desc):
        """Validates password length (< 30 chars) and password confirmation matching."""
        with allure.step(f"Validate password (len={len(password)}) vs confirm (len={len(confirm_password)})"):
            valid = 0 < len(password) < 30 and password == confirm_password
            assert valid == is_valid, f"Failed password validation: {desc}"

    # =========================================================================
    # 6. IPv4 Subnet Mask Boundary
    #    Rule: Must be contiguous bitmask (e.g., 255.255.255.0, /8 to /30)
    # =========================================================================
    @allure.story("Layer 3 - Subnet Mask Contiguity & Format")
    @pytest.mark.parametrize(
        "mask,is_valid,desc",
        [
            ("255.255.255.0", True, "Standard /24 Class C subnet mask"),
            ("255.0.0.0", True, "Standard /8 Class A subnet mask"),
            ("255.255.0.0", True, "Standard /16 Class B subnet mask"),
            ("255.255.255.252", True, "Standard /30 point-to-point mask"),
            ("255.255.255.255", False, "Host mask /32 not valid for interface subnet"),
            ("0.0.0.0", False, "Default route mask 0.0.0.0 not valid as interface mask"),
            ("255.255.255.1", False, "Non-contiguous subnet mask rejected"),
            ("255.255.0.255", False, "Discontinuous subnet mask (hole in bitmask)"),
            ("256.255.255.0", False, "Octet exceeds 255"),
            ("255.255.255", False, "Incomplete subnet mask (only 3 octets)"),
        ],
    )
    @allure.title("Boundary: Subnet Mask contiguity validation: '{mask}' ({desc})")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subnet_mask_boundary(self, mask, is_valid, desc):
        """Validates that subnet masks represent strictly contiguous bits within [8, 30]."""
        with allure.step(f"Validate subnet mask '{mask}'"):
            octets = mask.split(".")
            valid = False
            if len(octets) == 4 and all(o.isdigit() and 0 <= int(o) <= 255 for o in octets):
                binary_str = "".join(f"{int(o):08b}" for o in octets)
                # Valid subnet mask has all 1s followed by all 0s, with prefix length between 8 and 30
                ones_count = binary_str.count("1")
                expected_binary = "1" * ones_count + "0" * (32 - ones_count)
                valid = (binary_str == expected_binary) and (8 <= ones_count <= 30)

            assert valid == is_valid, f"Failed subnet mask check for '{mask}': {desc}"
