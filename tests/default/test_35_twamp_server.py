# test_35_twamp_server.py


import allure


@allure.title("twamp_server")
class TestTwampServer:
    def test_check_header(self, twamp_server_page):
        result = twamp_server_page.get_page_header_text()
        expected_val = "TWAMP Server"

        assert expected_val == result

    def test_check_twamp_server_tier2_header(self, twamp_server_page):
        result = twamp_server_page.get_twamp_server_tier2_header_text()
        expected_val = "Twamp Server Settings"

        assert expected_val == result

    def test_check_state_title_and_value(self, twamp_server_page):
        title, value = twamp_server_page.get_state_title_and_value()
        expected_title = "State"
        expected_val = "Disabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_protocol_title_and_value(self, twamp_server_page):
        title, value = twamp_server_page.get_protocol_title_and_value()
        expected_title = "Protocol"
        expected_val = "IPv4"

        assert expected_title == title
        assert expected_val == value

    def test_check_age_time_title_and_value(self, twamp_server_page):
        title, value = twamp_server_page.get_age_time_title_and_value()
        expected_title = "Age Time (5-60)"
        expected_val = "10"

        assert expected_title == title
        assert expected_val == value

    def test_check_auth_mode_title_and_value(self, twamp_server_page):
        title, value = twamp_server_page.get_auth_mode_title_and_value()
        expected_title = "Auth Mode"
        expected_val = "Unauthenticated"

        assert expected_title == title
        assert expected_val == value

    def test_check_minimum_udp_port_title_and_value(self, twamp_server_page):
        title, value = twamp_server_page.get_minimum_udp_port_title_and_value()
        expected_title = "Minimum UDP Port (1063-65535)"
        expected_val = "20000"

        assert expected_title == title
        assert expected_val == value

    def test_check_twamp_server_button_text(self, twamp_server_page):
        result = twamp_server_page.get_twamp_server_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_twamp_server_table_title(self, twamp_server_page):
        result = twamp_server_page.get_twamp_server_table_title()
        expected_val = ["Client", "Sessions", "Action"]

        assert expected_val == result

    def test_check_twamp_server_table_empty(self, twamp_server_page):
        result = twamp_server_page.get_table_default_is_empty()

        assert result

    def test_check_refresh_button_text(self, twamp_server_page):
        result = twamp_server_page.get_refresh_button_text()
        expected_val = "Refresh"

        assert expected_val == result
