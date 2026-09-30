# test_37_system_log_server.py


import allure


@allure.title("system_log_server.add_system_log_server")
class TestAddSystemLogServer:
    def test_check_header(self, system_log_server_page):
        result = system_log_server_page.get_page_header_text()
        expected_val = "System Log Server"

        assert expected_val == result

    def test_check_add_system_log_server_tier2_header(self, system_log_server_page):
        result = system_log_server_page.get_add_system_log_server_tier2_header_text()
        expected_val = "Add System Log Server"

        assert expected_val == result

    def test_check_server_id_title_and_value(self, system_log_server_page):
        title, value = system_log_server_page.get_server_id_title_and_value()
        expected_title = "Server ID"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_server_ipv4_address_title_and_value(self, system_log_server_page):
        title, value = system_log_server_page.get_server_ipv4_address_title_and_value()
        expected_title = "Server IPv4 Address"
        expected_val = "..."

        assert expected_title == title
        assert expected_val == value

    def test_check_server_ipv6_address_title_and_value(self, system_log_server_page):
        title, value = system_log_server_page.get_server_ipv6_address_title_and_value()
        expected_title = "Server IPv6 Address"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_v4_mode_default_options(self, system_log_server_page):
        assert system_log_server_page.get_checked_v4_mode_option() == True

    def test_check_v6_mode_default_options(self, system_log_server_page):
        assert system_log_server_page.get_checked_v6_mode_option() == False

    def test_check_domain_title_and_value(self, system_log_server_page):
        title, value = system_log_server_page.get_domain_title_and_value()
        expected_title = "Domain"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_domain_mode_default_options(self, system_log_server_page):
        assert system_log_server_page.get_checked_domain_mode_option() == False

    def test_check_severity_title_and_value(self, system_log_server_page):
        title, value = system_log_server_page.get_severity_title_and_value()
        expected_title = "Severity"
        expected_val = "Warning"

        assert expected_title == title
        assert expected_val == value

    def test_check_facility_title_and_value(self, system_log_server_page):
        title, value = system_log_server_page.get_facility_title_and_value()
        expected_title = "Facility"
        expected_val = "local0"

        assert expected_title == title
        assert expected_val == value

    def test_check_udp_port_title_and_value(self, system_log_server_page):
        title, value = system_log_server_page.get_udp_port_title_and_value()
        expected_title = "UDP Port (514 or 6000-65535)"
        expected_val = "514"

        assert expected_title == title
        assert expected_val == value

    def test_check_status_title_and_value(self, system_log_server_page):
        title, value = system_log_server_page.get_status_title_and_value()
        expected_title = "Status"
        expected_val = "Disabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_button_text(self, system_log_server_page):
        result = system_log_server_page.get_button_text()
        expected_val = "Apply"

        assert expected_val == result


@allure.title("system_log_server.system_log_server_list")
class TestSystemLogServerList:
    def test_check_system_log_server_list_header(self, system_log_server_page):
        result = system_log_server_page.get_system_log_server_list_header_text()
        expected_val = "System Log Server List"

        assert expected_val == result

    def test_check_total_entries_title(self, system_log_server_page):
        result = system_log_server_page.get_total_entries_title()
        expected_val = "Total Entries : 0"

        assert expected_val == result

    def test_check_table_title(self, system_log_server_page):
        result = system_log_server_page.get_table_title()
        expected_val = ["Server ID", "Server IP Address", "Severity", "Facility", "UDP Port", "Status"]

        assert expected_val == result

    def test_check_table_empty(self, system_log_server_page):
        result = system_log_server_page.get_table_default_is_empty()

        assert result
