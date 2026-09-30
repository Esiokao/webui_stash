# test_30_telnet_settings.py


import allure


@allure.title("Telnet_Settings")
class TestTelnetSettings:
    def test_check_header(self, telnet_settings_page):
        result = telnet_settings_page.get_page_header_text()
        expected_val = "Telnet Settings"

        assert expected_val == result

    def test_check_telnet_settings_tier2_header(self, telnet_settings_page):
        result = telnet_settings_page.get_telnet_settings_tier2_header_text()
        expected_val = "Telnet Settings"

        assert expected_val == result

    def test_check_telnet_state_title(self, telnet_settings_page):
        result = telnet_settings_page.get_telnet_state_title_text()
        expected_val = "Telnet State"

        assert expected_val == result

    def test_check_telnet_state_option_one_text(self, telnet_settings_page):
        result = telnet_settings_page.get_telnet_state_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_telnet_state_option_two_text(self, telnet_settings_page):
        result = telnet_settings_page.get_telnet_state_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_telnet_state_is_disabled(self, telnet_settings_page):
        opt = telnet_settings_page.get_checked_telnet_state_option()
        expected_val = "Disabled"

        assert opt == expected_val, "default telnet state is not Disabled"

    def test_check_port_title_and_value(self, telnet_settings_page):
        title, value = telnet_settings_page.get_port_title_and_value()
        expected_title = "Port (1-65535)"
        expected_value = "23"

        assert expected_title == title
        assert expected_value == value

    def test_check_telnet_settings_apply_button_text(self, telnet_settings_page):
        result = telnet_settings_page.get_telnet_settings_apply_button_text()
        expected_val = "Apply"

        assert expected_val == result
